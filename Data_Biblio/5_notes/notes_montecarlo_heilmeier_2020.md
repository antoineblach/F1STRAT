# Monte-Carlo dans la simulation de course (Heilmeier et al., 2020) : notes pour le projet

Article : Heilmeier, Graf, Betz, Lienkamp, « Application of Monte Carlo Methods to Consider Probabilistic Effects in a Race Simulation for Circuit Motorsport », Applied Sciences 10(12) 4229, 2020, DOI 10.3390/app10124229. Licence CC BY 4.0 (p. 21 ; le brief de la mission indiquait CC BY 3.0). Lu en entier le 20/10/2026 (PDF v3, 21 p., fourni par Antoine). Les numéros de page renvoient au PDF.

Code : TUMFTM/race-simulation, licence LGPL-3.0, dernier commit le 18/09/2021, lu le 20/10/2026.

Mentions : « (code) » = valeur lue dans le dépôt ; « (déduit) » = calcul de ma part à partir des valeurs publiées ; « (estimé) » = lecture sur un graphique.

## Code et données (établi)
- Le code est publié : toute la simulation, Monte-Carlo compris, est dans TUMFTM/race-simulation (p. 18 ; README du dépôt). Tirage des événements : racesim/src/_race_montecarlo.py ; tours, neutralisations et dépassements : race.py ; durée d'immobilisation : car.py.
- Tous les paramètres probabilistes sont dans racesim/input/parameters/pars_mcs.ini : par saison de 2014 à 2019, probabilité d'accident par pilote et de panne par écurie ; pour l'ensemble des saisons, lois des SC et des VSC, lois log-logistiques par écurie, écart-type du temps au tour et performance d'envol par pilote (code).
- Les valeurs du code coïncident avec les tableaux 4, 5, A1, A3 et A4, et avec le tableau A2 sauf deux écuries (voir « Écarts »).
- Données : base f1-timing-database 2014 à 2019 (p. 3). Pertes au stand sous neutralisation et départs mesurés sur les vidéos embarquées F1 TV de 2018 et 2019 (p. 8 et 14).

## Modèle de temps au tour (p. 2)
Même structure que dans l'article sur le VSE : t_lap = t_base + t_tire + t_fuel + t_car + t_driver + t_grid + t_pit. Simulation tour par tour ; dépassements testés sur les temps cumulés en fin de tour.

## Valeurs établies (ère 2014 à 2019)

### Safety car
- Nombre de SC par course (tableau A3, p. 20 ; figure 7, p. 11) : 0 : 0,455 ; 1 : 0,413 ; 2 : 0,099 ; 3 ou plus : 0,033. Le code plafonne à 3.
- Début de la SC (tableau A4, p. 20) : premier tour 0,364 ; du 2e tour à 20 % de la course 0,136 ; 20 à 40 % 0,136 ; 40 à 60 % 0,08 ; 60 à 80 % 0,193 ; 80 à 100 % 0,091. La probabilité d'une tranche est répartie également entre ses tours, puis l'instant est tiré uniformément dans le tour, U(0, 1) (p. 11). Plus de 36 % des phases de SC commencent au premier tour (p. 11) : c'est une part des SC, pas des courses.
- Durée de la SC en tours (tableau 4, p. 11) : 2 : 0,182 ; 3 : 0,25 ; 4 : 0,227 ; 5 : 0,193 ; 6 : 0,057 ; 7 : 0,068 ; 8 : 0,023. Espérance 3,99 tours (déduit).
- Espérances (déduit) : 0,71 SC par course ; au moins une SC dans 54,5 % des courses ; environ 0,26 SC au premier tour par course (0,71 × 0,364, en négligeant les tirages rejetés pour chevauchement).
- Rythme : environ 1,6 × t_lap,min sous SC et 1,4 × t_lap,min sous VSC (p. 6, figure 4). Tours retenus pour ce calcul : pour la SC, tours où elle est en piste depuis plus de 1,5 tour et qui ne sont pas le dernier de la phase ; pour la VSC, tours qu'elle couvre entièrement ; pilotes P1 à P3 ; moyenne sur 2014 à 2019 (p. 6).
- Derrière la SC : usure et consommation à 25 % (estimation des auteurs, p. 13) ; écart minimal entre voitures 0,8 s (code, min_t_dist_sc) ; DRS désactivé pendant deux tours après la SC (p. 13 ; code, drs_sc_delay = 2).
- Modélisation : « voiture de sécurité fantôme » propre à chaque pilote, pour contourner la discrétisation par tour ; son premier tour est ralenti pour simuler l'attente du leader à la sortie des stands (p. 13 et 14, figure 9). Validation sur le GP de Chine 2018 (figure 10, p. 15).

