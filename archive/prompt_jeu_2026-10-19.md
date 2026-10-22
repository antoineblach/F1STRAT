# Projet : jeu de stratégie de course automobile (navigateur, solo contre IA)

Version consolidée du 19/10/2026 (intègre la vidéo Chain Bear, le document de sources et Heilmeier et al. 2020). Mise à jour : plateau réel.

## Contexte
Jeu de type « muret des stands » : le joueur dirige une écurie de deux voitures pendant UNE course (pas de qualif, pas de saison, pas de gestion d'écurie). Il ne pilote pas : il décide des arrêts, des gommes, du carburant, du mode de pilotage et des consignes d'équipe. Adversaires : IA.

Plateau réel : circuits, écuries et pilotes de la saison 2026. Le joueur choisit un GP du calendrier 2026 et une écurie. Projet personnel, local, non diffusé : aucune contrainte de licence ni d'anonymat.

Documents de référence (dossier docs/) :
- chainbear_strategie_f1_releve.md : concepts (modèle à blocs, pit delta, undercut, overcut, météo).
- sources_donnees_strategie_f1.md : sources, pièges, grandeurs à dériver.
- notes_vse_heilmeier_2020.md : résumé de l'article sur le Virtual Strategy Engineer.
Signale tout conflit entre ce prompt et ces documents au lieu de trancher seul.

Travaille par lots. À la fin de chaque lot : tests verts, résumé de ce qui est fait, écarts par rapport à ce document, puis arrêt pour validation avant le lot suivant. Demande avant d'ajouter une dépendance hors liste ou de modifier l'architecture ci-dessous.

## Stack
- Vite, TypeScript strict, React (UI), Canvas 2D (carte du circuit), Web Workers, Vitest, zod (validation des données).
- Aucune autre dépendance sans accord. Site statique, aucun backend, aucun appel d'API pendant une partie.
- Identifiants et commentaires de code en anglais. Unités SI en interne (s, m, kg).
- Crée un CLAUDE.md qui résume ces conventions, l'architecture et les règles git ci-dessous.

## Dépôt git
- Un seul dépôt GitHub privé pour tout le projet : jeu à la racine, calibration/ pour l'outil Python, docs/ pour les documents de référence. Nom proposé : f1strat, à confirmer avec moi.
- Création au lot 1 avec la CLI GitHub (gh), que j'authentifie moi-même sur ma machine : gh repo create f1strat --private. Si gh n'est pas installé ou authentifié, ou si la création ou la poussée échoue : continue en dépôt local, signale-le, la poussée se fera plus tard.
- .gitignore dès le premier commit : node_modules/, dist/, .venv/, calibration/.cache/, calibration/inputs/external/, *.parquet, *.sqlite, fichiers d'éditeur et de système.
- Aucun fichier de plus de 50 Mo versionné (GitHub refuse au-delà de 100 Mo) : vérifie avant chaque commit.
- Aucun secret dans le dépôt. Aucun n'est prévu : FastF1 et Open-Meteo fonctionnent sans clé.
- Une branche par lot : jeu/lot-01-squelette, calib/lot-01-ingestion, etc. En fin de lot : commits lisibles, poussée, pull request contenant le résumé du lot et les écarts par rapport au prompt. Je relis et je fusionne ; tu ne fusionnes jamais toi-même.
- Tag à chaque lot fusionné : jeu-lot-01, calib-lot-01, etc.

## Architecture imposée
src/
  sim/        simulation pure : aucun accès DOM, aucun Date.now, aucun Math.random
    engine/   rng.ts, eventQueue.ts, state.ts, race.ts (boucle à événements), commands.ts
    model/    lapTime.ts, tyres.ts, fuel.ts, weather.ts, overtaking.ts, pit.ts, safetyCar.ts, reliability.ts, start.ts
    rules.ts  règlement paramétrable
  ai/         estimator.ts, planner.ts, reactive.ts, profiles.ts
  data/       JSON : tracks/, compounds.json, teams.json, drivers.json, weather/, rules.json, plus schemas.ts (zod)
  worker/     race.worker.ts, predictor.worker.ts, protocol.ts (messages typés)
  ui/         composants React
tools/        CLI Node : run-race.ts, batch.ts, replay.ts
tests/

sim/ doit produire des résultats identiques dans le navigateur (worker) et sous Node (CLI, tests).

## Moteur
- Simulation à événements discrets. Le circuit est découpé en micro-secteurs (environ 20 par tour, définis dans le JSON du circuit). Événement principal : « la voiture i atteint la fin du micro-secteur k à l'instant t ». File de priorité ordonnée par instant.
- Temps de simulation découplé du temps réel. API du moteur : advanceTo(tSim), applyCommand(cmd), snapshot(), clone().
- Déterminisme : même graine + même journal d'ordres horodatés = même course, à l'identique.
- RNG : générateur à graine implémenté localement (xoshiro128** ou équivalent). Flux indépendants dérivés de (graine, sous-système, voiture, tour) pour : météo, incidents, fiabilité, bruit de temps au tour, durée des arrêts, départ. Exigence : modifier une décision ne doit pas changer les tirages des autres sous-systèmes ni des autres voitures (nombres aléatoires communs pour comparer des stratégies).
- Les ordres (joueur ou IA) sont horodatés et appliqués à la frontière de micro-secteur suivante. Un appel aux stands reçu après la ligne d'entrée des stands est reporté au tour suivant.

## Modèle de temps
Temps au tour calculé puis réparti par micro-secteur selon des poids du JSON circuit (somme = 1) :

T = T_ref(circuit)
  + delta_voiture
  + delta_pilote
  + k_carbu * masse_carburant
  + delta_gomme(composé)
  + f_usure(composé, usure)
  + delta_mode(mode de pilotage)
  + delta_evolution(tour)              gain d'adhérence au fil de la course, partiellement remis à zéro par la pluie
  + delta_mouille(humidité locale, composé)   appliqué par micro-secteur
  + delta_air_sale(écart avec la voiture devant)
  + bruit ~ N(0, sigma_pilote)
  + delta_erreur                       erreur ponctuelle, probabilité selon pilote, mode et humidité

Pneus
- Composés : tendre, médium, dur, intermédiaire, pluie. Paramètres par composé : delta de performance, taux d'usure, seuil de falaise, pente après falaise, plage d'humidité utile.
- Usure par tour = taux(composé) * abrasivité(circuit) * facteur(mode) * facteur(gestion pneus du pilote) * facteur(air sale) * facteur(masse_carburant) * facteur(régime de course).
- facteur(masse_carburant) : une gomme se dégrade plus vite réservoir plein.
- facteur(régime de course) : 1 en vert ; valeurs par défaut 0,5 sous VSC et 0,25 sous SC (hypothèse reprise de Heilmeier et al. 2020, qui font progresser l'âge du pneu 50 % et 75 % moins vite sous VSC et SC), remplaçables par la calibration.
- f_usure linéaire jusqu'au seuil, puis pente forte (falaise). Au-delà de 100 % : risque de crevaison croissant.
- Gommes pluie et intermédiaires sur piste sèche : surchauffe et usure très accélérée.
- Âge du pneu au départ paramétrable par voiture (pneus neufs ou déjà utilisés).

Carburant
- Masse au départ choisie avant la course, bornée par le règlement. Consommation par tour * facteur(mode). Panne sèche = abandon.

Mode de pilotage
- 5 niveaux, de l'économie forte à l'attaque. Chaque niveau module : temps, usure, consommation, probabilité d'erreur, taux de défaillance moteur.

Météo spatiale
- La géométrie 2D du circuit est une donnée du moteur, pas seulement de l'UI : chaque micro-secteur a une position dans le plan.
- Pluie = ensemble de cellules (centre, rayon, intensité, cycle croissance, maturité, dissipation) transportées par le vent (vitesse, direction, dérive lente). Les cellules naissent selon un processus aléatoire dont le taux et les caractéristiques viennent du scénario ; un taux nul donne une course sèche.
- Pluie locale d'un micro-secteur = somme des contributions des cellules à sa position.
- Humidité par micro-secteur : monte avec la pluie locale ; baisse avec le passage des voitures, la température de piste et un coefficient de drainage propre au micro-secteur.
- Point de croisement slick, intermédiaire, pluie modulé par l'attribut pluie du pilote.
- Radar : image basse résolution du champ de pluie, observée avec bruit et rafraîchie à intervalle fixe (paramètre). Prévision = extrapolation du déplacement des cellules observées, estimé sur les dernières images, sans connaissance des naissances et dissipations futures. Aucun bruit de prévision ajouté artificiellement.
- Le joueur et l'IA disposent exactement des mêmes images radar et de la même prévision.

Dépassements et trafic
- À chaque frontière de micro-secteur, si l'arrivée projetée du suiveur est antérieure à celle de la voiture devant + écart minimal :
  - micro-secteur sans dépassement possible : suiveur recalé à l'écart minimal ;
  - micro-secteur de dépassement : tentative avec P = sigmoïde(a*delta_rythme + b*aide_au_dépassement + c*(attaque - défense) - difficulté_circuit). Échec : recalage et surcroît d'usure. Faible probabilité de contact (dégâts, crevaison ou abandon).
- Air sale : pénalité de temps et d'usure sous un écart seuil.
- Retardataires : drapeau bleu, ils cèdent avec une petite perte de temps.
- Aide au dépassement : mécanisme, conditions d'activation et zones selon le règlement 2026. Le DRS a peut-être été remplacé en 2026 : vérifie dans le règlement FIA avant d'implémenter, ne suppose rien. Paramétrée par circuit, désactivée au-delà d'un seuil d'humidité.

Arrêts aux stands
- La voie des stands est un chemin parallèle aux micro-secteurs compris entre l'entrée et la sortie (indices dans le JSON circuit). Temps dans la voie = longueur / vitesse limite + temps d'arrêt (distribution à queue lourde) + pertes de décélération et d'accélération.
- Perte au stand = temps dans la voie - temps que la voiture aurait mis sur les micro-secteurs évités dans les conditions du moment. Ce n'est jamais un paramètre direct : sous VSC ou SC, les micro-secteurs évités ralentissent et la perte baisse d'elle-même.
- Deux voitures de la même écurie au même tour : la seconde attend.
- Règle : au moins deux composés secs différents, sauf usage d'intermédiaires ou de pluie. Non-respect : pénalité en temps à l'arrivée (paramètre).

Safety car et VSC
- Déclenchés par incidents, débris, crevaisons, voitures immobilisées ou météo, pondérés par les parts de causes calibrées (calibration/export/events.json). Probabilité d'incident selon la zone du circuit.
- VSC : toutes les voitures ralenties, écarts conservés, durée courte ; peut se transformer en SC (probabilité paramétrée).
- SC : peloton regroupé à l'écart minimal en quelques tours, dédoublement des retardataires paramétrable, relance avec risque d'incident accru.
- Rythme sous neutralisation : valeurs par défaut 140 % du temps au tour vert sous VSC et 160 % sous SC (Heilmeier et al. 2020, données 2014 à 2019), remplaçables par la calibration.
- Durées de SC et de VSC tirées dans des distributions séparées issues de la calibration.

Fiabilité
- Taux de défaillance par composant (moteur, boîte, hydraulique) et par voiture, majoré par le mode d'attaque. Effet : abandon ou perte de performance.

Départ
- Grille réelle du GP s'il a eu lieu (calibration/export/grids.json), sinon générée (rythme + bruit), au choix du joueur. Qualité d'envol aléatoire selon le pilote. Risque d'incident accru au premier tour.
- Perte de temps au premier tour fonction de la position sur la grille (terme t_grid de Heilmeier et al.).
- La gomme module la qualité d'envol et le rythme du premier tour (la plus tendre est la plus adhérente à froid).

## Information
- Écurie du joueur : usure, carburant et état exacts.
- Rivaux : composé, âge du relais et nombre d'arrêts visibles ; usure estimée à partir des temps au tour, avec erreur ; carburant inconnu.
- L'IA est soumise exactement aux mêmes restrictions. Aucun ajustement de performance pour équilibrer la course.

## IA
- profiles.ts : profil par écurie (prudent, neutre, agressif) qui fixe seuils et tolérance au risque.
- estimator.ts : modèle tour par tour d'une voiture seule, sans interactions, avec pénalité de trafic moyenne. Rapide, volontairement plus simple que la simulation. Accepte une fonction de temps au tour injectée (profil tabulé par âge du pneu), pour les tests de référence.
- planner.ts, avant la course :
  - Programmation dynamique sur les relais. Coût d'un relais = somme des temps au tour estimés pour (composé, longueur, tour de départ), précalculée. État = (tours couverts, ensemble des composés secs déjà utilisés, nombre d'arrêts). Exact pour toute fonction de coût de relais, y compris falaise et effet carburant ; l'ordre des relais compte.
  - 1 à 3 arrêts en sec. Un arrêt supplémentaire n'est retenu que s'il rapporte au moins un seuil (défaut 2 s, d'après Heilmeier et al. 2020), paramètre du profil.
  - Les meilleures stratégies de chaque nombre d'arrêts sont ensuite évaluées sur K tirages météo et SC avec l'estimateur, classées selon le profil, avec un léger aléa pour éviter des stratégies identiques.
  - Sortie : trois plans (A, B, C). Le joueur reçoit les mêmes trois plans pour ses voitures. Relancé sur événement majeur (pluie, SC, dégâts).
- reactive.ts, à chaque tour, avec au minimum les signaux suivants (repris de Heilmeier et al. 2020) : progression de la course ; progression de l'âge du pneu ; leader ou poursuivant ; composé relatif ; sévérité du circuit ; statut de neutralisation (aucune, premier tour de VSC, VSC en cours, premier tour de SC, SC en cours) ; arrêts restants au plan ; poursuivant qui vient de s'arrêter ; poursuivant à moins de 1,5 s.
- Règles de reactive.ts :
  - arrêt si falaise imminente ;
  - neutralisation : décision au premier tour de VSC ou SC ; arrêt si le gain estimé dépasse le seuil du profil et qu'un arrêt reste au plan ; pas d'arrêt si les pneus sont encore frais (seuil d'âge paramétré) ; le leader tient compte du fait que ses poursuivants peuvent s'arrêter au même tour ;
  - couverture d'undercut : si le poursuivant à moins de 1,5 s vient de s'arrêter et que l'arrêt prévu est dans la fenêtre, s'arrêter maintenant ;
  - undercut offensif si la voiture devant est dans la fenêtre de perte au stand et que le gain de pneus neufs le permet ;
  - air libre : avant un arrêt, calcule la sortie projetée (écart au leader + perte au stand courante). Si elle tombe dans un groupe serré que la voiture ne pourra pas dépasser, retarde l'arrêt tant que l'usure le permet ;
  - attente de SC : prolonge un relais si le gain espéré (risque de SC sur les tours restants × gain d'un arrêt sous SC) dépasse la perte due à l'usure ; seuil selon le profil ;
  - changement slicks, intermédiaires ou pluie quand l'humidité franchit le point de croisement, avec hystérésis ;
  - économie de carburant si la projection est insuffisante ; consignes d'équipe ;
  - bascule entre plans A, B et C sur événement.

## Prédicteur du joueur
- predictor.worker.ts clone l'état courant et fait tourner la simulation complète jusqu'à l'arrivée, N fois par stratégie candidate (N réglable, défaut 200), avec nombres aléatoires communs entre candidates.
- Sortie : distribution de la position et du temps d'arrivée pour chaque candidate. Mesure le temps de calcul et remonte-le ; ne simplifie pas le modèle pour tenir une cible sans mon accord.

## Instantanés (contrat avec l'UI)
Les vues finales seront conçues plus tard. Le moteur expose dès maintenant, dans chaque instantané :
- par voiture : position, distance sur le tour, écart au leader en temps (continu), intervalle avec la voiture devant, gomme, âge du pneu, usure (exacte pour le joueur, estimée pour les rivaux), carburant projeté (joueur seulement), mode, statut (piste, stands, abandon) ;
- temps au tour de référence ;
- perte au stand courante pour les régimes vert, VSC et SC ;
- pour chaque voiture du joueur : sortie projetée si elle s'arrête maintenant (écart au leader, position, voitures à moins de N s devant et derrière) ;
- pluie locale et humidité par micro-secteur ;
- dernière image radar et prévision (pas de temps et horizon paramétrables) ;
- statut de course (vert, jaune, VSC, SC, rouge) ;
- profil de temps au tour estimé par gomme et âge du pneu ;
- historique des écarts au leader, tour par tour ;
- plans A, B et C de chaque voiture du joueur.

## UI
- Lot 6 : UI fonctionnelle minimale. La boucle d'animation demande au worker d'avancer jusqu'à t_cible = horloge * vitesse ; le worker renvoie des instantanés à environ 10 Hz ; l'UI interpole. Contrôle du temps (pause, x1, x2, x4, x8, x16, saut au prochain événement), longueur de course (25 %, 50 %, 100 %), carte simple, tour de chronométrage (bascule écart au leader et intervalle), ordres du joueur, écran de fin. Aucun travail de style.
- Lot 9 : vues stratégiques d'après des maquettes que je fournirai : cercle des écarts (tour vu comme un cercle, arcs de perte au stand vert, VSC et SC, sortie projetée), carte avec humidité par secteur, radar avec curseur temporel, planificateur de relais (profil de temps au tour par gomme, arrêt déplaçable, total, seuil où deux arrêts deviennent gagnants), graphe des écarts, courbes de croisement par gomme.

## Données
- Un fichier par circuit du calendrier 2026, depuis calibration/export/circuits/<circuit>.json : longueur, géométrie 2D réelle, micro-secteurs (alignés sur les secteurs de commissaires quand l'export les fournit ; poids, type, dépassement possible ou non, position 2D, coefficient de drainage, probabilité d'incident), zones d'aide au dépassement, voie des stands (géométrie, indices d'entrée et de sortie, longueur, vitesse limite), abrasivité, T_ref, gommes nommées pour le GP, climat.
- Écuries et pilotes 2026 réels, depuis calibration/export/teams.json et drivers.json. Écurie : nom, couleur, delta voiture (forme récente, par GP), fiabilité, efficacité carburant. Pilote : nom, code, rythme, régularité (sigma), gestion des pneus, envol, pluie, attaque, défense, taux d'erreur.
- Scénarios météo par circuit, depuis calibration/export/weather.json.
- Tous les paramètres numériques dans les JSON, validés par zod au chargement. Aucune constante de modèle en dur dans le code.
- Valeurs lues depuis calibration/export/ (circuits/, teams.json, drivers.json, grids.json, compounds.json, field.json, events.json, behaviour.json, weather.json) ; fichier absent : valeurs provisoires marquées comme telles. k_fuel et la consommation par tour sont partagés avec la configuration de calibration.
- Dans les schémas zod, tout paramètre numérique peut porter sa provenance { method, source } ; une valeur sans provenance est traitée comme hypothèse. Les attributs que les données ne permettent pas d'estimer restent des hypothèses visibles comme telles dans l'UI de débogage.
- rules.json : chaque règle tirée du règlement FIA 2026 (sections B et F, versions citées dans docs/sources_donnees_strategie_f1.md) porte sa référence d'article. Règle introuvable : marquée manquante, jamais inventée.

## Outillage et tests
- CLI : run-race (une course, résumé texte), batch (N courses sans UI vers CSV : positions, arrêts, dépassements, abandons, SC, écarts), replay (graine + journal d'ordres vers résultat identique).
- Tests obligatoires : déterminisme ; indépendance des flux RNG (modifier un arrêt ne change ni la météo ni les incidents des autres voitures) ; monotonie de f_usure et existence de la falaise ; panne sèche ; règle des deux composés ; regroupement sous SC ; conservation des écarts sous VSC ; hystérésis météo de l'IA ; application des ordres à la bonne frontière.
- Cas de référence (modèles en blocs, estimateur seul, sans carburant ni aléa, deux composés obligatoires) :
  - 10 tours ; tendre 3 blocs par tour, 4 tours maximum ; médium 4 blocs par tour. Un arrêt optimal : 4 tendre + 6 médium = 36 + P. Deux arrêts : 4 + 4 tendre + 2 médium = 32 + 2P. Égalité à P = 4.
  - 20 tours ; profil tendre par âge 3,3,3,4,4,5,5,6,6,7,7,8,8,9,9 (15 tours maximum) ; profil médium 4,4,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9. Un arrêt optimal : 9 tendre + 11 médium = 92 + P. Deux arrêts tendre, tendre, médium : minimum 79 + 2P, atteint par 5-7-8, 6-6-8, 6-7-7 et 7-7-6 (relais tendres non ordonnés). Deux arrêts meilleurs si P < 13.
  - Course de 55 tours, dégradation linéaire t = k0 + k1 * âge, dur (1,2 s ; 0,016 s/tour), médium (0,5 s ; 0,05 s/tour), tendre (0 s ; 0,09 s/tour), départ en tendre avec 2 tours d'âge : le planificateur retrouve l'optimum d'une énumération exhaustive (Heilmeier et al. 2020 donnent tendre 22 tours + médium 33 tours, et tendre 18 tours + dur 37 tours pour ces deux combinaisons).
- Perte au stand qui baisse sous VSC puis sous SC sur un circuit de test, sans paramètre dédié.
- Météo : une cellule qui traverse le circuit mouille les micro-secteurs dans l'ordre de son passage ; la prévision se trompe quand une cellule naît hors du champ observé.
- Mesure et affiche la durée d'un batch de 1 000 courses complètes (20 voitures, 60 tours).

## Lots
1. Dépôt git et .gitignore, squelette, schémas de données, RNG, file d'événements, temps au tour sans interactions, carburant, pneus secs, arrêts planifiés fixes, CLI run-race et batch, tests de déterminisme.
2. Interactions : dépassements, air sale, aide au dépassement, retardataires, contacts, départ.
3. SC, VSC, fiabilité, crevaisons.
4. Météo spatiale : cellules, vent, humidité par micro-secteur, drainage, radar et prévision, intermédiaires et pluie.
5. IA : estimateur, planificateur, réactions, profils, cas de référence.
6. UI fonctionnelle minimale (voir section UI).
7. Prédicteur Monte-Carlo dans l'UI.
8. Calibration : batch comparé à calibration/export/targets.json et behaviour.json, rapport des écarts par cible, en comptant les dépassements comme le pipeline (en piste, hors tour 1, arrêts, SC, VSC et relances).
9. Vues stratégiques d'après maquettes.

## Hors périmètre
Qualifications, réglages de voiture, saison, gestion d'écurie, ERS distinct du mode de pilotage, température des pneus, pénalités autres que la règle des composés, multijoueur, 3D, son, sauvegarde en cours de course (hors replay), IA à réseaux de neurones.
