# OpenF1 2023 à 2025 : arrêts et dépassements

Version du 21/10/2026. Extraction lancée sur le PC (script `4_donnees/_extraction_api/extraction_api.py`), contrôlée le même jour.

## Source

- api.openf1.org, endpoints `sessions` (session_name = Race), `pit` et `overtakes` ; historique gratuit, sans authentification. Réponses brutes dans `brut/`.
- Définitions (documentation OpenF1, consultée le 21/10/2026) :
  - `lane_duration` : temps passé dans la voie des stands (s) ; `pit_duration` : même valeur, champ déprécié ;
  - `stop_duration` : temps d'immobilisation (s), « disponible seulement à partir du GP des États-Unis 2024 » ;
  - `overtakes` : « disponible seulement en course, peut être incomplet » ; `position` = place du dépasseur après le dépassement.

## Fichiers

| Fichier | Contenu | Lignes |
| --- | --- | --- |
| sessions_course_2023_2025.csv | 70 courses : clés OpenF1, date, lieu, décalage horaire | 70 |
| arrets_2023_2025.csv | un passage dans la voie des stands par ligne : course (_annee, _lieu, _date_course), pilote (numéro), tour, lane_duration, stop_duration | 2 339 |
| depassements_2023_2025.csv | un changement de place par ligne : dépasseur, dépassé, heure, place après | 17 589 |

## Contrôles

- Arrêts : aucune donnée pour les 6 premières courses de 2023 (Bahreïn à Monaco). 64 courses couvertes.
- Comparaison avec F1DB, course par course : nombre d'entrées identique sur 63 courses sur 64. Exception : Canada 2025, 82 entrées contre 33 dans F1DB. FastF1 donne aussi 82 changements de relais sur ce GP : doublons probables dans le flux officiel, à dédoublonner.
- Immobilisation : 851 arrêts, du GP des États-Unis 2024 à Abu Dhabi 2025. Médiane 2,9 s en 2024 (fin de saison), 2,7 s en 2025 ; minimum 1,8 s ; maximum 38,3 s (arrêts avec réparation ou pénalité). Couverture incomplète sur certaines courses : São Paulo 2024 (12 sur 35), Qatar 2024 (27 sur 60), Melbourne 2025 (34 sur 82), Silverstone 2025 (28 sur 35).
- Temps dans la voie des stands : médiane 23,1 à 23,7 s selon la saison. 110 entrées dépassent 60 s : 103 sur six courses interrompues par un drapeau rouge (Zandvoort, Mexico et São Paulo 2023 ; Suzuka, Monaco et São Paulo 2024), voitures rentrées dans la voie pendant l'interruption ; 7 arrêts longs isolés (réparations, hypothèse). À exclure du calcul de la perte au stand.
- Dépassements : 47 à 642 par course, médiane 236. Ce sont des changements de place bruts : départ, cycles d'arrêts, neutralisations et doublements y figurent. À filtrer avant toute calibration des dépassements en piste (par exemple : hors premier tour, hors tours d'entrée et de sortie des stands des deux voitures, hors SC et VSC, à recouper avec les positions par tour de FastF1).

## Usage prévu

- Temps d'immobilisation : loi par écurie et par saison sur fin 2024 et 2025 (seul échantillon disponible) ; pour 2023 et début 2024, temps dans la voie seulement, l'immobilisation étant imputée.
- Perte au stand : temps dans la voie des stands, à compléter par FastF1 (entrées et sorties des stands) pour les 6 courses manquantes de 2023.
- Dépassements : contrôle du modèle de dépassement, après filtrage.
