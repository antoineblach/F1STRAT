# Projet : jeu de stratégie de course automobile (navigateur, solo contre IA)

Version du 20/10/2026. Remplace la version du 19/10/2026. Intègre la synthèse des enjeux de réalisme (docs/synthese_enjeux_realisme.md), ses décisions, l'arbitrage des amendements de la veille bibliographique et le règlement FIA 2026.

## Contexte
Jeu de type « muret des stands » : le joueur dirige une écurie de deux voitures pendant UNE course (pas de qualif, pas de saison, pas de gestion d'écurie). Il ne pilote pas : il décide des arrêts, des gommes, du carburant, du mode de pilotage et des consignes d'équipe. Adversaires : IA.

Plateau réel : circuits, écuries et pilotes de la saison 2026, règlement 2026. Le joueur choisit un GP du calendrier 2026 et une écurie. Projet personnel, local, non diffusé : aucune contrainte de licence ni d'anonymat.

Documents de référence (dossier docs/) :
- synthese_enjeux_realisme.md : décisions de modélisation, articles du règlement 2026 (section 6), valeurs de référence (annexe A). En cas de conflit entre documents, elle fait foi ; signale le conflit.
- chainbear_strategie_f1_releve.md : concepts (modèle à blocs, pit delta, undercut, overcut, météo).
- sources_donnees_strategie_f1.md : sources, pièges, grandeurs à dériver ; partiellement dépassé (synthèse, section 1.2).
- notes_vse_heilmeier_2020.md : Virtual Strategy Engineer (Heilmeier et al. 2020, Appl. Sci. 10(21) 7805).
- notes_montecarlo_heilmeier_2020.md : lois probabilistes 2014 à 2019 et code TUM (Heilmeier et al. 2020, Appl. Sci. 10(12) 4229).
- veille_biblio_strategie.md : modèle de dépassement TUM, sources secondaires.
- reglement/ : règlement FIA F1 2026, sections A, B et C (PDF).
Deux articles de Heilmeier et al. datent de 2020 et ont chacun un tableau 8 : cite toujours « VSE » ou « Monte-Carlo ».
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
    model/    lapTime.ts, tyres.ts, tyreSets.ts, fuel.ts, weather.ts, overtaking.ts, overtakeMode.ts, pit.ts, safetyCar.ts, redFlag.ts, reliability.ts, start.ts
    rules.ts  règlement paramétrable
  ai/         estimator.ts, planner.ts, reactive.ts, profiles.ts
  data/       JSON : tracks/, compounds.json, teams.json, drivers.json, grids.json, weather/, rules.json, plus schemas.ts (zod)
  worker/     race.worker.ts, predictor.worker.ts, protocol.ts (messages typés)
  ui/         composants React
tools/        CLI Node : run-race.ts, batch.ts, replay.ts
tests/

sim/ doit produire des résultats identiques dans le navigateur (worker) et sous Node (CLI, tests).

## Moteur
- Simulation à événements discrets. Le circuit est découpé en micro-secteurs (environ 20 par tour, définis dans le JSON du circuit), regroupés en trois secteurs officiels. Événement principal : « la voiture i atteint la fin du micro-secteur k à l'instant t ». File de priorité ordonnée par instant.
- Temps de simulation découplé du temps réel. API du moteur : advanceTo(tSim), applyCommand(cmd), snapshot(), clone().
- Déterminisme : même graine + même journal d'ordres horodatés = même course, à l'identique.
- RNG : générateur à graine implémenté localement (xoshiro128** ou équivalent). Flux indépendants dérivés de (graine, sous-système, voiture, tour) pour : météo, incidents, fiabilité, bruit de temps au tour, durée des arrêts, départ, procédures de neutralisation. Exigence : modifier une décision ne doit pas changer les tirages des autres sous-systèmes ni des autres voitures (nombres aléatoires communs pour comparer des stratégies).
- Les ordres (joueur ou IA) sont horodatés et appliqués à la frontière de micro-secteur suivante. Un appel aux stands reçu après la ligne d'entrée des stands est reporté au tour suivant.

## Modèle de temps
Temps au tour calculé puis réparti par micro-secteur selon des poids du JSON circuit (somme = 1) :

T = T_ref(circuit)
  + delta_voiture
  + delta_pilote
  + k_carbu * masse_carburant
  + delta_gomme(composé)
  + f_usure(composé, usure)
  + delta_pneus_froids                 premier tour de chaque relais
  + delta_mode(mode de pilotage)
  + delta_evolution(tour)              gain d'adhérence au fil de la course, partiellement remis à zéro par la pluie
  + delta_mouille(humidité du secteur, composé)   appliqué par micro-secteur, selon le secteur officiel qui le contient
  + delta_air_sale(écart avec la voiture devant)
  + delta_mode_depassement             gain du suiveur sur les zones d'activation quand le mode dépassement est actif
  + bruit ~ N(0, sigma_pilote)
  + delta_erreur                       erreur ponctuelle, probabilité selon pilote, mode et humidité (hypothèse : aucune source chiffrée ; calibrable sur la queue haute des résidus)

L'aileron actif en mode ligne droite est commun à toutes les voitures (règlement B7.1) : son effet est absorbé dans T_ref et les poids des micro-secteurs, sans terme propre.

Pneus
- Composés : tendre, médium, dur, intermédiaire, pluie. Paramètres par composé : delta de performance, taux d'usure, seuil de falaise, pente après falaise, plage d'humidité utile.
- Usure par tour = taux(composé) * abrasivité(circuit) * facteur(mode) * facteur(gestion pneus du pilote) * facteur(air sale) * facteur(masse_carburant) * facteur(régime de course).
- facteur(masse_carburant) = (1 + δ)^(masse / masse_ref), forme de Carrasco Heine et Thraves 2023 (éq. 9) ; δ par défaut 0,1 (valeur de leur code, hypothèse : aucune source ne le mesure) ; masse_ref = masse de départ de référence du circuit. C'est ce couplage qui rend l'ordre des relais significatif.
- facteur(régime de course) : 1 en vert ; valeurs par défaut 0,5 sous VSC et 0,25 sous SC (estimations des auteurs du Monte-Carlo, hypothèse), remplaçables par la calibration.
- f_usure linéaire jusqu'au seuil, puis pente forte (falaise). Au-delà de 100 % : risque de crevaison croissant. Le seuil de falaise issu des données est une borne basse.
- La dégradation calibrée correspond au rythme géré des équipes : elle s'applique au niveau « neutre » du mode de pilotage ; les autres niveaux en sont des extrapolations (hypothèse).
- Pneus froids : delta_pneus_froids = 1,0 s par défaut (code TUM 2014 à 2019, hypothèse), au premier tour de chaque relais, en plus de la perte au stand calculée par la géométrie. La calibration en rapporte un contrôle.
- Gommes pluie et intermédiaires sur piste sèche : surchauffe et usure très accélérée.

Inventaire de trains (tyreSets.ts)
- Chaque voiture part avec un inventaire de trains : composé, neuf ou utilisé, âge. Source : calibration/export/grids.json (estimation) ; à défaut, inventaire par défaut tiré de l'allocation du règlement (B6.2.4 : 2 durs, 3 médiums, 8 tendres, 5 intermédiaires, 2 pluie en format standard ; 2, 4, 6, 6, 2 en format sprint) diminuée d'un usage de week-end type (hypothèse, paramètre).
- Un arrêt consomme un train de l'inventaire ; un composé sans train disponible ne peut pas être monté.
- Âge du pneu au départ = âge du train monté.

Carburant
- Aucune masse maximale réglementaire en course en 2026 : le règlement technique limite seulement le débit d'énergie du carburant (3 000 MJ/h, C5.2.3). Masse au départ choisie avant la course, bornée par une capacité de réservoir (paramètre, hypothèse). Ordre de grandeur de consommation : environ 70 kg par course (hypothèse).
- Consommation par tour * facteur(mode) * facteur(régime) : 0,5 sous VSC et 0,25 sous SC par défaut (estimations du Monte-Carlo, hypothèse). Le carburant économisé reste disponible pour la suite de la course. Panne sèche = abandon.

Mode de pilotage
- 5 niveaux, de l'économie forte à l'attaque. Chaque niveau module : temps, usure, consommation, probabilité d'erreur, taux de défaillance moteur.
- La gestion de l'énergie électrique (boost, recharge, lift and coast) est agrégée dans ces niveaux. Limite connue du réalisme : boost et recharge ne sont pas des décisions distinctes. Seul le mode dépassement est explicite.

Météo spatiale
- La géométrie 2D du circuit est une donnée du moteur, pas seulement de l'UI : chaque micro-secteur a une position dans le plan et appartient à un secteur officiel.
- Pluie = ensemble de cellules (centre, rayon, intensité, cycle croissance, maturité, dissipation) transportées par le vent (vitesse, direction, dérive lente). Les cellules naissent selon un processus aléatoire dont le taux et les caractéristiques viennent du scénario ; un taux nul donne une course sèche. Taille et vitesse des cellules : hypothèses (aucune source).
- Pluie locale calculée aux positions des micro-secteurs (somme des contributions des cellules), puis agrégée par secteur officiel (moyenne pondérée par la longueur).
- Humidité par secteur officiel : monte avec la pluie du secteur ; baisse avec le passage des voitures, la température de piste et un coefficient de drainage propre au secteur. Résolution choisie parce que c'est la plus fine observable dans les données (temps par secteur) : les croisements sont calibrés sur les tours de transition (calibration/export/weather.json).
- Point de croisement slick, intermédiaire, pluie modulé par l'attribut pluie du pilote.
- Conditions de faible adhérence (règlement B1.5.11) : déclarées par la direction de course simulée quand l'humidité d'un secteur franchit un seuil (paramètre, hypothèse), levées avec hystérésis. Effets : mode dépassement désactivé (B7.2.2 d), aileron actif partiel (B7.1.2 b, absorbé dans le delta de mouillé), courbes ERS propres (absorbées dans le delta de mouillé).
- Radar : image basse résolution du champ de pluie, observée avec bruit et rafraîchie à intervalle fixe (paramètre). Prévision = extrapolation du déplacement des cellules observées, estimé sur les dernières images, sans connaissance des naissances et dissipations futures. Aucun bruit de prévision ajouté artificiellement.
- Le joueur et l'IA disposent exactement des mêmes images radar et de la même prévision.

Dépassements et trafic
- À chaque frontière de micro-secteur, si l'arrivée projetée du suiveur est antérieure à celle de la voiture devant + écart minimal :
  - micro-secteur hors zone de dépassement : suiveur recalé à l'écart minimal ;
  - zone de dépassement : tentative avec P = sigmoïde(a*delta_rythme + b*mode_depassement_actif + c*(attaque - défense) + e*delta_vitesse_pointe - difficulté_circuit). Échec : recalage et surcroît d'usure. Faible probabilité de contact (dégâts, crevaison ou abandon).
- Zones de dépassement : une zone peut couvrir plusieurs micro-secteurs consécutifs (ligne droite plus freinage) ; la tentative se décide sur l'ensemble de la zone, pas dans un seul micro-secteur. Plusieurs voitures peuvent dépasser dans la même zone. La difficulté reste un paramètre par circuit, pas par micro-secteur (critique du modèle par secteurs de Bekker, Heilmeier et al. 2018, p. 2987).
- difficulté_circuit : initialisée à partir du seuil de dépassement TUM du circuit quand il existe (1,26 à 3,75 s, médiane 2,0 s), puis calibrée sur les dépassements en piste 2026 seuls.
- delta_vitesse_pointe : écart de vitesse de pointe (proxy de calibration) entre les deux voitures ; coefficient e mis à 0 si la calibration ne le trouve pas significatif.
- Écart minimal entre voitures : 0,5 s en vert, 0,8 s derrière la SC (défauts du code TUM). Contrôlé aussi à chaque sortie des stands.
- Duel : deux voitures à moins de l'écart minimal perdent chacune du temps (défaut 0,3 s par tour) ; la voiture dépassée perd en plus 0,3 s (défauts du code TUM).
- Air sale : pénalité de temps et d'usure sous un écart seuil ; pénalité initialisée par la borne haute mesurée (field.json).
- Retardataires : drapeau bleu, ils cèdent avec une petite perte de temps.
- Dépassement interdit sous VSC (B5.12.2 c) et derrière la SC jusqu'à la ligne de contrôle qui suit la rentrée de la SC (B5.13.2 c), hors exceptions liées aux stands et aux voitures en difficulté.

Mode dépassement (overtakeMode.ts ; règlement B7.2.2, B7.2.3, C5.2.8 ii, C5.2.10 iii)
- Chaque circuit définit une ligne de détection, une ligne d'activation et un écart de détection (calibration ; défaut 1 s, hypothèse).
- Activé à la ligne d'activation si la voiture a passé la ligne de détection à moins de l'écart de détection d'une autre voiture ; désactivé à la ligne d'activation suivante sinon.
- Désactivé avant le départ et la reprise, jusqu'au premier passage du leader sur la ligne de détection ; désactivé sous SC, réactivé quand toutes les voitures ont passé la ligne de contrôle après la rentrée de la SC ; désactivé en conditions de faible adhérence.
- Effet : delta_mode_depassement sur les micro-secteurs des zones d'activation et terme b de la probabilité de dépassement, calibrés sur 2026. Mécanisme réel (pour mémoire, non simulé en énergie) : puissance ERS-K de 350 kW maintenue jusqu'à 337,5 km/h au lieu de 290 km/h, et jusqu'à 0,5 MJ de recharge supplémentaire sur le tour.

Arrêts aux stands
- La voie des stands est un chemin parallèle aux micro-secteurs compris entre l'entrée et la sortie (indices dans le JSON circuit). Temps dans la voie = longueur / vitesse limite + temps d'immobilisation + pertes de décélération et d'accélération. Vitesse limite : 80 km/h (B1.6.3 a), exception par circuit dans le JSON.
- Temps d'immobilisation = minimum + tirage log-logistique par écurie (paramètres de teams.json), retiré tant qu'il dépasse 3 fois la moyenne de la loi (borne du code TUM) ; les arrêts ratés au-delà de cette borne suivent une loi séparée, issue de la calibration.
- Perte au stand = temps dans la voie - temps que la voiture aurait mis sur les micro-secteurs évités dans les conditions du moment. Ce n'est jamais un paramètre direct : sous VSC ou SC, les micro-secteurs évités ralentissent et la perte baisse d'elle-même.
- Test de vraisemblance : sur chaque circuit, les rapports perte VSC sur vert et SC sur vert calculés par la géométrie sont comparés aux plages observées (médianes 0,60 et 0,54 sur 2014 à 2019 ; tableau 6 du Monte-Carlo pour 4 circuits ; valeurs 2023 à 2026 de la calibration). Un écart est signalé, jamais corrigé à la main.
- Sous VSC et sous SC, une voiture n'entre aux stands que pour changer de pneus (B5.12.3, B5.13.3).
- Deux voitures de la même écurie au même tour : la seconde attend.
- Règle des spécifications (B6.3.6) : sauf usage d'intermédiaires ou de pneus pluie, chaque voiture utilise au moins deux spécifications sèches, dont au moins une spécification obligatoire du GP (une ou deux, désignées par GP dans le JSON circuit). Un train compte dès que la voiture sort de la voie avec lui (B6.3.2). Non-respect : disqualification ; si la course est suspendue sans reprise, +30 s au temps.

Safety car et VSC (safetyCar.ts)
- Déclenchés par incidents, débris, crevaisons, voitures immobilisées ou météo, pondérés par les parts de causes calibrées (calibration/export/events.json). Probabilité d'incident selon la zone du circuit.
- Chaînes causales par défaut : un accident déclenche une SC ; une panne déclenche une VSC avec une probabilité p (défaut 0,227, Monte-Carlo, 2015 à 2019) ; débris et météo ont leurs propres taux. En batch, ces chaînes doivent reproduire les lois 2023 à 2026 de events.json : nombre de SC par course, part au premier tour, début par tranches de course, durées de SC et de VSC. Les valeurs 2014 à 2019 (36 % des SC au premier tour, SC de 2 à 8 tours, VSC de 1 à 4 tours) servent de contrôle.
- VSC (B5.12) : toutes les voitures ralenties, écarts conservés ; fin annoncée, retour au vert 10 à 15 s plus tard ; peut se transformer en SC (probabilité paramétrée).
- SC (B5.13) : peloton regroupé en file (écart minimal derrière la SC) en quelques tours ; dédoublement des retardataires sur décision de la direction de course (probabilité paramétrée), la SC rentrant alors à la fin du tour suivant ; relance avec risque d'incident accru.
- Une SC peut être déployée jusqu'à la fin : si elle est en piste au dernier tour, l'arrivée se fait derrière elle, sans dépassement (B5.13.8).
- Rythme sous neutralisation : valeurs par défaut 140 % du temps au tour vert sous VSC et 160 % sous SC (2014 à 2019), remplaçables par la calibration.
- Durées de SC et de VSC tirées dans des distributions séparées issues de la calibration.

Drapeau rouge (redFlag.ts ; règlement B5.14, B5.15, B2.5.3)
- Déclenché par un accident grave ou par une intensité de pluie au-delà d'un seuil, avec les taux et causes de events.json.
- Suspension : dépassement interdit ; toutes les voitures rejoignent la voie rapide des stands et s'y alignent ; ordre de reprise pris au dernier point où toutes les positions étaient connues (B5.15.1 b iii).
- Pendant la suspension : changement de pneus libre et réparation des dégâts d'accident (B5.14.4 a vii et viii). Le joueur et l'IA choisissent un composé pour chaque voiture ; les trains montés comptent pour la règle des spécifications.
- Avant la reprise : les retardataires se dédoublent (B5.15.2 c) ; pneus pluie imposés si la direction de course le décide (B5.15.2 a).
- Reprise derrière la SC, puis départ arrêté ou lancé (B5.15.4, B5.15.5), choix tiré selon les fréquences 2023 à 2026 de events.json ; un départ arrêté passe par le modèle de départ.
- Durée de course : limite de 2 h augmentée de la durée de la suspension, plafond 3 h (B2.5.3).
- Course non reprise : classement à la fin de l'avant-dernier tour précédant le drapeau rouge (B5.14.2).

Fiabilité
- Taux de défaillance par composant (moteur, boîte, hydraulique) et par voiture, majoré par le mode d'attaque ; probabilité de panne par écurie et d'accident par pilote issues de l'inférence Beta-Bernoulli de la calibration. Effet : abandon ou perte de performance.

Départ
- Grille réelle du GP s'il a eu lieu (calibration/export/grids.json), sinon générée (rythme + bruit), au choix du joueur. Risque d'incident accru au premier tour.
- Chaque voiture franchit la ligne au temps t_s(p_g) + N(μ_pilote, σ_pilote²). Courbe de référence t_s = √(2 d(p_g) / a) + t_r du Monte-Carlo (p. 8 : a = 11,2 m/s², t_r = 0,2 s, 8 m entre deux places, origine décalée de 0,8 place), paramètres dans le JSON. Pilote sans données : μ = 0, σ = 0,146 s. Cette courbe remplace le terme t_grid. La règle MGU-K au départ (C5.2.12) est absorbée dans la courbe.
- La gomme module la qualité d'envol et le rythme du premier tour (la plus tendre est la plus adhérente à froid ; hypothèse qualitative, Chain Bear).
- Mode dépassement désactivé jusqu'au premier passage du leader sur la ligne de détection.

## Information
- Écurie du joueur : usure, carburant, état et inventaire de trains exacts.
- Rivaux : composé, âge du relais et nombre d'arrêts visibles ; usure estimée à partir des temps au tour, avec erreur ; carburant et inventaire de trains inconnus.
- L'IA est soumise exactement aux mêmes restrictions. Aucun ajustement de performance pour équilibrer la course.

## IA
- profiles.ts : profil par écurie (prudent, neutre, agressif) qui fixe seuils et tolérance au risque.
- estimator.ts : modèle tour par tour d'une voiture seule, sans interactions, avec pénalité de trafic moyenne. Rapide, volontairement plus simple que la simulation. Accepte une fonction de temps au tour injectée (profil tabulé par âge du pneu), pour les tests de référence.
- planner.ts, avant la course :
  - Programmation dynamique sur les relais. Coût d'un relais = somme des temps au tour estimés pour (composé, longueur, tour de départ), précalculée. État = (tours couverts, ensemble des composés secs déjà utilisés, nombre d'arrêts, trains restants). Exact pour toute fonction de coût de relais, y compris falaise et effet carburant ; l'ordre des relais compte. Contraintes : inventaire de trains et règle des spécifications (B6.3.6).
  - 1 à 3 arrêts en sec. Un arrêt supplémentaire n'est retenu que s'il rapporte au moins un seuil (défaut 2 s, VSE), paramètre du profil.
  - Masse de carburant au départ : pour chaque stratégie candidate, masse minimale pour finir la course au mode prévu, plus une marge fixée par le profil (valeur par défaut marquée hypothèse), dans la limite de la capacité du réservoir. Option : recherche sur une grille de masses (éq. 8 de Carrasco Heine et Thraves 2023). Le joueur reçoit la masse proposée avec chaque plan.
  - Les meilleures stratégies de chaque nombre d'arrêts sont ensuite évaluées sur K tirages météo et neutralisations avec l'estimateur, classées selon le profil, avec un léger aléa pour éviter des stratégies identiques.
  - Sortie : trois plans (A, B, C). Le plan C est toujours une option de relais long, avec un arrêt nettement plus tardif que le plan A, même si l'estimateur la classe moins bien (Aversa et al. 2018 : l'option gagnante manquait à l'outil de Ferrari à Abu Dhabi 2010). Le joueur reçoit les mêmes trois plans pour ses voitures. Relancé sur événement majeur (pluie, SC, drapeau rouge, dégâts).
  - Pas de programmation dynamique stochastique complète en v1 : dans Carrasco Heine et Thraves 2023 (tableau 1), elle ne gagne en moyenne qu'environ 1 s sur une DP résolue à nouveau à chaque neutralisation, ce que fait déjà le planificateur. L'effet d'anticipation passe par la règle « attente de SC ».
