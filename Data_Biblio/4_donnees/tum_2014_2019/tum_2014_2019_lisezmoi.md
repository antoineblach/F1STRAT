# Base TUM 2014 à 2019 et paramètres de simulation

Version du 21/10/2026. Extraction 2 de la série « API ».

## Sources

- `F1_timingdata_2014_2019.sqlite` : dépôt github.com/TUMFTM/f1-timing-database, copie sans modification. Licence CC BY-NC-SA 3.0 (usage non commercial). Construite surtout à partir de l'API Ergast ; accidents et pannes par pilote et par saison repris de racefans.net.
- `tum_parametres_*.csv` et `tum_pars_mcs.ini` : dépôt github.com/TUMFTM/race-simulation (licence LGPL-3.0), dossier `racesim/input/parameters` : un fichier de paramètres par course (121), ajusté par TUM sur la course réelle (méthode : Heilmeier et al. 2020, voir `5_notes/notes_montecarlo_heilmeier_2020.md`). Les CSV en sont une mise à plat, sans recalcul.

## Base de chronométrage (SQLite)

| Table | Lignes | Contenu |
| --- | --- | --- |
| races | 121 | saison, date, lieu, gommes disponibles, tours courus et prévus, longueur, commentaire (28 courses commentées : pluie, drapeau rouge, SC, arrivée sous SC) |
| laps | 134 006 | un tour par pilote : temps, temps de course, écart au leader et à la voiture devant, gomme, âge du pneu, entrée aux stands, durée de l'arrêt, gomme suivante, part du tour sous VSC et SC |
| fcyphases | 136 | phases SC et VSC : début et fin en temps de course, en avancement du leader et en tours |
| starterfields | 2 479 | partants : écurie, motoriste, place de grille, statut, classement, tours effectués |
| qualifyings | 2 472 | temps Q1, Q2, Q3, vitesse au piège |
| retirements | 270 | accidents et pannes par pilote et par saison (vide quand le pilote n'a pas couru la saison) |
| drivers | 45 | numéro, initiales, nom |

Par saison :

| Saison | GP | Tours | Arrêts | Phases SC | Phases VSC |
| --- | --- | --- | --- | --- | --- |
| 2014 | 19 | 21 387 | 817 | 14 | 0 |
| 2015 | 19 | 20 226 | 740 | 14 | 7 |
| 2016 | 21 | 24 975 | 989 | 14 | 13 |
| 2017 | 20 | 20 707 | 694 | 15 | 6 |
| 2018 | 21 | 22 666 | 537 | 15 | 14 |
| 2019 | 21 | 24 045 | 653 | 16 | 8 |

Points d'attention (documentation du dépôt) :
1. Gommes en noms absolus A1 à A7, comparables d'une saison à l'autre : 2014 et 2015 A1 dur à A4 supertendre ; 2016 et 2017 A1 dur à A5 ultratendre ; 2018 A1 superdur à A7 hypertendre ; 2019 A2 = C1, A3 = C2, A4 = C3, A6 = C4, A7 = C5. I = intermédiaire, W = pluie. Le rôle (dur, médium, tendre) par GP se déduit de `races.availablecompounds`.
2. Âge du pneu des 10 premiers sur la grille fixé par convention à 2 tours (gomme de Q2), sauf départ en pluie ou intermédiaires.
3. Avancement des phases et des tours calculé en temps, pas en distance : 0,8 = 80 % du temps du tour.
4. `pitstopduration` : durée de l'arrêt au sens Ergast (passage dans la voie des stands), pas l'immobilisation.

## Contrôles effectués

- Arrêts : nombre identique à F1DB pour chaque saison (817, 740, 989, 694, 537, 653).
- Temps au tour 2018 et 2019 comparés aux tours FastF1 (`fastf1_2018_2025`) : 45 871 tours appariés, 99,9 % identiques à 0,01 s près, toutes les courses appariées.
- Phases SC et VSC 2018 et 2019 : 15 et 14, puis 16 et 8, contre 15 et 13, puis 17 et 9 messages de déploiement dans la direction de course FastF1. Écarts d'une unité, dus au mode de comptage (non vérifié course par course).
- Aucune gomme ni âge de pneu manquant.

## Paramètres de simulation (CSV)

| Fichier | Lignes | Contenu |
| --- | --- | --- |
| tum_parametres_courses_2014_2019.csv | 121 | par course : tours, distances minimales entre voitures, pertes en duel et pour le dépassé, DRS (fenêtre, tour d'activation, délai après SC), meilleur temps de qualif, écart rythme de course, sensibilité à la masse, perte au stand (entrée, sortie, sous VSC et sous SC), perte par place de grille et au premier tour, écart requis pour dépasser et sa correction par la vitesse, gain DRS, multiplicateurs de temps sous SC (1,6) et VSC (1,4), catégorie de contrainte pneus (1 forte à 3 faible), gommes, nombre de phases SC et VSC réelles |
| tum_parametres_ecuries_2014_2019.csv | 1 244 | par course et écurie : écart de performance de la voiture, carburant au départ (100, 105 ou 110 kg selon la saison) et consommation par tour (de l'ordre du carburant de départ divisé par le nombre de tours), multiplicateurs de consommation sous SC et VSC, temps d'arrêt additionnel de l'écurie |
| tum_parametres_pilotes_2014_2019.csv | 2 479 | par course et pilote : écart de performance du pilote, place de grille, vitesse maximale, consigne d'équipe, stratégie réelle et stratégie de base (JSON : tour d'arrêt, gomme, âge, carburant ajouté) |
| tum_parametres_pneus_2014_2019.csv | 6 583 | par course, pilote et gomme : modèle de dégradation retenu (linéaire sur toutes les lignes ; coefficients quadratiques aussi fournis), coefficients k, multiplicateurs de dégradation sous SC (0,25) et VSC (0,5), perte pneus froids (1,0 s) |
| tum_pars_mcs.ini | | paramètres Monte-Carlo : probabilités d'accident par pilote et de panne par écurie et par saison, lois du nombre, du début et de la durée des SC, VSC après panne, variabilité des arrêts par écurie (loi de Fisk), écart-type du temps au tour par pilote, performance au départ |

Points d'attention :
- Valeurs aberrantes sur les courses où la qualification ou la course était sous la pluie : `t_gap_racepace` de -15,8 à +18,9 s (Sepang, Shanghai, Spa et Suzuka 2014 ; Austin 2015 ; São Paulo 2016 ; Monza 2017). À exclure des a priori.
- Carburant de départ (100, 105 ou 110 kg), multiplicateurs SC et VSC (temps, consommation, dégradation), perte pneus froids (1,0 s), temps d'arrêt minimal (1,9 s) : valeurs fixes du modèle TUM, identiques sur toutes les courses, pas des mesures.
- Les paramètres sont ajustés pour reproduire la course avec le modèle TUM : ils ne sont transposables au jeu que si le modèle du jeu a la même forme.

## Usage prévu

- Tours 2014 à 2017 (absents de FastF1) : SC, VSC, abandons, arrêts et dégradation sur toute l'ère hybride.
- A priori et contrôles pour la calibration : pertes au stand, dégradation, écart requis pour dépasser, gain DRS, variabilité des arrêts.
