# -*- coding: utf-8 -*-
"""
F1STRAT : extractions OpenF1 (2023 à 2025) et Open-Meteo (2005 à 2025).

Bibliothèque standard uniquement (aucun pip install).
Lancer depuis ce dossier (PowerShell ou invite de commandes) :
    py extraction_api.py --test    une requête par source, pour vérifier l'accès
    py extraction_api.py           extraction complète (environ 30 à 45 minutes)
Relançable : les réponses déjà téléchargées (dossiers « brut ») sont réutilisées.

Sorties (dans 4_donnees) :
    openf1_2023_2025/   sessions, arrêts (durée dans la voie, immobilisation), dépassements
    meteo_open_meteo/   météo horaire des week-ends 2014 à 2025, climatologie 2005 à 2024
                        autour de chaque GP 2023 à 2025, prévisions archivées 2024 à 2025
Journal : journal_extraction.txt (dans ce dossier).
"""
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

ICI = Path(__file__).resolve().parent
DONNEES = ICI.parent
GP_CSV = ICI / "gp_2014_2025.csv"
OUT_OF = DONNEES / "openf1_2023_2025"
OUT_OM = DONNEES / "meteo_open_meteo"
JOURNAL = ICI / "journal_extraction.txt"
TEST = "--test" in sys.argv

# Pauses entre requêtes (s). OpenF1 gratuit : 3 req/s et 30 req/min.
# Open-Meteo gratuit : moins de 600 appels/min, 5 000/h, 10 000/jour.
PAUSE = {"api.openf1.org": 2.2, "open-meteo.com": 0.25}
_dernier_appel = {}

# Variables Open-Meteo (noms vérifiés dans la documentation le 21/10/2026).
VARS_HORAIRES = ["precipitation", "rain", "temperature_2m", "relative_humidity_2m",
                 "cloud_cover", "wind_speed_10m", "wind_direction_10m"]
VARS_JOURNALIERES = ["precipitation_sum", "precipitation_hours",
                     "temperature_2m_max", "temperature_2m_min"]
VARS_PREVISION = (["precipitation"] + [f"precipitation_previous_day{i}" for i in range(1, 8)]
                  + ["temperature_2m"] + [f"temperature_2m_previous_day{i}" for i in range(1, 4)])
CLIMATO_ANNEES = range(2005, 2025)   # 20 ans
CLIMATO_DEMI_FENETRE = 7             # jours de part et d'autre de la date du GP
PREVISION_DEBUT = date(2024, 1, 8)   # archives Open-Meteo complètes à partir de janvier 2024


def journal(msg):
    ligne = f"{datetime.now():%Y-%m-%d %H:%M:%S} {msg}"
    print(ligne)
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def _pause(url):
    hote = urllib.parse.urlparse(url).hostname or ""
    cle = next((k for k in PAUSE if hote.endswith(k)), None)
    if cle:
        attente = PAUSE[cle] - (time.time() - _dernier_appel.get(cle, 0))
        if attente > 0:
            time.sleep(attente)
        _dernier_appel[cle] = time.time()


