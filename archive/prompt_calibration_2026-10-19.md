# Calibration du jeu de stratégie : pipeline Python FastF1

Version consolidée du 19/10/2026 (intègre la vidéo Chain Bear, le document de sources et Heilmeier et al. 2020). Mise à jour : plateau réel.

## Contexte
Le dépôt contient un jeu de stratégie de course en TypeScript (voir CLAUDE.md et docs/prompt_jeu.md). Ce chantier ajoute un outil Python séparé, dans calibration/, qui extrait des données réelles de F1 et produit les paramètres du jeu : circuits, écuries et pilotes réels de la saison 2026, plus les cibles de calibration. Projet personnel, local, non diffusé : les exports contiennent les vrais noms.

Documents de référence (dossier docs/) : chainbear_strategie_f1_releve.md (concepts), sources_donnees_strategie_f1.md (sources, pièges, grandeurs à dériver), notes_vse_heilmeier_2020.md (article sur le Virtual Strategy Engineer). Signale tout conflit entre ce prompt et ces documents au lieu de trancher seul. Ne jamais inventer une valeur absente des sources : la signaler comme manquante.

Travaille par lots. Après chaque lot : tests verts, résumé, écarts par rapport à ce document, puis arrêt pour validation. Demande avant toute dépendance hors liste.

## Stack
- Python (version minimale exigée par la release FastF1 courante), fastf1, pandas, numpy, statsmodels, scikit-learn (regroupement uniquement), pyarrow, matplotlib, requests (Open-Meteo), pytest. sqlite3 de la bibliothèque standard pour la base externe. Projet géré par pyproject.toml.
- Code et identifiants en anglais, unités SI (s, m, kg).
- Caches FastF1 et Open-Meteo dans calibration/.cache/ et données externes dans calibration/inputs/external/ : dans .gitignore pour leur volume. Dans calibration/out/, seul le rapport est versionné (les fichiers parquet sont ignorés). calibration/export/ est versionné.

## Dépôt git
Même dépôt GitHub privé que le jeu ; règles de la section « Dépôt git » de docs/prompt_jeu.md (branche par lot calib/lot-NN-nom, pull request en fin de lot, fusion par moi uniquement, tag calib-lot-NN, aucun fichier de plus de 50 Mo).

