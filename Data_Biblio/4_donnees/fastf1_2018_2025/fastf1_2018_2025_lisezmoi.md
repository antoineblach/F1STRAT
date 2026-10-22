# Tours, messages, météo et circuits 2018 à 2025 (FastF1 via TracingInsights)

Version du 21/10/2026. Extraction 1 de la série « API ».

## Source

- Dépôts GitHub TracingInsights, un par saison (github.com/TracingInsights/2018 à 2025). Ce sont des exports des tables FastF1 (données officielles de chronométrage F1), séance par séance. Licence MIT ou Apache 2.0 selon le dépôt.
- Récupérés par git (seul accès réseau disponible depuis l'espace de travail : les API FastF1, Jolpica, OpenF1 et Open-Meteo sont bloquées par le proxy, sur le cloud comme sur ta machine).
- Séances extraites : qualification (Q) et course (R). Essais libres, sprints, télémétrie et radios non extraits.
- Manches et identifiants de circuit : rattachés à F1DB (`race.yml`) par le nom du GP, puis contrôlés. Seul alias : « Mexico City Grand Prix » (FastF1) = « Mexican Grand Prix » (F1DB).

## Fichiers

| Fichier | Contenu | Lignes |
| --- | --- | --- |
| calendrier_2018_2025.csv | saison, manche, date, nom FastF1 du GP, identifiants F1DB (GP, circuit, version du tracé), tours prévus, longueur, distance | 173 GP |
| tours_AAAA.csv (8 fichiers) | un tour par ligne, qualification et course | 23 651 à 34 196 par saison |
| messages_direction_course_2018_2025.csv | messages de la direction de course (drapeaux, SC, VSC, DRS, enquêtes, temps supprimés, risque de pluie) | 21 047 |
| meteo_seances_2018_2025.csv | météo de la station du circuit, une ligne par minute environ | 40 205 |
| circuits_seances_2018_2025.csv | par GP : circuit, rotation de la carte, pertes au stand estimées (vert, SC, VSC), source du tracé, nombre de virages | 173 |
| virages_circuits_2018_2025.csv | par GP et par virage : numéro, lettre, position X/Y, angle, distance depuis la ligne | 2 844 |
| circuits_json_2023_2025/ | fichier `corners.json` brut des 70 GP 2023 à 2025 : tracé (TrackX, TrackY), secteurs de commissaires, zones de vitesse (lent, moyen, rapide, ligne droite) | 70 fichiers |

## Colonnes de tours_AAAA.csv

saison ; manche ; gp ; seance (Q ou R) ; pilote (code à 3 lettres) ; numero ; ecurie ; tour ; temps_tour, s1, s2, s3 (s) ; gomme ; relais ; age_pneu (tours) ; pneu_neuf (1/0) ; position ; statut_piste (codes FastF1 concaténés sur le tour : 1 vert, 2 jaune, 4 SC, 5 rouge, 6 VSC, 7 fin de VSC) ; entree_stands, sortie_stands (heure de séance, s) ; debut_tour, fin_tour (heure de séance, s) ; debut_tour_utc ; tour_supprime, motif_suppression ; genere_fastf1 (tour reconstitué par FastF1) ; precis (indicateur IsAccurate de FastF1) ; vitesse_i1, vitesse_i2, vitesse_ligne, vitesse_piege (km/h) ; air_c, piste_c, humidite, pression_hpa, pluie (1/0), vent_dir, vent_ms (météo associée au tour).

Valeur vide = absente dans la source.

## Contrôles effectués

| Saison | GP | Tours de course | Temps manquant | Gomme inconnue | Âge du pneu manquant | Tours « précis » |
| --- | --- | --- | --- | --- | --- | --- |
| 2018 | 21 | 22 342 | 0,3 % | 1,7 % | 1,6 % | 82 % |
| 2019 | 21 | 23 676 | 0,1 % | 0,0 % | 0,0 % | 88 % |
| 2020 | 17 | 18 436 | 0,2 % | 0,0 % | 0,4 % | 83 % |
| 2021 | 22 | 23 758 | 0,3 % | 0,3 % | 0,0 % | 87 % |
| 2022 | 22 | 23 577 | 0,2 % | 1,4 % | 2,2 % | 83 % |
| 2023 | 22 | 24 422 | 0,1 % | 0,1 % | 0,1 % | 87 % |
| 2024 | 24 | 26 606 | 0,1 % | 0,0 % | 0,0 % | 89 % |
| 2025 | 24 | 26 692 | 0,1 % | 1,9 % | 2,0 % | 86 % |

Comparaison avec F1DB :
- Changements de relais (FastF1) et arrêts au stand (F1DB) : 5 873 contre 5 893 sur 173 GP. Écart de plus de 2 arrêts sur seulement 10 GP : 6 en 2018 (Australie, Chine, Bakou, France, Belgique, Italie), Miami 2025 (14 contre 18) et Canada 2025 (82 contre 33, numérotation des relais incohérente). Sur ces GP, recompter les arrêts depuis entree_stands et sortie_stands.
- Nombre de tours : identique au vainqueur F1DB sauf sur 4 GP où le classement est arrêté avant le dernier tour couru : Canada 2018 (70 contre 68), Japon 2019 (53 contre 52), Belgique 2021 (3 contre 1), Japon 2022 (29 contre 28). Conforme aux classements officiels (hypothèse non vérifiée sur les documents FIA : drapeau à damier anticipé ou classement à rebours).
- Nombre de pilotes : 7 GP avec un pilote de moins que F1DB, qui compte les non-partants.

## Points d'attention

1. **Gommes 2018** : noms absolus (HYPERSOFT, ULTRASOFT, SUPERSOFT, SOFT, MEDIUM, HARD), pas les rôles. Rôle à déduire par GP : les trois gommes sèches utilisées, de la plus dure à la plus tendre. À partir de 2019, la colonne donne le rôle (HARD, MEDIUM, SOFT).
2. **Gommes manquantes** concentrées : Miami 2025 (446 tours), Autriche 2022 (299), Belgique 2025 (57). À reconstituer depuis les relais, ou GP à exclure des modèles de pneus.
3. **Risque de pluie annoncé** : la direction de course publie « RISK OF RAIN FOR F1 RACE IS x % » avant presque chaque course depuis 2019 (21 à 24 courses par saison ; 7 sur 21 en 2018). C'est une prévision officielle archivée, à comparer à la pluie observée (colonne pluie) pour calibrer la prévision montrée au joueur.
4. **Incidents en qualification** (pour la règle du départ des stands) : drapeaux rouges, voitures arrêtées et temps supprimés figurent dans les messages de qualification.
5. **Pertes au stand de corners.json** (vert, SC, VSC) : estimations du dépôt, origine non documentée. Contrôle seulement : la calibration les mesure depuis entree_stands et sortie_stands.
6. **Zones de vitesse** absentes pour la Chine, le Japon et Las Vegas (listes vides dans corners.json).
7. **Tracé** : le dépôt prend le tracé MultiViewer le plus récent disponible pour le circuit (colonnes LayoutYear et LayoutLapSession) : il peut différer du tracé de l'année.

## Non couvert ici

- Durée d'immobilisation à l'arrêt : absente de FastF1. Source prévue : OpenF1 (2023 et après), bloquée par le proxy.
- 2014 à 2017 : prochaine extraction (base TUM).