def obtenir(url, fichier_brut):
    """Renvoie le JSON (liste ou dict) ou None. Met en cache dans fichier_brut."""
    if fichier_brut.exists():
        with open(fichier_brut, encoding="utf-8") as f:
            return json.load(f)
    fichier_brut.parent.mkdir(parents=True, exist_ok=True)
    for essai in range(1, 6):
        _pause(url)
        req = urllib.request.Request(url, headers={"User-Agent": "F1STRAT-extraction/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                donnees = json.loads(r.read().decode("utf-8"))
            with open(fichier_brut, "w", encoding="utf-8") as f:
                json.dump(donnees, f, ensure_ascii=False)
            return donnees
        except urllib.error.HTTPError as e:
            corps = e.read().decode("utf-8", "replace")[:300]
            if e.code == 404:          # OpenF1 : « No results found »
                journal(f"404 (aucune donnée) {url}")
                with open(fichier_brut, "w", encoding="utf-8") as f:
                    json.dump([], f)
                return []
            if e.code == 429 or e.code >= 500:
                journal(f"HTTP {e.code}, essai {essai}/5, attente {15 * essai} s : {url}")
                time.sleep(15 * essai)
                continue
            journal(f"ERREUR HTTP {e.code} {url} : {corps}")
            return None
        except Exception as e:  # réseau, délai, JSON invalide
            journal(f"ERREUR {type(e).__name__} essai {essai}/5 : {e} : {url}")
            time.sleep(10 * essai)
    journal(f"ABANDON après 5 essais : {url}")
    return None


def ecrire_csv(chemin, entete, lignes):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";", lineterminator="\n")
        w.writerow(entete)
        w.writerows(lignes)
    journal(f"écrit : {chemin.name} ({len(lignes)} lignes)")


def cles_union(enregistrements, prioritaires):
    cles = list(prioritaires)
    for e in enregistrements:
        for k in e:
            if k not in cles:
                cles.append(k)
    return cles


# ------------------------------------------------------------------ OpenF1
def openf1():
    journal("=== OpenF1 ===")
    brut = OUT_OF / "brut"
    sessions = []
    for annee in ([2024] if TEST else [2023, 2024, 2025]):
        url = f"https://api.openf1.org/v1/sessions?year={annee}&session_name=Race"
        s = obtenir(url, brut / f"sessions_{annee}.json")
        if s is None:
            journal(f"sessions {annee} indisponibles : OpenF1 interrompu")
            return
        sessions += [x for x in s if not x.get("is_cancelled")]
    sessions.sort(key=lambda x: x.get("date_start", ""))
    if TEST:
        sessions = sessions[-1:]
    tables = {"pit": [], "overtakes": []}
    for s in sessions:
        sk = s["session_key"]
        for ep in tables:
            d = obtenir(f"https://api.openf1.org/v1/{ep}?session_key={sk}", brut / f"{ep}_{sk}.json")
            for e in d or []:
                e = dict(e)
                e["_annee"] = s.get("year")
                e["_lieu"] = s.get("location")
                e["_date_course"] = s.get("date_start")
                tables[ep].append(e)
    ecrire_csv(OUT_OF / "sessions_course_2023_2025.csv",
               ["annee", "meeting_key", "session_key", "date_start", "location", "country_name",
                "circuit_short_name", "gmt_offset"],
               [[s.get(k) for k in ["year", "meeting_key", "session_key", "date_start", "location",
                                    "country_name", "circuit_short_name", "gmt_offset"]] for s in sessions])
    for ep, nom in [("pit", "arrets_2023_2025.csv"), ("overtakes", "depassements_2023_2025.csv")]:
        cles = cles_union(tables[ep], ["_annee", "_lieu", "_date_course", "session_key"])
        ecrire_csv(OUT_OF / nom, cles, [[e.get(k) for k in cles] for e in tables[ep]])
    avec_immo = sum(1 for e in tables["pit"] if e.get("stop_duration") is not None)
    journal(f"OpenF1 : {len(sessions)} courses, {len(tables['pit'])} arrêts "
            f"(dont {avec_immo} avec immobilisation), {len(tables['overtakes'])} dépassements")


# ------------------------------------------------------------- Open-Meteo
def lire_gp():
    with open(GP_CSV, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))


def fenetre_week_end(gp):
    course = date.fromisoformat(gp["date_course"])
    debut = date.fromisoformat(gp["date_ep1"]) if gp["date_ep1"] else course - timedelta(days=3)
    return debut, course


def deplier_horaire(rep, variables):
    h = (rep or {}).get("hourly") or {}
    temps = h.get("time") or []
    return [[t] + [h.get(v, [None] * len(temps))[i] for v in variables] for i, t in enumerate(temps)]


