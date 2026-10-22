# Pénalités de grille réelles : fréquence et places perdues (2014 à 2025)

Version du 21/10/2026. Objet : dimensionner les « jetons de pénalité » que le joueur devra dépenser pendant la saison. Données : `penalites_grille_2014_2025.csv` (493 événements, un par ligne).

## Source et méthode

- Source : F1DB (github.com/f1db/f1db, licence CC BY 4.0, attribution obligatoire), fichiers `starting-grid-positions.yml` (champ `gridPenalty`, départ des stands noté « PL »), `qualifying-results.yml` et `sprint-race-results.yml` de chaque course.
- Événement : un départ avec une pénalité de grille non vide ou un départ des stands. Plusieurs pénalités cumulées sur une même course comptent pour un événement (F1DB donne le total).
- Base : position en qualification ; résultat du sprint quand le sprint formait la grille (2021 et 2022, 10 événements). Base absente (pas de temps en qualification) : 45 événements sur 493, dont 6 en 2023 à 2025.
- Recul effectif = position de grille moins base. Départ des stands : position de grille = nombre de partants (dernier). Le recul peut être négatif quand des pilotes devant sont aussi pénalisés.
- Classes : 1 à 3 places, 4 à 6, 10, 15 et plus, fond de grille (« SFB » dans F1DB), voie des stands.
- Voitures-saison : nombre d'écuries × 2. Distribution par pilote : pilotes ayant pris au moins 10 départs dans la saison.
- 2026 exclu (saison incomplète, autre règlement moteur).

## Règles qui s'appliquent (règlement sportif 2023 à 2025, établi)

- Art. 28 : 4 ICE, MGU-H, TC, MGU-K, 2 ES et CE, 8 échappements par saison. Premier élément supplémentaire d'un type : 10 places ; suivants : 5 places ; cumul possible.
- Art. 18.2 : cinquième réprimande (dont au moins 4 pour conduite) : 10 places. Une pénalité de 10 places n'est donc pas toujours une pénalité moteur.
- Art. 54.3 g : les commissaires peuvent infliger un recul d'un nombre quelconque de places à la course suivante.
- Art. 40.9 : toute modification de pièce ou de réglage de suspension sous parc fermé : départ des stands.
- Art. 42.3, procédure de formation de la grille : position temporaire = qualification + somme des pénalités ; les non-pénalisés remplissent les places libres ; les pénalisés remontent ensuite combler les trous. Plus de 15 places cumulées : derrière tous les classés. En 2023 et 2024, l'alinéa vise aussi les pilotes « pénalisés pour partir au fond de la grille » ; cette mention disparaît en 2025, et F1DB ne compte aucun fond de grille en 2025.
- Conséquence de 42.3 : le recul effectif est plafonné par la taille de la grille. Un recul de 10 places après une qualification en 15e position coûte environ 5 places.

## Période jouée : 2023 à 2025

110 événements, 70 courses, 60 voitures-saison : **1,83 événement par voiture et par saison**, 1,57 par course.

| Classe | Événements | Part | Par voiture et par saison | Recul effectif moyen | Médian | 1er à 3e quartile | Max | Qualif médiane |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 à 3 places | 26 | 24 % | 0,43 | 2,2 | 3 | 2 à 3 | 3 | 8 |
| 4 à 6 places | 14 | 13 % | 0,23 | 2,7 | 4 | 0 à 5 | 6 | 15 |
| 10 places | 8 | 7 % | 0,13 | 7,9 | 10 | 6 à 10 | 10 | 8 |
| 15 places et plus | 0 | 0 % | 0 | | | | | |
| Fond de grille | 7 | 6 % | 0,12 | 2,0 | 2 | 0 à 4 | 7 | 18 |
| Voie des stands | 55 | 50 % | 0,92 | 2,4 | 1 | 0 à 4 | 14 | 19 |

Valeurs brutes de F1DB en 2023 à 2025 : 3 places (22), 5 (12), 10 (8), fond de grille (7), 1 (4), 2 (3), 4 (1), 6 (1), voie des stands (55).

Nombre d'événements par pilote et par saison (60 pilotes-saison) :

| 0 | 1 | 2 | 3 | 4 et plus | Moyenne |
| --- | --- | --- | --- | --- | --- |
| 10 (17 %) | 21 (35 %) | 11 (18 %) | 11 (18 %) | 7 (12 %) | 1,78 |

Places effectivement perdues sur la saison, par pilote (reculs négatifs ramenés à 0) : moyenne 4,7 ; médiane 3 ; 3e quartile 8 ; 9e décile 13 ; maximum 16.

Par écurie et par saison (deux voitures) : moyenne 3,7 événements, médiane 3, de 0 (McLaren 2023 et 2025) à 8 (Haas 2023, Sauber 2024, Red Bull 2025).

Départs des stands 2023 à 2025 : sur les 50 dont la qualification est connue, 42 suivent une qualification en 16e position ou au-delà, 2 seulement une qualification dans les 10 premiers.