### VSC
- Causée uniquement par les pannes : P(VSC sachant panne) = n_vsc / n_pannes = 0,227 sur 2015 à 2019 (éq. 15, p. 12).
- Instant de la panne, et de la VSC éventuelle : uniforme sur la course, U(0, n_tours) (p. 12).
- Durée (tableau 5, p. 12) : 1 tour : 0,479 ; 2 : 0,396 ; 3 : 0,021 ; 4 : 0,104 ; plus U(0, 1). Espérance avant l'ajout uniforme : 1,75 tour (déduit).
- Pendant la VSC : usure et consommation à 50 % (estimation des auteurs, p. 13) ; dépassement interdit si la VSC couvre au moins la moitié du tour (p. 13).
- Validation (tableau 7, p. 17), part des courses avec 0, 1, 2 ou 3 phases. VSC réel : 0,637 / 0,294 / 0,040 / 0,029 ; simulé : 0,618 / 0,304 / 0,067 / 0,011. SC réel : 0,455 / 0,413 / 0,099 / 0,033 ; simulé : 0,462 / 0,416 / 0,091 / 0,031.

### Accidents et pannes
- Chaque SC est causée par l'accident d'un seul pilote, tiré au sort avec des poids proportionnels aux p_accident (p. 12 ; code). Les accidents n'existent donc qu'avec une SC. Les pannes sont des tirages indépendants par voiture (code).
- Inférence Beta-Bernoulli (p. 9 et 10) :
  - a priori Beta(α̂, β̂) par la méthode des moments (éq. 11 et 12), à partir de la fraction d'accidents par pilote et de pannes par écurie, sur les pilotes et écuries ayant au moins 30 courses dans la base ;
  - a posteriori Beta(α + z, β + N − z) par pilote ou écurie et par saison ;
  - valeur utilisée : la moyenne a posteriori.
- L'accident dépend du pilote, la panne de la voiture donc de l'écurie (p. 9).
- Hyperparamètres α̂ et β̂ : non publiés (manquant). Mode de l'a priori d'accident vers 5 % (estimé, figure 6, p. 9).
- Probabilités par course :
  - accidents : de 0,045 à 0,072 par pilote en 2019 (tableau A1) ; de 0,045 à 0,114 sur 2014 à 2019 (code) ;
  - pannes : de 0,041 (Mercedes) à 0,117 (McLaren) en 2019 (tableau A2) ; de 0,041 à 0,225 sur 2014 à 2019 (code).
- Voitures endommagées : non modélisées faute de données (p. 8). Dans la littérature, Salminen prend 1 % de dégâts par dépassement pour chaque voiture et 1 % pour les deux, une perte U(2 s, 60 s) et un arrêt immédiat (p. 6). L'origine de ces valeurs n'est pas donnée.

### Variabilité du temps au tour
- Bruit gaussien N(0, σ²) propre à chaque pilote (éq. 6, p. 5).
- Méthode (p. 4) : polynôme du second degré ajusté par relais, écarts au polynôme ; exclure les deux premiers tours, les tours d'arrêt et les tours de neutralisation.
- σ de 0,458 à 0,841 s pour les pilotes 2019 (tableau A1) ; de 0,458 à 0,855 s sur 2014 à 2019, et 0,625 s pour un pilote inconnu (code). Ces valeurs valent pour toutes les saisons (tableau A1).

### Durée d'immobilisation
- Loi log-logistique (Fisk) par écurie, paramètres (forme, position, échelle) au sens de scipy.stats.fisk (éq. 7, p. 5 ; tableau A2, p. 20).
- Ajustée sur l'écart à l'arrêt le plus court de la course, en ne gardant que les arrêts au plus 4 s au-dessus de ce minimum (tableau A2).
- Exemples 2019 (tableau A2) : Mercedes (1,563 ; −0,046 ; 0,480) ; Ferrari (2,414 ; −0,153 ; 0,737) ; Alfa Romeo (5,827 ; −0,953 ; 2,327).
- Code : immobilisation = 1,9 s, minimum identique dans les 121 fichiers, plus le tirage Fisk, retiré tant qu'il dépasse 3 fois la moyenne de la loi (car.py).
- Justification : distribution asymétrique ; Mercedes concentrée près du minimum, Force India plus étalée (figure 3, p. 5).