## Entrées
- calibration/inputs/track_dna_2026.csv (séparateur ;) : caractéristiques et notes 1 à 5 par circuit 2026, source formula1dashboard.com. Anomalies connues : la ligne « Bahrain Grand Prix » porte le nom court « Kuala Lumpur » ; conditions vides pour Madring ; colonne downforce vide.
- calibration/inputs/race_review_tracks_2023_2026.csv (séparateur ;) : par circuit, moyennes d'interruptions (SC + VSC + drapeaux rouges), de changements de position et taux de pluie, GP 2023 à 2026, source f1-race-review.com. Leur « dépassement » compte tout changement de position.
- calibration/inputs/compound_allocations.csv, à constituer : saison ; manche ; GP ; dur ; medium ; tendre (désignations C1 à C5, ou C6 si une saison antérieure l'a utilisé) ; url_source. Une ligne par GP, chaque valeur tirée d'un communiqué Pirelli ou d'une source équivalente citée. Valeur introuvable : NA, jamais déduite.
- calibration/inputs/circuit_coords.csv, à constituer : circuit ; latitude ; longitude ; url_source.
- Fichier de correspondance des circuits à créer (nom d'événement et lieu FastF1 ↔ noms des CSV ↔ lieux de la base TUM). Signale les circuits sans correspondance au lieu de deviner.
- Externe, optionnel (lot 9) : base TUMFTM/f1-timing-database (SQLite, saisons 2014 à 2019) et fichiers de paramètres TUMFTM/race-simulation (racesim/input/parameters/*.ini, 121 courses 2014 à 2019), en lecture.

## Architecture
calibration/
  pyproject.toml
  cli.py              sous-commandes : ingest, fit, climate, external, report, export
  src/calib/
    ingest.py         chargement des courses via FastF1, cache parquet par course
    clean.py          filtrage des tours
    features.py       variables dérivées (âge pneu, écart à la voiture devant, statut piste, météo)
    fit_pace.py       rythme et dégradation
    fit_events.py     SC, VSC, drapeaux rouges, pluie, arrêts, perte au stand, dépassements, rythme sous neutralisation
    behaviour.py      cibles de comportement stratégique pour l'IA
    fit_field.py      dispersion des performances voitures et pilotes
    fit_entrants.py   attributs des écuries et pilotes 2026
    geometry.py       géométrie des circuits, voie des stands, micro-secteurs
    climate.py        climat par circuit via Open-Meteo
    external_tum.py   lecture de la base TUM 2014-2019 et des paramètres race-simulation
    shrink.py         lissage des grandeurs par circuit
    track_model.py    paramètres de circuit en fonction des notes Track DNA, archétypes
    report.py         rapport avec figures de contrôle
    export.py         paramètres pour le jeu
  tests/
  inputs/  out/  export/  .cache/

## Ingestion
- Courses uniquement (pas de sprints), saisons 2023 à 2026 jusqu'à la dernière course disponible. Saisons en paramètre CLI.
- Charger : tours, météo, statut de piste, messages de direction de course, résultats.
- Vérifie les noms de colonnes contre la version installée. Attendus : LapTime, LapNumber, Stint, Compound, TyreLife, FreshTyre, PitInTime, PitOutTime, TrackStatus, IsAccurate, Deleted, DeletedReason, Position, Time, LapStartTime. Liste les écarts.
- TrackStatus est une chaîne qui concatène les codes survenus pendant le tour : 1 piste libre, 2 jaune, 4 SC, 5 rouge, 6 VSC déployée, 7 fin de VSC annoncée (la fin réelle est le retour à 1), 3 jamais observé. Vérifie ce format sur la version installée. N'utilise pas le module fastf1.api (privé).
- Une course qui échoue au chargement est journalisée et sautée.
- Cache obligatoire, aucun rechargement si le parquet existe.

## Nettoyage : tours verts représentatifs
Exclure, avec un compteur par motif :
- tour 1, tours d'entrée et de sortie des stands ;
- tours non verts : un tour n'est conservé que si sa chaîne TrackStatus ne contient que le code 1 ; exclure aussi le tour de relance après SC ou VSC ;
- tours supprimés ou non précis ;
- gommes intermédiaire et pluie (traitées à part), tours avec précipitation ;
- tours en trafic : écart à la voiture devant sous un seuil au passage de la ligne (défaut 1,5 s, paramétrable) ;
- aberrants : au-delà de 107 % de la médiane du pilote sur la course.
Rapporter la part de tours conservés par course.

## Modèle de rythme
Par course, sur les tours verts secs :
lap_time = a_pilote + b_gomme + d_gomme * age + c_gomme * age² + g * tour + ε
- Âge du pneu = TyreLife (inclut les tours des séances précédentes), FreshTyre en covariable.
- a_pilote : effet fixe pilote (voiture + pilote).
- b, d, c : offset, dégradation linéaire (s/tour) et courbure par gomme. Courbure conservée seulement si significative, sinon 0.
- g : effet tour combinant allègement en carburant et évolution de la piste. Ne pas les séparer par régression (colinéaires). Décomposition paramétrique : effet carburant = k_fuel * conso_par_tour ; masse de départ 70 kg par défaut (ordre de grandeur donné par la vidéo Chain Bear, non vérifié contre le règlement technique 2026) ; k_fuel et conso en configuration, marqués hypothèses ; effet piste = g - effet carburant. Signaler un effet piste négatif.
- Régression robuste (Huber).
- Gommes : rôle du week-end (tendre, médium, dur) et désignation absolue via compound_allocations.csv.
- Ajustement groupé par ère : dégradation = d_C (par composé absolu) * s_circuit (sévérité, moyenne normalisée à 1), estimés ensemble sur toutes les courses de l'ère. Compare s_circuit aux notes Track DNA (abrasion, tyre_stress) et rapporte la corrélation.
- Sorties par course et par gomme : offset, pente, courbure, intervalles de confiance, nombre de tours, sigma résiduel global et par pilote.
- Agrégation par circuit et par ère : 2023 à 2025, et 2026 séparément.

## Falaise et relais
- Distribution de l'âge du pneu à l'arrêt par circuit et par gomme : médiane, quantiles 75 et 95 %, maximum.
- Seuil de falaise proposé = quantile 95 % (paramétrable), documenté comme borne basse (données censurées par les arrêts).

## Événements
- SC, VSC, drapeau rouge, séparément : nombre par course, tour de déclenchement, durée (en tours pour la SC, en secondes et en tours pour la VSC), transitions VSC vers SC.
- Cause de chaque neutralisation, classée à partir du texte des messages de direction de course : accident, débris, voiture arrêtée ou panne, météo, autre, indéterminé. Part de chaque cause.
- Rythme sous neutralisation : rapport temps au tour sous VSC et sous SC / médiane verte du pilote, par circuit et global. Comparer aux valeurs 140 % et 160 % de Heilmeier et al. 2020 (2014 à 2019).
- Pluie : part de courses avec précipitation, part de tours en intermédiaires ou pluie, tours de transition.
- Arrêts : nombre par pilote classé, séquences de gommes, tours d'arrêt en % de la course, part des arrêts sous SC ou VSC.
- Perte au stand par circuit : (tour d'entrée + tour de sortie) - 2 × médiane des tours verts du pilote dans les relais adjacents. Médiane et dispersion.
- Perte au stand par régime (vert, VSC, SC), à partir des arrêts effectués sous chaque régime. Si l'échantillon est insuffisant, rapports globaux VSC/vert et SC/vert.
- Dépassements en piste : changements de position entre deux tours consécutifs, hors tour 1, hors tours où l'un des deux pilotes s'arrête, hors SC, VSC et tour de relance. Fournir aussi le total de tous les changements de position, comparé à race_review_tracks_2023_2026.csv, avec le rapport entre les deux.

## Comportements stratégiques (cibles pour l'IA)
Mêmes grandeurs que Heilmeier et al. 2020 (tables 3, 17 et figure 5), recalculées sur 2023 à 2026 pour comparaison d'ère. Filtres : courses sèches, 1 à 3 arrêts, temps au tour < 200 s, durée d'arrêt < 50 s ; signaler séparément les arrêts après 90 % de course.
- Âge normalisé du pneu au changement (âge / nombre de tours de la course) par rôle de gomme.
- Part des arrêts faits au premier tour d'une neutralisation, et selon la progression de la course au déclenchement (seuil en dessous duquel une SC précoce ne déclenche pas d'arrêt).
- Comportement du leader et des poursuivants au premier tour de neutralisation.
- Réactions à l'undercut : part des cas où un pilote s'arrête au tour suivant l'arrêt de son poursuivant situé à moins de 1,5 s.
- Gomme au départ (part par rôle) et gomme choisie à chaque arrêt (part par rôle et par rang d'arrêt).
- Gain de temps des stratégies à n+1 arrêts par rapport à n arrêts, quand les deux sont observées sur une même course.

## Plateau
- Par course : écart de chaque a_pilote à la référence la plus rapide ; écarts entre écuries (moyenne des deux voitures) et entre coéquipiers.
- Sorties par ère : écart premier-dernier, écart-type entre écuries, écart-type entre coéquipiers.

## Écuries et pilotes 2026
- Entrants depuis les résultats FastF1 : nom, code, numéro, écurie, couleur d'écurie.
- Delta voiture par écurie et par GP : moyenne des a_pilote des deux voitures, lissée sur une fenêtre glissante des dernières courses (forme récente, taille paramétrable). Exporter aussi la série complète pour suivre le développement.
- Delta pilote : écart au coéquipier (a_pilote - moyenne de l'écurie), moyenné sur la saison, avec intervalle.
- Régularité : sigma résiduel par pilote.
- Gestion des pneus : écart entre la pente de dégradation du pilote et celle de son coéquipier, sur les mêmes gommes.
- Envol : places gagnées ou perdues au premier tour par rapport à la grille, hors incidents identifiés.
- Pluie : rythme relatif sur les tours en intermédiaires ou pluie, seulement si l'échantillon le permet ; sinon hypothèse marquée.
- Attaque et défense : dépassements en piste réussis et subis, rapportés à l'écart de rythme. Échantillon faible attendu : lisser vers la moyenne et marquer.
- Fiabilité et erreurs : abandons par cause (statut des résultats et messages de direction de course), par écurie pour les pannes, par pilote pour les accidents.
- Grilles : grille de départ réelle de chaque GP 2026 couru.

## Géométrie des circuits
- Tracé : polyligne issue des données de position (X, Y) d'un tour vert propre, rééchantillonnée et lissée. Longueur comparée à la longueur officielle de track_dna_2026.csv, écart rapporté.
- Voie des stands : trajet issu des positions d'une voiture sur un tour d'entrée et de sortie ; indices des micro-secteurs d'entrée et de sortie.
- Micro-secteurs : si FastF1 fournit les secteurs de commissaires dans les informations du circuit, les utiliser comme micro-secteurs ; sinon découpage régulier d'environ 20 segments. Vérifie la disponibilité sur la version installée.
- Type et poids des micro-secteurs depuis la vitesse sur le tour de référence (lent, moyen, rapide ; part du temps au tour).
- Probabilité d'incident par micro-secteur : drapeaux jaunes localisés dans les messages de direction de course quand ils citent un secteur, agrégés sur les saisons disponibles, lissés.
- Zones d'aide au dépassement : depuis la télémétrie (canal dédié s'il existe) ou le règlement 2026. Mécanisme 2026 à vérifier, ne rien supposer.
- Gommes nommées par GP 2026 depuis compound_allocations.csv.

## Climat (Open-Meteo, archive historique)
- Aux coordonnées de chaque circuit, séries horaires : rain, precipitation, wind_speed_10m, wind_direction_10m, temperature_2m (vérifie les noms exacts dans la doc). Modèle ECMWF IFS 9 km pour 2017 et après, ERA5 pour la profondeur historique ; rapporte les deux.
- Fenêtre : date du GP plus ou moins 7 jours, heure de course plus ou moins 2 heures, sur le plus d'années disponibles.
- Sorties par circuit : probabilité de pluie dans la fenêtre de course, distribution des intensités horaires, durée des épisodes de pluie, vent (vitesse, direction dominante), température.
- Comparaison avec l'indicateur Rainfall de FastF1 et les taux de race_review_tracks_2023_2026.csv ; rapporte le biais (hypothèse à tester : sous-estimation des averses courtes due à la maille).
- Requêtes groupées, mises en cache, aucune rafale en parallèle.
- Export : paramètres du générateur de cellules de pluie par circuit (taux de naissance, durée de vie, intensité, vent), avec l'archétype comme a priori si les données manquent.

## Données externes 2014 à 2019 (TUM)
- Base f1-timing-database : fréquence et durée des phases VSC et SC (table fcyphases), abandons par accident et par panne (table retirements), comportements stratégiques de la section précédente. Utilisées comme a priori d'une autre ère pour le lissage, jamais mélangées sans étiquette d'ère.
- Paramètres race-simulation (*.ini) : ordres de grandeur de dégradation et de perte au stand de 2014 à 2019, en comparaison avec l'ajustement 2023 à 2026. Lire le format sur les fichiers eux-mêmes, ne rien supposer.

## Lissage
Pour toute moyenne ou fréquence par circuit : (n × moyenne_circuit + k × moyenne_a_priori) / (n + k). A priori par défaut : moyenne globale de l'ère ; en option, valeur 2014 à 2019 du même circuit. Choisir k par validation croisée ou maximum de vraisemblance et le documenter.

## Modèle de circuit
- Joindre les paramètres par circuit (dégradation moyenne, sévérité s_circuit, perte au stand, dépassements, interruptions, effet piste) aux notes Track DNA.
- Régressions à 1 ou 2 variables explicatives (n ≈ 17) : par exemple s_circuit ~ abrasion + tyre_stress, dépassements ~ straights_level + drs. Rapporter R², coefficients, intervalles. Ne garder que ce qui est significatif, sinon la moyenne globale.
- Archétypes : 4 à 6 groupes de circuits (k-means ou équivalent sur notes + paramètres). Ils servent d'a priori pour les circuits peu documentés (une seule course, nouveau tracé).

## Rapport
calibration/out/report.html : attributs des écuries et pilotes avec leur provenance, tracés des circuits superposés à la longueur officielle, parts de tours conservés, courbes temps/âge par gomme pour 3 circuits contrastés, tableau des paramètres par circuit, distributions d'événements, comportements stratégiques comparés entre ères, climat, comparaison avec les CSV d'entrée, hypothèses et limites.

## Export vers le jeu
calibration/export/ :
- circuits/<circuit>.json : un fichier par circuit du calendrier 2026 (géométrie, micro-secteurs, voie des stands, zones d'aide au dépassement, abrasivité, sévérité, T_ref, perte au stand par régime, probabilités d'incident, gommes nommées, climat).
- teams.json et drivers.json : attributs des écuries et pilotes 2026, delta voiture par GP.
- grids.json : grilles de départ réelles des GP 2026 courus.
- compounds.json : offsets relatifs, pentes, courbures, seuils de falaise, par ère et par composé absolu.
- field.json : distributions des écarts voitures et pilotes, sigma de régularité.
- events.json : taux, durées et causes SC, VSC, rouge ; transitions VSC vers SC ; rythme sous neutralisation ; pluie ; dépassements en piste.
- behaviour.json : cibles de comportement stratégique de l'IA.
- weather.json : paramètres du générateur de cellules de pluie par circuit.
- targets.json : cibles de calibration du jeu avec intervalles (arrêts par voiture, dépassements en piste par course, interruptions par course, taux d'abandon, écart vainqueur-second), globales et par circuit.
- Chaque paramètre exporté est un objet { value, unit, method: "measured" | "derived" | "hypothesis", source, era, n, ci }. Aucun nombre nu.
- sources.md : liste des sources effectivement utilisées, pour la traçabilité.

## Tests
- Chaque filtre de nettoyage exclut les cas prévus (fixtures synthétiques).
- Modèle de rythme : sur données synthétiques générées avec des paramètres connus, les retrouver dans la tolérance.
- Ajustement groupé d_C × s_circuit : retrouver des valeurs connues sur données synthétiques.
- Lissage : n = 0 donne la moyenne a priori, n grand donne la moyenne du circuit.
- Géométrie : tracé fermé, longueur à moins de 2 % de la longueur officielle (seuil paramétrable), voie des stands raccordée au tracé aux bons micro-secteurs.
- Export : schémas respectés, provenance présente partout.

## Lots
1. Squelette, ingestion avec cache, correspondance des circuits, essai sur 3 courses.
2. Nettoyage et variables dérivées, rapport de conservation.
3. Rythme et dégradation (par course puis groupé), tests synthétiques.
4. Falaise, arrêts, perte au stand par régime, événements, dépassements, comportements stratégiques.
5. Plateau, écuries et pilotes 2026, grilles.
6. Géométrie des circuits.
7. Lissage, modèle de circuit, archétypes comme a priori.
8. Climat Open-Meteo et paramètres du générateur de pluie.
9. Données externes TUM 2014 à 2019 (optionnel).
10. Rapport et export.