Plus gros reculs effectifs 2023 à 2025 : Hamilton, Bakou 2024, voie des stands depuis la 7e place (13 places) ; Russell, Austin 2024, voie des stands depuis la 6e (14) ; 10 places depuis les premières positions : Leclerc, Djeddah 2023 (depuis la 2e) ; Sainz, Las Vegas 2023 (2e) ; Verstappen, Spa 2024 (1re) ; Bearman, Silverstone 2025 (8e).

## Par saison (2014 à 2025)

| Saison | Courses | Voitures | Événements | Par voiture | 1 à 3 | 4 à 6 | 10 | 15+ | Fond | Stands | Recul effectif par voiture | Places chiffrées par voiture |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2014 | 19 | 22 | 38 | 1,73 | 3 | 13 | 8 | 3 | 0 | 11 | 5,7 | 8,5 |
| 2015 | 19 | 20 | 43 | 2,15 | 6 | 10 | 7 | 17 | 0 | 3 | 6,7 | 34,4 |
| 2016 | 21 | 22 | 46 | 2,09 | 11 | 20 | 1 | 6 | 0 | 8 | 5,2 | 17,0 |
| 2017 | 20 | 20 | 62 | 3,10 | 6 | 21 | 6 | 27 | 0 | 2 | 9,1 | 43,1 |
| 2018 | 21 | 20 | 45 | 2,25 | 7 | 11 | 2 | 20 | 0 | 5 | 6,6 | 35,7 |
| 2019 | 21 | 20 | 52 | 2,60 | 9 | 15 | 3 | 2 | 18 | 5 | 7,5 | 8,1 |
| 2020 | 17 | 20 | 20 | 1,00 | 7 | 6 | 0 | 0 | 6 | 1 | 2,7 | 2,5 |
| 2021 | 22 | 20 | 38 | 1,90 | 7 | 11 | 1 | 1 | 15 | 3 | 7,7 | 5,0 |
| 2022 | 22 | 20 | 39 | 1,95 | 3 | 8 | 2 | 3 | 17 | 6 | 10,4 | 5,7 |
| 2023 | 22 | 20 | 35 | 1,75 | 10 | 3 | 3 | 0 | 3 | 16 | 5,2 | 3,6 |
| 2024 | 24 | 20 | 37 | 1,85 | 9 | 6 | 2 | 0 | 4 | 16 | 4,7 | 3,8 |
| 2025 | 24 | 20 | 38 | 1,90 | 7 | 5 | 3 | 0 | 0 | 23 | 4,4 | 3,5 |

« Places chiffrées » : somme des pénalités numériques (hors fond de grille et voie des stands). De 2015 à 2018, 34 à 43 places chiffrées par voiture et par saison pour 5 à 9 places réellement perdues : l'écart vient du plafonnement de 42.3.

Périodes groupées :
- 2014 à 2021 : 344 événements, 2,10 par voiture et par saison ; pilotes à 0/1/2/3/4+ événements : 21/48/40/32/23 sur 164.
- 2022 à 2025 : 149 événements, 1,86 par voiture et par saison ; 1 à 3 : 29 ; 4 à 6 : 22 ; 10 : 10 (recul effectif médian 10, qualif médiane 4) ; 15+ : 3 ; fond de grille : 24 (recul moyen 5,7) ; voie des stands : 61 (recul moyen 2,7) ; pilotes 13/25/17/17/8 sur 80.

## Où et quand (grosses pénalités : 10 places et plus, fond de grille, voie des stands)

- Par GP, 2022 à 2025, rapporté au nombre d'éditions : Spa 3,8 par course ; Monza 2,2 ; Austin 2,0 ; Montréal 1,8 ; Barcelone, Bakou, Melbourne 1,2 ; Singapour 1,0. Les moins touchés : Bahreïn 0 ; Djeddah, Monaco, Miami, Abu Dhabi 0,2.
- Par GP, 2014 à 2025 : Spa 2,8 ; Monza 2,7 ; Austin 2,1 ; Sotchi 2,0 ; Mexico 1,8.
- Par quart de saison, 2022 à 2025 (98 événements) : 12, 23, 39, 24. Pic au troisième quart.

## Établi et hypothèses

Établi par les données :
1. Environ 1,8 événement par voiture et par saison en 2023 à 2025, stable de 2022 à 2025 (1,75 à 1,95).
2. La moitié sont des départs des stands, presque toujours après une qualification en fond de grille.
3. Les pénalités de 10 places touchent des voitures qualifiées vers la 8e place et coûtent réellement environ 10 places ; les fonds de grille et départs des stands coûtent 1 à 2 places en médiane.
4. Les grosses pénalités se concentrent à Spa, Monza et Austin, et dans le troisième quart de saison.

Établi par le règlement : une valeur de 1 à 3 places ne peut pas venir de l'art. 28 (10 ou 5 places). Les 26 événements de cette classe en 2023 à 2025 sont donc sportifs, à condition que F1DB enregistre la valeur nominale.