### Départ
- Courbe de référence de l'envol moyen (éq. 10, p. 8) : t_s = √(2 (p_g − p_s) / a_avg) + t_r, temps entre le départ et le franchissement de la ligne selon la place de grille p_g.
- Paramètres (p. 8) : p_s = 0,8 ; t_r = 0,2 s ; a_avg = 11,2 m/s², ajusté sur 2019 avec 8 m entre deux places. Mesures sur les vidéos embarquées F1 TV 2019 (figure 5).
- Performance d'envol du pilote : écart à cette courbe, modélisé par N(μ, σ²) et ajouté au temps du premier tour (p. 8 et 9).
  - Tableau A1 : μ de −0,097 à +0,102 s, σ de 0,098 à 0,245 s.
  - Pilote inconnu : μ = 0, σ = 0,146 s (code).
- Le code n'utilise pas la courbe pendant la course. Premier tour = t_loss_firstlap + (p_g − 1) × t_loss_pergridpos + N(μ, σ²) (race.py).
  - Sur les 121 courses (code) : t_loss_firstlap de 0,43 à 8,22 s (médiane 3,82 s) ; t_loss_pergridpos de 0,113 à 0,188 s par place (médiane 0,139 s).
- Les auteurs critiquent l'approche par places gagnées ou perdues : elle fausse les probabilités, car les pilotes de tête ont peu de places à gagner (p. 4 ; exemple 2018 : Hamilton −0,8 place en moyenne, Stroll +1,9).

### Perte au stand sous neutralisation
- Le facteur 0,5 de la littérature (Salminen, éq. 9, p. 7) est rejeté : la perte sous neutralisation dépend fortement du tracé (p. 7) et doit être paramétrée par circuit.
- Mesures sur vidéos embarquées 2018 et 2019 (tableau 6, p. 14), perte de roulage dans la voie, hors immobilisation, en secondes :

| Circuit | Vert | VSC | SC |
| --- | --- | --- | --- |
| Catalunya | 19,04 | 10,03 | 7,88 |
| Melbourne | 17,85 | 12,95 | 12,61 |
| Monza | 20,60 | 15,42 | 10,16 |
| Suzuka | 19,48 | 15,05 | 13,60 |

