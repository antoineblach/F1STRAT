# Virtual Strategy Engineer (Heilmeier et al., 2020) : notes pour le projet

Article : Heilmeier, Thomaser, Graf, Betz, « Virtual Strategy Engineer: Using Artificial Neural Networks for Making Race Strategy Decisions in Circuit Motorsport », Applied Sciences 10(21) 7805, 2020, DOI 10.3390/app10217805, licence CC BY 4.0. Lu en entier le 19/10/2026. Les numéros de page renvoient au PDF.

## Code et données (établi)
- Simulation de course en Python, avec les modèles VSE entraînés : https://github.com/TUMFTM/race-simulation (p. 29). Licence LGPL-3.0 (page GitHub). Contient des fichiers de paramètres pour les 121 courses 2014 à 2019 (racesim/input/parameters/*.ini) et des VSE par apprentissage par renforcement préentraînés, sauf courses (partiellement) mouillées (README).
- Base de chronométrage 2014 à 2019 : https://github.com/TUMFTM/f1-timing-database (p. 7). SQLite, licence CC BY-NC-SA 3.0 (usage non commercial, partage à l'identique). Tables laps, fcyphases, races, starterfields, qualifyings, drivers, retirements. Sources : Ergast, plus ajouts (phases VSC et SC, gommes, longueurs de circuit) ; abandons depuis racefans.net (README).

## Modèle de temps au tour de leur simulation (p. 3)
t_lap = t_base + t_tire(âge, gomme) + t_fuel(tour) + t_car + t_driver + t_grid(tour, position de grille) + t_pit (tour d'entrée et de sortie). Simulation tour par tour ; dépassements détectés en comparant les temps cumulés en fin de tour. Effets aléatoires (variabilité du tour, durée d'arrêt, phases VSC et SC) évalués par Monte-Carlo.

## Valeurs reprises (établies dans l'article, ère 2014 à 2019)
- Temps au tour sous VSC ≈ 140 % d'un tour normal, sous SC ≈ 160 % (p. 7, citant leur référence [3]).
- Pour leurs entrées, l'âge du pneu progresse 50 % moins vite sous VSC et 75 % moins vite sous SC, les pneus étant moins sollicités (p. 9). C'est un choix de modélisation, pas une mesure.
- Pneus au départ des 10 premiers : 2 tours d'âge (p. 16, règle de l'époque).
- Base : 131 527 tours sur 121 courses, 4 087 changements de pneus, soit 3,1 % des tours (p. 7).
- Âge normalisé du pneu au changement (filtré) : dur 38,8 %, médium 34,1 %, tendre 29,5 % de la course (p. 9, tableau 3).
- Gomme au départ, saisons 2016 à 2019 : dur 4,4 %, médium 32,5 %, tendre 63,1 % (p. 24, tableau 17).
- Les pilotes s'arrêtent le plus souvent au premier tour d'une neutralisation (p. 10). Une SC vers 17 % de course ne déclenche pas d'arrêt dans leur exemple, une SC plus tardive oui (p. 21).
- Le leader décide souvent autrement que ses poursuivants, par exemple à l'arrivée d'une SC (p. 9).
- Un arrêt supplémentaire n'est retenu dans la stratégie de base que s'il rapporte au moins 2 s (p. 16).

## Stratégie de base (p. 13 à 16)
- Sur piste libre et sans aléa, avec dégradation linéaire t_tire = k0(c) + k1(c) × âge, les longueurs de relais optimales se calculent par un problème quadratique en nombres entiers (MIQP) : environ 150 ms pour 22 combinaisons de gommes sur 55 tours, contre environ 20 s en force brute (Python).
- Leurs hypothèses : ordre des relais indifférent, dégradation indépendante de la masse de carburant. Dans notre jeu, l'usure dépend de la masse de carburant (vidéo Chain Bear) : l'ordre compte, d'où le choix d'une programmation dynamique sur les relais plutôt que du MIQP.
- Exemple (tableau 8) : 55 tours, départ en tendre avec 2 tours d'âge ; dur k0 = 1,2 s, k1 = 0,016 s/tour ; médium 0,5 s, 0,05 s/tour ; tendre 0 s, 0,09 s/tour. Optimum tendre 22 tours + médium 33 tours, et tendre 18 + dur 37 pour l'autre combinaison. Vérifié par énumération le 19/10/2026. Repris comme test de référence.

## Le VSE lui-même (p. 7 à 25)
- Deux réseaux : décision d'arrêt (oui ou non) à chaque tour, puis choix de la gomme (tendre, médium, dur) si arrêt.
- Entrées de la décision d'arrêt (tableau 5) : progression de la course, progression de l'âge du pneu, leader ou poursuivant, gomme relative, catégorie de circuit (1 à 3, d'après la gomme la plus dure disponible en 2019), statut de neutralisation (0 aucune, 1 premier tour de VSC, 2 VSC en cours, 3 premier tour de SC, 4 SC en cours), arrêts restants (issus de la stratégie de base), poursuivant qui vient de s'arrêter, à moins de 1,5 s devant son poursuivant.
- Entrées du choix de gomme (tableau 7) : progression, arrêts restants, gomme relative, circuit, deuxième gomme déjà utilisée, nombre de gommes disponibles.
- Entraînement sur données réelles 2014 à 2019, courses sèches, pilotes classés dans les 10 premiers pour la décision d'arrêt (p. 11). Réseau hybride (3 couches de 64 neurones plus une cellule LSTM sur 4 tours) : score F1 ≈ 0,59 ; il prédit souvent l'arrêt plusieurs tours trop tôt (p. 19 et 20). Choix de gomme : précision ≈ 0,77 (p. 21).
- Limites reconnues par les auteurs (p. 27) : pas d'undercut actif, pas de recherche d'air libre, pas de facteurs de théorie des jeux, réseaux figés sur une ère réglementaire.
- Perspective (p. 28) : un agent par renforcement entraîné dans la simulation fait mieux dans un premier test (position moyenne 8,46 contre 9,51 sur une course de 2019), mais apprend aussi les erreurs de la simulation.

## Ce que le projet en retient
- Pas de VSE dans la version 1 : ère 2014 à 2019 avec la règle des pneus de qualification, gommes relatives d'une autre époque, besoin d'un nombre d'arrêts fixé à l'avance, décisions souvent prématurées, et portage TensorFlow vers TypeScript à prévoir.
- Ses entrées deviennent les signaux obligatoires de l'IA à règles (reactive.ts).
- Ses statistiques de comportement deviennent des cibles de calibration, recalculées sur 2023 à 2026.
- Notre IA couvre explicitement ce que le VSE ne savait pas faire : air libre et undercut actif.
- Une IA apprise (supervisée sur FastF1 2023 à 2026, ou par renforcement dans notre simulateur) reste une option après la version 1.
