# Météo Open-Meteo : week-ends 2014 à 2025, climatologie, prévisions archivées

Version du 21/10/2026. Extraction lancée sur le PC (script `4_donnees/_extraction_api/extraction_api.py`), contrôlée le même jour.

## Source

- Open-Meteo (open-meteo.com), licence CC BY 4.0, usage gratuit non commercial.
- Coordonnées : position du circuit dans F1DB (un point par circuit). Dates : F1DB (`gp_2014_2025.csv`).
- Modèle : « best match » par défaut d'Open-Meteo (réanalyses ERA5 et ERA5-Land, modèle IFS à 9 km depuis 2017 pour l'archive ; modèles de prévision combinés pour les prévisions archivées). Le modèle effectivement retenu par point n'est pas renvoyé par l'API.
- Réponses brutes dans `brut_archive/`, `brut_climatologie/`, `brut_previsions/`.

## Fichiers

| Fichier | Contenu | Lignes |
| --- | --- | --- |
| meteo_week_ends_2014_2025.csv | 252 GP, horaire, heure UTC, du troisième jour avant la course (ou du jour des EL1 à partir de 2024) au jour de la course : précipitations, pluie, température, humidité, nébulosité, vent (vitesse en km/h, direction) | 23 040 |
| climatologie_gp_2005_2024.csv | pour chacun des 70 GP 2023 à 2025 : 20 années (2005 à 2024), 15 jours centrés sur le jour et le mois du GP, journalier en heure locale : cumul de précipitations, heures de précipitations, températures maximale et minimale ; `ecart_jours` = écart au jour du GP | 21 000 |
| previsions_week_ends_2024_2025.csv | 48 GP (à partir de janvier 2024), horaire UTC, du jour des EL1 au jour de la course : précipitations observées par le modèle (`precipitation`) et prévues 1 à 7 jours avant (`precipitation_previous_dayN`) ; température et prévisions 1 à 3 jours avant | 3 456 |

## Contrôles

- Aucune requête abandonnée ; deux coupures passagères, reprises automatiquement.
- Aucune valeur vide dans les trois fichiers.

## Limites

- Un point de grille par circuit : résolution de 9 à 25 km selon le modèle. Les averses localisées (Spa, Interlagos, Singapour) peuvent être manquées ou décalées. Contrôle prévu : la colonne `pluie` (station du circuit) des tours FastF1 2018 à 2025.
- `precipitation` des prévisions archivées est la sortie du modèle le plus récent, pas une observation. L'erreur de prévision se mesure par rapport à la station du circuit (FastF1) ou à l'archive, pas par rapport à cette colonne seule.
- Climatologie : 20 ans, fenêtre de 15 jours. Elle donne une fréquence de jours pluvieux autour de la date du GP, pas une probabilité de pluie pendant la course : pour celle-ci, croiser avec les heures de course.
- Prévisions archivées disponibles seulement depuis janvier 2024 : 48 week-ends.
- Autre prévision disponible : le message « RISK OF RAIN FOR F1 RACE IS x % » de la direction de course, 2019 à 2025 (dans `fastf1_2018_2025/messages_direction_course_2018_2025.csv`).