Hypothèses (cohérentes avec les données, non démontrées par elles) :
- Les équipes choisissent de prendre leurs pénalités moteur quand elles coûtent le moins : après une mauvaise qualification, sur un circuit où l'on double (Spa, Monza, Austin), quand les éléments s'épuisent en fin d'été. Les données montrent la coïncidence, pas la décision. Une partie des départs des stands sont la conséquence d'un accident en qualification (voiture reconstruite sous parc fermé), pas un choix.
- Les 7 valeurs de 1 et 2 places de 2023 à 2025 (São Paulo 2023 : Russell, Ocon, Gasly ; Bahreïn 2025 : Russell, Antonelli ; Qatar 2024 : Verstappen ; Imola 2025 : Colapinto) : nature non vérifiée. Ce peut être des sanctions sportives réelles ou des reculs liés à des temps annulés. Impact faible (recul moyen 1,3).

## Limites

- Aucune cause dans F1DB. Les messages de direction de course 2023 à 2025 (dépôt TracingInsights, `rcm.json`) ne contiennent aucune pénalité de grille (vérifié). La cause figure dans les décisions des commissaires (documents FIA), non extraites.
- La taille ne donne pas la cause : 5 et 10 places peuvent être sportives (art. 18.2, 54.3 g) ou moteur (art. 28).
- Départ des stands compté comme dernière place, même quand plusieurs voitures partent des stands.
- Base absente pour 9 % des événements (pas de temps en qualification) : ils comptent dans les fréquences, pas dans les reculs.

## Jetons de pénalité : décision du 21/10/2026

Décidé :
- Deux jetons par voiture et par saison, IA comprise : un « +5 » et un « +10 ».
- Dépense libre, à n'importe quel GP de la saison, avant la course.
- Départ des stands aléatoire, à faible probabilité.
- Jeton déclaré avant la qualification, par le joueur comme par l'IA.
- La qualification simulée produit des incidents (sortie, panne, voiture à réparer) ; le départ des stands se déclenche sur un incident, pas au hasard pur.

Règles d'application (proposées, défauts à valider) :
1. Application par la procédure 42.3 : position temporaire = qualification + jetons dépensés, puis remontée pour combler les places libres. Les deux jetons au même GP font +15 : pas de fond de grille, que 42.3 d réserve aux cumuls de plus de 15.
2. Jetons rattachés à la voiture : un pilote remplaçant hérite des jetons restants, comme pour le décompte des éléments moteur (art. 28.4).
3. Jeton non dépensé avant le dernier GP : appliqué d'office au dernier GP.
4. Départ des stands aléatoire : p = 0,6 % par voiture et par course (paramètre). Référence 2023 à 2025 : départs des stands après une qualification dans les 15 premiers, 8 sur 1 398 départs (0,57 %), soit 0,13 par voiture et par saison, environ 3 par saison sur toute la grille. Tous départs des stands confondus : 3,9 % (0,92 par voiture et par saison), mais 42 sur 50 suivent une qualification en fond de grille, donc surtout choisis ou consécutifs à un accident. Option : si la qualification simulée tire des accidents, conditionner le départ des stands à un accident plutôt que tirer à plat.
5. Départ des stands et jeton dépensé au même GP : le jeton est consommé sans effet supplémentaire (hypothèse : un départ des stands rend la pénalité de grille sans objet).
6. IA, au même moment de décision que le joueur, pour chaque jeton restant :
   - coût attendu = places perdues selon 42.3, depuis la position de qualification attendue (rythme de la voiture), × valeur d'une place sur ce circuit (difficulté à dépasser, issue des dépassements par circuit de la calibration) ;
   - dépense si le coût attendu est sous un seuil qui monte quand le nombre de GP restants baisse ; seuil fixé par le profil (prudent, neutre, agressif) ; dépense forcée au dernier GP.
7. Contrôles de réalisme sur des saisons simulées :
   - répartition des dépenses de l'IA par circuit et par quart de saison, à comparer au réel (Spa, Monza, Austin en tête ; pic au troisième quart) ;
   - places effectivement perdues par voiture et par saison, à comparer à 4,7 (réel 2023 à 2025, toutes causes confondues, départs des stands compris).

Écart assumé avec le réel : 15 places nominales par voiture et par saison, contre 3,5 à 3,8 places chiffrées en 2023 à 2025 ; 20 pénalités de 10 places par saison sur la grille, contre 2 à 3. Le coût effectif dépendra du moment de dépense.

Point ouvert : moment de la décision.
- Avant la qualification (recommandé) : conforme au réel, où les éléments sont montés avant la qualification ; un changement après la qualification se fait sous parc fermé et impose le départ des stands (art. 40.9). Le joueur parie sur sa qualification, ce qui donne un coût aux jetons. Dans les données, les 10 places ont coûté 10 places en médiane (qualification médiane : 8e) ; ils sont en général connus avant la qualification (hypothèse, cause non vérifiée).
- Après la qualification : le joueur dépense quand il est déjà en fond de grille. Dans les données, fonds de grille et départs des stands, pris surtout dans ce cas, coûtent 1 à 2 places en médiane : les jetons deviennent presque gratuits.