- reactive.ts, à chaque tour, avec au minimum les signaux suivants (VSE) : progression de la course ; progression de l'âge du pneu ; leader ou poursuivant ; composé relatif ; sévérité du circuit ; statut de neutralisation (aucune, premier tour de VSC, VSC en cours, premier tour de SC, SC en cours, drapeau rouge) ; arrêts restants au plan ; poursuivant qui vient de s'arrêter ; poursuivant à moins de 1,5 s ; trains restants.
- Règles de reactive.ts :
  - arrêt si falaise imminente ;
  - neutralisation : décision au premier tour de VSC ou SC ; arrêt si le gain estimé dépasse le seuil du profil et qu'un arrêt reste au plan ; pas d'arrêt si les pneus sont encore frais (seuil d'âge issu de behaviour.json) ; le leader tient compte du fait que ses poursuivants peuvent s'arrêter au même tour ; fenêtre d'arrêt : s'arrêter si l'arrêt prévu tombe dans les N prochains tours (N issu de behaviour.json ; défaut 12, Phillips 2014) ;
  - drapeau rouge : choix du composé à monter pendant la suspension, en tenant compte de la règle des spécifications et des trains restants ;
  - couverture d'undercut : si le poursuivant à moins de 1,5 s vient de s'arrêter et que l'arrêt prévu est dans la fenêtre, s'arrêter maintenant, sauf si la sortie projetée tombe dans un groupe que la voiture ne pourra pas dépasser : la règle d'air libre prime (cas Ferrari, Abu Dhabi 2010) ;
  - undercut offensif si la voiture devant est dans la fenêtre de perte au stand et que le gain de pneus neufs le permet ;
  - air libre : avant un arrêt, calcule la sortie projetée (écart au leader + perte au stand courante). Si elle tombe dans un groupe serré que la voiture ne pourra pas dépasser, retarde l'arrêt tant que l'usure le permet ;
  - attente de SC : prolonge un relais si le gain espéré (risque de SC sur les tours restants × gain d'un arrêt sous SC) dépasse la perte due à l'usure ; seuil selon le profil ;
  - changement slicks, intermédiaires ou pluie quand l'humidité du secteur le plus mouillé franchit le point de croisement, avec hystérésis ;
  - économie de carburant si la projection est insuffisante ; consignes d'équipe ;
  - bascule entre plans A, B et C sur événement.

## Prédicteur du joueur
- predictor.worker.ts clone l'état connu du joueur et fait tourner la simulation complète jusqu'à l'arrivée, N fois par stratégie candidate (N réglable, défaut 200), avec nombres aléatoires communs entre candidates.
- Le prédicteur part de l'état connu du joueur, pas de l'état réel : usure des rivaux estimée, carburant et inventaire de trains des rivaux tirés dans une loi plausible, événements futurs tirés. Sinon il révèle des informations cachées.
- Sortie : distribution de la position et du temps d'arrivée pour chaque candidate, avec l'intervalle de confiance à 95 % de la position moyenne. Ordre de grandeur (Monte-Carlo, tableau 8) : ± 0,31 place avec 100 tirages, ± 0,08 avec 1 000 ; avec N = 200, environ ± 0,2 (extrapolation, hypothèse). Les nombres aléatoires communs réduisent l'incertitude sur l'écart entre candidates : à mesurer.
- Mesure le temps de calcul et remonte-le ; ne simplifie pas le modèle pour tenir une cible sans mon accord.
- Contrôle de qualité (lot 7) : sur un batch de courses à graines fixées, à 25 %, 50 % et 75 % de la course, comparer la position finale prévue pour chaque voiture du joueur (moyenne sur N tirages) à la position obtenue par la simulation complète. Le prédicteur doit faire mieux, en RMSE et en exactitude de signe (gain, perte, stable), que deux références triviales : position actuelle conservée ; position moyenne depuis le départ. Rapporter les trois scores (méthode de Tulabandhula et Rudin 2014 et de Choo 2015).

## Instantanés (contrat avec l'UI)
Les vues finales seront conçues plus tard. Le moteur expose dès maintenant, dans chaque instantané :
- par voiture : position, distance sur le tour, écart au leader en temps (continu), intervalle avec la voiture devant, gomme, âge du pneu, usure (exacte pour le joueur, estimée pour les rivaux), carburant projeté (joueur seulement), mode, état du mode dépassement, statut (piste, stands, voie rapide pendant un drapeau rouge, abandon, disqualifié) ;
- pour chaque voiture du joueur : inventaire de trains, spécifications déjà utilisées ;
- temps au tour de référence ;
- perte au stand courante pour les régimes vert, VSC et SC ;
- pour chaque voiture du joueur : sortie projetée si elle s'arrête maintenant (écart au leader, position, voitures à moins de N s devant et derrière) ;
- pluie et humidité par secteur officiel ; conditions de faible adhérence ;
- dernière image radar et prévision (pas de temps et horizon paramétrables) ;
- statut de course (vert, jaune, VSC, SC, rouge) et, pendant un drapeau rouge, ordre de reprise et temps restant avant la reprise ;
- profil de temps au tour estimé par gomme et âge du pneu ;
- historique des écarts au leader, tour par tour ;
- plans A, B et C de chaque voiture du joueur, avec la masse de carburant proposée.

## UI
- Lot 6 : UI fonctionnelle minimale. La boucle d'animation demande au worker d'avancer jusqu'à t_cible = horloge * vitesse ; le worker renvoie des instantanés à environ 10 Hz ; l'UI interpole. Contrôle du temps (pause, x1, x2, x4, x8, x16, saut au prochain événement), longueur de course (25 %, 50 %, 100 %), carte simple, tour de chronométrage (bascule écart au leader et intervalle), ordres du joueur (dont choix de pneus pendant un drapeau rouge), écran de fin. Aucun travail de style.
- Lot 9 : vues stratégiques d'après des maquettes que je fournirai : cercle des écarts (tour vu comme un cercle, arcs de perte au stand vert, VSC et SC, sortie projetée), carte avec humidité par secteur, radar avec curseur temporel, planificateur de relais (profil de temps au tour par gomme, arrêt déplaçable, total, seuil où deux arrêts deviennent gagnants), graphe des écarts, courbes de croisement par gomme.

## Données
- Un fichier par circuit du calendrier 2026, depuis calibration/export/circuits/<circuit>.json : longueur, géométrie 2D réelle, micro-secteurs (alignés sur les secteurs de commissaires quand l'export les fournit ; poids, type, dans une zone de dépassement ou non, position 2D, probabilité d'incident), secteurs officiels (micro-secteurs contenus, coefficient de drainage), zones de dépassement, zones d'activation de l'aileron actif, lignes de détection et d'activation et écart de détection du mode dépassement, voie des stands (géométrie, indices d'entrée et de sortie, longueur, vitesse limite), abrasivité, T_ref, gommes nommées et spécifications obligatoires pour le GP, climat.
- Écuries et pilotes 2026 réels, depuis calibration/export/teams.json et drivers.json. Écurie : nom, couleur, delta voiture (forme récente, par GP), fiabilité, efficacité carburant, vitesse de pointe (proxy), loi d'immobilisation. Pilote : nom, code, rythme, régularité (sigma), gestion des pneus, envol (μ, σ), pluie, attaque, défense, taux d'erreur.
- Grilles et inventaires de trains depuis calibration/export/grids.json.
- Scénarios météo par circuit, depuis calibration/export/weather.json.
- Tous les paramètres numériques dans les JSON, validés par zod au chargement. Aucune constante de modèle en dur dans le code.
- Valeurs lues depuis calibration/export/ (circuits/, teams.json, drivers.json, grids.json, compounds.json, field.json, events.json, behaviour.json, weather.json) ; fichier absent : valeurs provisoires marquées comme telles. k_fuel et la consommation par tour sont partagés avec la configuration de calibration.
- Dans les schémas zod, tout paramètre numérique peut porter sa provenance { method, source } ; une valeur sans provenance est traitée comme hypothèse. Les attributs que les données ne permettent pas d'estimer restent des hypothèses visibles comme telles dans l'UI de débogage.
- rules.json : chaque règle tirée du règlement FIA 2026 (docs/reglement/, sections B et C) porte sa référence d'article. Liste de départ : synthèse, section 6 (B1.6.3, B1.9.5, B1.9.6, B2.5.2, B2.5.3, B2.5.5, B5.12, B5.13, B5.14, B5.15, B6.1.2, B6.2.4, B6.3.2, B6.3.6, B6.3.7, B7.1, B7.2, C5.2.3, C5.2.8, C5.2.10). Règle introuvable : marquée manquante, jamais inventée.

## Outillage et tests
- CLI : run-race (une course, résumé texte), batch (N courses sans UI vers CSV : positions, arrêts, dépassements, abandons, SC, VSC, drapeaux rouges, écarts), replay (graine + journal d'ordres vers résultat identique).
- Tests obligatoires : déterminisme ; indépendance des flux RNG (modifier un arrêt ne change ni la météo ni les incidents des autres voitures) ; monotonie de f_usure et existence de la falaise ; panne sèche ; règle des spécifications (spécification obligatoire, disqualification, +30 s si course suspendue sans reprise) ; inventaire de trains (impossible de monter un composé épuisé) ; regroupement sous SC ; conservation des écarts sous VSC ; arrêt sous VSC ou SC seulement pour changer de pneus ; arrivée derrière la SC au dernier tour ; drapeau rouge (ordre de reprise, changement de pneus libre compté pour la règle des spécifications, dédoublement, durée maximale) ; mode dépassement (activation sous l'écart de détection, désactivation au départ, sous SC et en faible adhérence) ; hystérésis météo de l'IA ; application des ordres à la bonne frontière.
- Cas de référence (modèles en blocs, estimateur seul, sans carburant ni aléa, deux composés obligatoires) :
  - 10 tours ; tendre 3 blocs par tour, 4 tours maximum ; médium 4 blocs par tour. Un arrêt optimal : 4 tendre + 6 médium = 36 + P. Deux arrêts : 4 + 4 tendre + 2 médium = 32 + 2P. Égalité à P = 4.
  - 20 tours ; profil tendre par âge 3,3,3,4,4,5,5,6,6,7,7,8,8,9,9 (15 tours maximum) ; profil médium 4,4,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9. Un arrêt optimal : 9 tendre + 11 médium = 92 + P. Deux arrêts tendre, tendre, médium : minimum 79 + 2P, atteint par 5-7-8, 6-6-8, 6-7-7 et 7-7-6 (relais tendres non ordonnés). Deux arrêts meilleurs si P < 13.
  - Course de 55 tours, dégradation linéaire t = k0 + k1 * âge, dur (1,2 s ; 0,016 s/tour), médium (0,5 s ; 0,05 s/tour), tendre (0 s ; 0,09 s/tour), départ en tendre avec 2 tours d'âge : le planificateur retrouve l'optimum d'une énumération exhaustive (VSE, tableau 8 : tendre 22 tours + médium 33 tours, et tendre 18 tours + dur 37 tours pour ces deux combinaisons).
  - Carburant seul (forme fermée du document McLaren, éq. 7, sans ravitaillement) : relais de n tours sans usure, sans aléa ni interaction, masse m0 au départ, consommation c par tour répartie uniformément sur le tour. Temps du relais = n × t0 + k_carbu × (m0 × n − c × n² / 2). Tolérance : écart dû à la consommation par micro-secteur, de l'ordre de k_carbu × c × n / (2 × nombre de micro-secteurs) pour des micro-secteurs de même durée.
- Sensibilité au couplage usure-masse : sur les circuits 2026, optimum du planificateur pour δ = 0, 0,1 et 0,2. S'il ne change pas, l'ordre des relais ne compte pas en pratique : le rapporter.
- Propriété de l'IA : sur un circuit de test, à paramètres identiques, l'âge moyen au premier arrêt sous vert ne diminue pas quand la probabilité de SC augmente (retard prédit par Carrasco Heine et Thraves 2023, p. 259 et fig. 5). Mesurer aussi le gain moyen de la règle « attente de SC » contre la même IA sans cette règle ; ordre de grandeur attendu d'environ 1 s (hypothèse : leur instance est synthétique et sans rivaux).
- Perte au stand qui baisse sous VSC puis sous SC sur un circuit de test, sans paramètre dédié.
- Météo : une cellule qui traverse le circuit mouille les secteurs officiels dans l'ordre de son passage ; la prévision se trompe quand une cellule naît hors du champ observé.
- Mesure et affiche la durée d'un batch de 1 000 courses complètes (20 voitures, 60 tours).

## Lots
1. Dépôt git et .gitignore, squelette, schémas de données, RNG, file d'événements, temps au tour sans interactions, carburant, pneus secs, inventaire de trains, règle des spécifications, arrêts planifiés fixes, CLI run-race et batch, tests de déterminisme.
2. Interactions : dépassements, air sale, mode dépassement, retardataires, contacts, départ.
3. SC, VSC, drapeau rouge, fiabilité, crevaisons.
4. Météo spatiale : cellules, vent, humidité par secteur officiel, drainage, faible adhérence, radar et prévision, intermédiaires et pluie.
5. IA : estimateur, planificateur, réactions, profils, cas de référence, test de sensibilité δ.
6. UI fonctionnelle minimale (voir section UI).
7. Prédicteur Monte-Carlo dans l'UI, contrôle de qualité.
8. Calibration : batch comparé à calibration/export/targets.json et behaviour.json, rapport des écarts par cible, en comptant les dépassements comme le pipeline (en piste, hors tour 1, arrêts, SC, VSC, drapeau rouge et relances). Cibles : nombre de SC par course, part des SC au premier tour, durées de SC et de VSC, drapeaux rouges par course, dispersion des immobilisations, changements de position au premier tour, arrêts sous neutralisation croisés avec la sévérité du circuit, la position et l'âge du pneu, âge au premier arrêt sous vert selon la probabilité de SC. Réglage de difficulté_circuit par une courbe « dépassements par course en fonction de la difficulté », comme Phillips 2014 pour son seuil de dépassement.
9. Vues stratégiques d'après maquettes.

## Hors périmètre
Qualifications, réglages de voiture, saison, gestion d'écurie, gestion de l'énergie distincte du mode de pilotage (limite connue : boost et recharge non décidés séparément ; seul le mode dépassement est explicite), température des pneus, pénalités autres que la règle des spécifications, multijoueur, 3D, son, sauvegarde en cours de course (hors replay), IA à réseaux de neurones ou à recherche arborescente (option après la v1 : MCTS par tour sur l'estimateur, sans réseau, d'après Liu et Fotouhi 2020), correction en course des hypothèses du prédicteur par le joueur (reportée à la phase game design), règlement 2027.