def meteo_week_ends():
    journal("=== Open-Meteo : météo horaire des week-ends 2014 à 2025 ===")
    brut = OUT_OM / "brut_archive"
    lignes = []
    gps = lire_gp()[:1] if TEST else lire_gp()
    for gp in gps:
        debut, fin = fenetre_week_end(gp)
        url = ("https://archive-api.open-meteo.com/v1/archive?" + urllib.parse.urlencode({
            "latitude": gp["latitude"], "longitude": gp["longitude"],
            "start_date": debut.isoformat(), "end_date": fin.isoformat(),
            "hourly": ",".join(VARS_HORAIRES), "timezone": "GMT"}))
        rep = obtenir(url, brut / f"{gp['saison']}_{int(gp['manche']):02d}_{gp['grand_prix_id']}.json")
        for l in deplier_horaire(rep, VARS_HORAIRES):
            lignes.append([gp["saison"], gp["manche"], gp["grand_prix_id"], gp["circuit_id"]] + l)
    ecrire_csv(OUT_OM / "meteo_week_ends_2014_2025.csv",
               ["saison", "manche", "grand_prix_id", "circuit_id", "heure_utc"] + VARS_HORAIRES, lignes)


def climatologie():
    journal("=== Open-Meteo : climatologie 2005 à 2024 autour des GP 2023 à 2025 ===")
    brut = OUT_OM / "brut_climatologie"
    vus, cibles = set(), []
    for gp in lire_gp():
        if int(gp["saison"]) < 2023:
            continue
        cle = (gp["circuit_id"], gp["date_course"][5:])
        if cle not in vus:
            vus.add(cle)
            cibles.append(gp)
    lignes = []
    for gp in (cibles[:1] if TEST else cibles):
        mmjj = gp["date_course"][5:]
        for annee in ([2024] if TEST else CLIMATO_ANNEES):
            centre = date.fromisoformat(f"{annee}-{mmjj}")
            debut = centre - timedelta(days=CLIMATO_DEMI_FENETRE)
            fin = centre + timedelta(days=CLIMATO_DEMI_FENETRE)
            url = ("https://archive-api.open-meteo.com/v1/archive?" + urllib.parse.urlencode({
                "latitude": gp["latitude"], "longitude": gp["longitude"],
                "start_date": debut.isoformat(), "end_date": fin.isoformat(),
                "daily": ",".join(VARS_JOURNALIERES), "timezone": "auto"}))
            rep = obtenir(url, brut / f"{gp['circuit_id']}_{mmjj}_{annee}.json")
            d = (rep or {}).get("daily") or {}
            for i, t in enumerate(d.get("time") or []):
                lignes.append([gp["circuit_id"], mmjj, annee, t, (date.fromisoformat(t) - centre).days]
                              + [d.get(v, [None] * (i + 1))[i] for v in VARS_JOURNALIERES])
    ecrire_csv(OUT_OM / "climatologie_gp_2005_2024.csv",
               ["circuit_id", "jour_gp_mm_jj", "annee", "date_locale", "ecart_jours"] + VARS_JOURNALIERES,
               lignes)


def previsions_archivees():
    journal("=== Open-Meteo : prévisions archivées (1 à 7 jours avant) 2024 à 2025 ===")
    brut = OUT_OM / "brut_previsions"
    lignes = []
    gps = [g for g in lire_gp() if date.fromisoformat(g["date_course"]) >= PREVISION_DEBUT]
    for gp in (gps[:1] if TEST else gps):
        debut, fin = fenetre_week_end(gp)
        url = ("https://previous-runs-api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode({
            "latitude": gp["latitude"], "longitude": gp["longitude"],
            "start_date": debut.isoformat(), "end_date": fin.isoformat(),
            "hourly": ",".join(VARS_PREVISION), "timezone": "GMT"}))
        rep = obtenir(url, brut / f"{gp['saison']}_{int(gp['manche']):02d}_{gp['grand_prix_id']}.json")
        for l in deplier_horaire(rep, VARS_PREVISION):
            lignes.append([gp["saison"], gp["manche"], gp["grand_prix_id"], gp["circuit_id"]] + l)
    ecrire_csv(OUT_OM / "previsions_week_ends_2024_2025.csv",
               ["saison", "manche", "grand_prix_id", "circuit_id", "heure_utc"] + VARS_PREVISION, lignes)


if __name__ == "__main__":
    journal(f"début ({'TEST' if TEST else 'complet'}) ; sorties dans {DONNEES}")
    for etape in (openf1, meteo_week_ends, climatologie, previsions_archivees):
        try:
            etape()
        except Exception as e:  # une source en échec ne bloque pas les autres
            journal(f"ÉCHEC {etape.__name__} : {type(e).__name__} : {e}")
    journal("fin")