- Sous SC, la perte est souvent même plus faible que sous VSC (p. 14). Pour les circuits sans VSC ni SC en 2018 et 2019, les auteurs reprennent les valeurs de circuits similaires (p. 14).
- Ces quatre lignes se retrouvent dans les fichiers de paramètres 2018 et 2019 (somme tour d'entrée + tour de sortie ; Monza VSC 15,41 dans le code).
- Sur les 121 courses, hors immobilisation (code) :
  - vert : 14,1 à 24,6 s (médiane 18,3 s) ;
  - rapport VSC sur vert : 0,29 à 0,77 (médiane 0,60) ;
  - rapport SC sur vert : 0,18 à 0,88 (médiane 0,54) ;
  - une partie de ces valeurs sont des substituts de circuits similaires (p. 14).
- La perte est répartie entre tour d'entrée et tour de sortie. Le tour d'entrée peut avoir une perte négative sous neutralisation (code ; Spielberg 2019 : −0,937 s sous VSC).

### Autres paramètres du code (121 courses 2014 à 2019, code)
- Carburant : masse au départ 100, 105 ou 110 kg ; consommation 1,28 à 2,5 kg par tour ; sensibilité du temps au tour à la masse 0,017 à 0,045 s/kg (médiane 0,031).
- Pneus froids : +1,0 s au premier tour de chaque relais (t_add_coldtires, valeur unique).
- Usure sous neutralisation : 0,5 sous VSC, 0,25 sous SC (valeurs uniques).
- Dégradation : modèle linéaire dans les 121 fichiers. Le modèle de dépassement est décrit dans veille_biblio_strategie.md, section ITSC 2018.

## Écarts entre l'article et le code
- Tableau A2 contre pars_mcs.ini :
  - Red Bull : (2,045 ; −0,094 ; 0,598) dans l'article, (2,012 ; −0,091 ; 0,577) dans le code ;
  - Toro Rosso : (4,290 ; −0,568 ; 1,606) dans l'article, (4,094 ; −0,459 ; 1,513) dans le code ;
  - les autres écuries coïncident. Cause non documentée.
- Licence : CC BY 4.0 dans le PDF (p. 21), contre CC BY 3.0 dans le brief.

## Résultats et discussion (p. 14 à 18)
- Calcul : 90 à 110 ms par course à 20 voitures en Python, pré-simulation comprise ; 10 000 courses en 250 à 300 s sur 4 cœurs (p. 14).
- Convergence, position moyenne de Hamilton avec intervalle à 95 % (tableau 8, p. 17) : 100 courses ± 0,309 ; 1 000 ± 0,082 ; 10 000 ± 0,029 ; 100 000 ± 0,011. 10 000 courses jugées un bon compromis.
- Le résultat déterministe n'est souvent pas l'issue la plus probable. Exemple : Verstappen, 5e en déterministe, finit le plus souvent 4e (figure 11, p. 16).
- La stratégie théoriquement la plus rapide est souvent fragile une fois les effets aléatoires pris en compte (p. 18).
- Limites reconnues (p. 18) : les retardataires ne peuvent pas se dédoubler en fin de SC ; la SC ne sort pas devant le leader ; un seul pilote par accident. Piste suggérée : échantillonnage par hypercube latin pour réduire le nombre de tirages.
- Les neutralisations doivent être fixées en temps de course et non en tours, pour toucher tous les pilotes au même instant (p. 7). C'est pourquoi le code tire tous les événements avant la course (p. 10).

## Confrontation avec prompt_calibration.md

| Section | Déjà couvert | Manque | Contredit |
| --- | --- | --- | --- |
| Événements | nombre, tour de début et durée des SC et VSC ; transitions VSC vers SC ; causes ; rythme sous neutralisation ; perte au stand par régime | loi du nombre de SC par course ; part des SC au premier tour et loi de début par tranches de 20 % ; P(VSC sachant panne) et P(SC sachant accident) ; critères de sélection des tours pour le rythme sous neutralisation (p. 6) ; loi de durée d'immobilisation par écurie | rien |
| Écuries et pilotes 2026 | régularité (sigma résiduel) ; fiabilité et erreurs par cause | a priori Beta pour les accidents (pilote) et les pannes (écurie) ; envol mesuré en temps | l'envol en places gagnées ou perdues est l'approche que l'article critique (p. 4) |
| Lissage | formule générique (n × moyenne + k × a priori) / (n + k) | pour une probabilité, c'est un a priori Beta avec k = α + β : estimer α et β par la méthode des moments (éq. 11 et 12) | rien |
| Données externes | base TUM et fichiers *.ini | pars_mcs.ini (toutes les lois du Monte-Carlo 2014 à 2019) ; tableau 6 comme référence de perte au stand par régime | rien |
| Modèle de rythme (hors du périmètre demandé) | effet carburant paramétrique | | masse au départ de 70 kg par défaut, alors que le code TUM utilise 100 à 110 kg pour 2014 à 2019 : à fixer par ère |

## Ce que le projet en retient
- Les lois 2014 à 2019 servent de valeurs par défaut et d'a priori, jamais de valeurs 2026 : tout se recalcule sur 2023 à 2026.
- Notre moteur à événements en temps continu n'a pas besoin de tirer les neutralisations avant la course, puisque le problème de discrétisation qui l'imposait (p. 10) n'existe pas chez nous. Nos déclencheurs causaux doivent en revanche reproduire les mêmes marges : nombre de SC par course, part au premier tour, durées.
- La perte au stand calculée par la géométrie (prompt_jeu.md) va dans le sens de l'article, qui rejette le facteur 0,5. Le tableau 6 et les rapports VSC sur vert et SC sur vert servent de tests de vraisemblance.
- À ajouter au jeu : immobilisation log-logistique par écurie, pénalité de pneus froids, envol en temps, écart minimal derrière la SC, aide au dépassement désactivée après la SC.
- Le prédicteur doit afficher un intervalle de confiance. Avec 200 tirages, l'incertitude sur la position moyenne serait de l'ordre de ± 0,2 place (déduit par extrapolation en 1/√N du tableau 8 ; hypothèse).
