# Veille bibliographique sur la stratégie de course

Lot documentaire du 20/10/2026, sans code. Sources tirées de la bibliographie de Heilmeier et al. 2020 (Virtual Strategy Engineer) et du tri d'Antoine. Relecture de vérification le 20/10/2026 après-midi : Fieni, Cappello, Liu et Aversa relus en texte intégral ; Tulabandhula et Rudin, Choo, le document McLaren, Carrasco Heine et Thraves, et Dinh et al. lus en texte intégral sur les PDF fournis par Antoine. Bekker et Lotz 2009 : introuvable, abandonné. Ajouts du 20/10 en fin d'après-midi : le VSE (lu le 19/10, jusque-là absent du tableau), l'article McLaren sur la SC listé dans le document de sources d'Antoine, et une ligne « Bibliographie » pour chaque source.

Mentions :
- « (code) » : valeur lue dans un dépôt ;
- « (déduit) » : calcul de ma part ;
- « (estimé) » : lecture sur un graphique ;
- « lecture indirecte » : texte lu au travers de l'outil de lecture web, qui renvoie un résumé et non le document entier. Les valeurs issues d'une lecture indirecte sont à recontrôler sur le document avant tout usage chiffré ;
- « texte intégral » : document lu en entier (page HTML complète ou PDF).

## Synthèse

| Source | Accès | Licence | Apport pour F1STRAT | Action proposée | Priorité |
| --- | --- | --- | --- | --- | --- |
| Heilmeier, Thomaser, Graf, Betz 2020, Appl. Sci. 10(21) 7805 (Virtual Strategy Engineer) | PDF fourni par Antoine, texte intégral (19/10/2026) | CC BY 4.0 ; code LGPL-3.0 ; base de chronométrage CC BY-NC-SA 3.0 | entrées de la décision d'arrêt, cibles de comportement, cas de référence ; sa bibliographie est l'origine de la veille | déjà intégré aux prompts le 19/10 ; notes_vse_heilmeier_2020.md | 1 |
| Heilmeier, Graf, Betz, Lienkamp 2020, Appl. Sci. 10(12) 4229 (Monte-Carlo) | PDF fourni par Antoine, lu en entier (site de l'éditeur bloqué depuis mon environnement) | article CC BY 4.0 ; code LGPL-3.0 | lois des SC, VSC, accidents, pannes, immobilisations, envol, bruit ; perte au stand par régime | notes_montecarlo_heilmeier_2020.md ; amendements ci-dessous | 1 |
| Heilmeier, Graf, Lienkamp 2018, ITSC, p. 2986 à 2993 | PDF fourni par Antoine, texte intégral (8 p.) ; code race-simulation relu en complément | article © 2018 IEEE (copie sous licence IEEE Xplore, usage personnel) ; code LGPL-3.0 | modèle de temps au tour et de dépassement ; critique des modèles par secteurs ; valeurs par circuit (121 courses, code) | calibrer la difficulté de dépassement ; pertes de duel ; vitesse de pointe ; zones de dépassement sur plusieurs micro-secteurs | 1 |
| Fieni, Wüthrich, Neumann, Moradi, Onder 2025, arXiv:2512.21570 | arXiv, texte intégral (HTML) | licence de diffusion non exclusive d'arXiv 1.0 (pas de Creative Commons) | usure dynamique dépendant de la masse ; RL (SAC) à 5 s de l'optimum ; ni SC ni trafic ; bibliographie récente (programmation dynamique des arrêts) | conforte l'usure liée au carburant ; pistes nouvelles ci-dessous | 2 |
| Bonomi, Turri, Iacca 2023, GECCO '23 Companion (réf. [9] de Fieni) | article : lecture indirecte, la copie ouverte (IRIS, Trento) est désormais derrière une vérification anti-robots ; dépôt cloné et inventorié | article : tous droits réservés (ACM) ; dépôt GPL-3.0 | données d'usure du jeu vidéo F1 2021, 6 circuits ; données Pirelli non publiques | ne pas utiliser pour compounds.json | 2 |
| Cappello, Hoegh 2025, arXiv:2512.00640 | arXiv, texte intégral (HTML) | CC BY 4.0 (vérifié sur la page arXiv) | modèle d'état bayésien, 1 pilote, 1 course, Stan | contrôle optionnel de fit_pace.py, sans Stan | 3 |
| Liu, Fotouhi 2020, Neural Comput. Appl. 32, 15191 à 15207 | Springer en accès ouvert, texte intégral (HTML) | CC BY 4.0 (vérifié sur la page Springer et le dépôt Cranfield) | substitut rapide + MCTS par tour ; réaction à une SC | option d'IA après la v1, sans réseau | 3 (après v1) |
| Choo 2015, mémoire de master du MIT (100 p.) | PDF fourni par Antoine, texte intégral ; version publique caviardée (série et circuits anonymisés, variables non décrites) | © 2015 l'auteur, tous droits réservés ; diffusion accordée au MIT | NASCAR 2012 à 2014 ; décisions d'arrêt sous caution selon l'usure du circuit, la position et l'âge des pneus ; rien de chiffré sur les cautions ; plusieurs conclusions fragiles | deux cibles de comportement à mesurer sur F1 ; référence « rang conservé » | 3 |
| Tulabandhula, Rudin 2014, Big Data 2(2), 97 à 112 | PDF du dépôt MIT fourni par Antoine, texte intégral | CC BY 3.0 États-Unis (vérifié p. 112) | NASCAR 2012 ; paradoxe de Simpson sur les choix de pneus ; rang artificiel pendant un cycle d'arrêts ; références triviales du prédicteur | ajustement par effet pilote dans la calibration ; contrôle du prédicteur contre deux références triviales | 2 |
| McLaren Racing, « Formula One Race Strategy », Royal Academy of Engineering (réf. [9] de l'ITSC 2018) | PDF fourni par Antoine, texte intégral (7 p., 2009) | aucune licence indiquée ; usage personnel | exercice pédagogique de l'ère du ravitaillement : effet du carburant en forme fermée, tour d'arrêt optimal | cas de référence analytique pour le terme carburant | 3 |
| Carrasco Heine, Thraves 2023, Cent. Eur. J. Oper. Res. 31(1), 239 à 268 | PDF fourni par Antoine, texte intégral ; code F1DP cloné et lu | article : licence exclusive Springer, usage personnel ; code MIT | DP par tour et DP stochastique (jaunes, météo) ; la version stochastique retarde les arrêts, pour un gain moyen de l'ordre de 1 s ; usure liée à la masse | conforte notre DP par relais ; masse de départ choisie par le planificateur ; contrôles de l'attente de SC | 2 |
| Dinh, Tran, Reichert, Ametsbichler 2026, prépublication SSRN 6271405 | PDF fourni par Antoine, texte intégral | aucune licence indiquée ; non relu par des pairs | classification des tours d'arrêt sur FastF1 2022 à 2025 ; fuite d'information probable | une règle de mesure pour les comportements (état connu avant la décision) ; deux pistes | 3 |
| McLaren Racing, « Making the right call » (page web, propos de Randeep Singh) | lecture indirecte (20/10/2026) | © McLaren, usage personnel | méthode d'une écurie pour la probabilité de SC par GP | taux de SC séparés entre courses sèches et humides, causes exceptionnelles exclues | 3 |
| Aversa, Cabantous, Haefliger 2018, J. Strateg. Inf. Syst. 27, 221 à 236 | manuscrit accepté (City, University of London), texte intégral (PDF, 35 p.) | manuscrit CC BY-NC-ND 4.0 | Abu Dhabi 2010 : échec d'un outil d'aide à la décision | règles d'IA et du prédicteur | 2 |

## Points établis, source par source

### 1. Heilmeier et al. 2020, Monte-Carlo
Voir notes_montecarlo_heilmeier_2020.md. Le code est publié (p. 18) et ses paramètres coïncident avec les tableaux, à deux écuries près.
- Bibliographie (13 réf., p. 20 et 21) : l'ITSC 2018 (section 2), Bekker et Lotz 2009 (abandonné), Phillips 2014 (section 10) ; deux pistes nouvelles, Sulsters 2018 et Salminen 2019 (section « Pistes ») ; le reste porte sur des données (Ergast, RaceFans, F1 TV) ou des outils (scipy, méthodes de tirage aléatoire).

### 2. Heilmeier, Graf, Lienkamp 2018, ITSC
Article lu en entier (PDF fourni par Antoine). Pages = pagination des actes (2986 à 2993). Le code TUMFTM/race-simulation et ses 121 fichiers de paramètres 2014 à 2019 complètent l'article ; le code est postérieur et a fait évoluer certains choix (voir « Écarts article et code »).

Article (établi) :
- Modèle de temps au tour (éq. 2, p. 2988) : t_lap = t_base + t_tire(âge, gomme) + t_fuel + t_car + t_driver + t_grid + t_pit,inlap/outlap. t_base = meilleur tour de qualification + écart au rythme de course, ce dernier mesuré en essais libres (éq. 3).
- Pneus (éq. 4 et 5, p. 2988) : modèle logarithmique t = log(âge × k1 + 1) × k2 + k3, jugé plus fidèle que le quadratique de Phillips sur la plage utile ; modèle linéaire âge × k2 + k3 quand les données sont rares. Paramètres par pilote ou au moins par écurie, ajustés sur les temps corrigés du carburant (essais, qualifications, courses précédentes).
- Carburant (éq. 6 et 7, p. 2988 et 2989) : environ 100 kg consommés par course en F1 à l'époque ; perte = masse restante × sensibilité de masse. L'effet du carburant sur l'usure des pneus est explicitement ignoré.
- Départ (éq. 8, p. 2989) : t_grid = p_grid × t_perGridPos + t_firstlap.
- Arrêts (éq. 9, p. 2989) : t_pit,outlap = roulage dans la voie + immobilisation + pénalité éventuelle (5 ou 10 s) ; vitesse limite de 80 km/h. Les voitures qui s'arrêtent reçoivent un temps de course temporaire pour être reclassées dès le début du tour (figure 5) ; doubler dans la voie des stands se fait sans perte de temps.
- Dépassement (p. 2989 et 2990, figure 6) :
  - DRS : réduction t_DRSeffect du temps du suiveur s'il est à moins de 1 s après les deux premiers tours ;
  - le suiveur passe si son avance en temps de course atteint t_gap,overtake, mesure de la facilité de dépasser sur le circuit (exemple : 1,2 s d'avance sur un circuit à 0,9 s suffit) ;
  - matrice de consignes d'équipe qui modifie ce seuil entre coéquipiers (tableau I : −0,1 s et 0,15 s) ;
  - l'aspiration n'est pas modélisée ;
  - en cas de dépassement, les deux voitures perdent du temps (t_overtake,win et t_overtake,lose, éq. 11), ce qui rend possibles les dépassements multiples ;
  - sinon, l'écart minimal t_gap,front est imposé, y compris après les arrêts.
- Critique des modèles antérieurs (p. 2987) :
  - Bekker découpe la piste en environ 40 secteurs de 150 m, chacun à paramétrer (impossible avec des données publiques) ; le dépassement doit se terminer dans un seul secteur, donc les dépassements dans les longues lignes droites sont mal simulés ; le seuil de dépassement par secteur est difficile à régler ; une seule voiture peut dépasser à la fois ;
  - Phillips ne contrôle l'écart minimal qu'en fin de tour, pas après les arrêts ; seule la voiture dépassée perd du temps ; pénalité de carburant constante par tour.
- Valeurs d'exemple du tableau II (GP d'Abu Dhabi 2017, p. 2991) : t_gap,racepace 3,67 s ; sensibilité de masse 0,033 s/kg ; perte au tour d'entrée 2,0 s ; roulage au tour de sortie 18,5 s ; t_perGridPos « 1,0 s/pos » (dix fois les valeurs du code, voir plus bas : valeur d'exemple ou coquille, non tranché) ; t_firstlap 2,5 s ; t_gap,overtake 1,0 s ; t_DRSeffect −0,8 s ; carburant 100 kg, 1,79 kg/tour ; immobilisation 3,0 s ; t_gap,front 0,95 s ; t_overtake,win 0,1 s ; t_overtake,lose 0,6 s ; fenêtre DRS 1,0 s.
- Tableau III (p. 2991) : pentes de dégradation linéaires de 0,013 à 0,050 s/tour selon pilote et gomme ; décalage du supertendre de 0,127 à 0,900 s ; t_car de 0 à 0,370 s ; t_driver de 0 à 0,637 s.
- Résultats (p. 2990 et 2991) : 1 à 2 s par course en Python (i7 2,7 GHz) ; écart de durée de course de −4,1 à +1,6 s sur les 6 pilotes simulés (tableau IV) ; écarts moyens des temps au tour simulés de −1,06 à +0,73 s, écarts-types de 0,63 à 1,09 s.
- Limites reconnues (p. 2992) : consommation constante par tour ; style de pilotage non représenté ; pas de SC ; pas de prise de tour (effet jugé négligeable).

Écarts article et code (le code est postérieur) :
- Pertes de dépassement : article 0,1 s au gagnant et 0,6 s au perdant ; code 0,3 s aux deux voitures dès qu'elles sont à moins de l'écart minimal, plus 0,3 s au perdant.
- Écart minimal : 0,95 s dans l'exemple de l'article ; 0,5 s dans le code (0,8 s derrière la SC).
- Départ : p_grid × t_perGridPos dans l'article ; (p_grid − 1) × t_loss_pergridpos dans le code, avec 0,113 à 0,188 s par place.

Temps au tour (code) :
- t_q + t_gap_racepace : meilleur tour de qualification + écart au rythme de course ;
- + t_car + t_driver ;
- + dégradation (modèles linéaire, quadratique, cubique ou logarithmique disponibles ; linéaire dans les 121 fichiers) + 1,0 s au premier tour d'un relais (pneus froids) ;
- + masse de carburant × t_lap_sens_mass ;
- + N(0, σ²) si les effets aléatoires sont actifs ;
- premier tour : + t_loss_firstlap + (p_g − 1) × t_loss_pergridpos + envol ;
- DRS : moitié de l'effet selon l'écart en fin de tour précédent, moitié selon l'écart après le traitement des sorties de stand.

Dépassement (race.py, fonction __handle_overtaking_track) :
- Test en fin de tour, de l'avant vers l'arrière, répété tant qu'une position change (plusieurs dépassements possibles dans un tour, 20 itérations au plus).
- Interdit sous SC, et sous VSC si elle couvre au moins la moitié du tour.
- Le suiveur passe si son temps de course projeté devance celui de la voiture de devant d'au moins t_gap_overtake + t_gap_overtake_vel × (v_max suiveur − v_max devant) + consigne d'équipe. v_max est la vitesse maximale en qualification, en km/h.
- Sinon, s'il est plus près que min_t_dist, il est recalé à min_t_dist derrière.
- Duel : + t_duel aux deux voitures quand elles sont à moins de min_t_dist ; + t_overtake_loser à la voiture dépassée.
- Positions après les arrêts : simple tri sur le temps de course, sans duel (fonction __check_pos_changes_wo_timeloss).

Valeurs, 121 courses 2014 à 2019 (code) :

| Paramètre | Valeur |
| --- | --- |
| min_t_dist (vert) | 0,5 s partout |
| min_t_dist_sc (derrière la SC) | 0,8 s partout |
| t_duel, t_overtake_loser | 0,3 s partout |
| t_gap_overtake | 1,26 à 3,75 s, médiane 2,03 s ; 2019 : Monaco 3,75, Singapour 3,75, Budapest 2,42, Spielberg 2,01, Monza 1,75, Sakhir 1,38, Silverstone 1,35 |
| t_gap_overtake_vel | −0,061 à −0,009 s par km/h, médiane −0,034 |
| Fenêtre DRS | 1,0 s ; activable à partir du tour 3 ; désactivé 2 tours après une SC |
| Effet DRS par tour | −0,13 à −0,92 s, médiane −0,50 |
| t_loss_pergridpos | 0,113 à 0,188 s par place, médiane 0,139 |
| t_loss_firstlap | 0,43 à 8,22 s, médiane 3,82 |
| t_teamorder | 0 partout |

Comparaison avec prompt_jeu.md :
- Notre modèle est probabiliste, par micro-secteur, en sigmoïde. Le leur est déterministe, en fin de tour, avec un seuil propre au circuit.
- Leur seuil donne un ordre de grandeur pour initialiser notre difficulté de dépassement par circuit. Il ne convient pas à 2026 sans recalage : aide au dépassement différente, voitures différentes.
- Ce qui nous manque : la vitesse de pointe, et les pertes de duel pour les deux voitures.
- Risque à traiter (déduit de la critique de Bekker, p. 2987) : notre test de dépassement par micro-secteur hérite du défaut du modèle par secteurs si une tentative doit aboutir dans un seul micro-secteur. Une zone de dépassement doit pouvoir couvrir plusieurs micro-secteurs (ligne droite plus freinage), et la difficulté doit rester un paramètre par circuit, pas par micro-secteur, faute de données publiques pour la régler finement.

### 3. Fieni et al. 2025 (texte intégral)
- Usure (section 2.4, éq. 25 à 27) : TW[k+1] = a_j TW[k] + b_j (m_car[k] / m_car[0]) + c_j, remis à 0 à chaque arrêt, avec des coefficients par composé et par circuit, non publiés. b_j est choisi de façon heuristique « faute de données dans la littérature ».
- Correction du temps au tour (section 2.5.2, figure 4) : fonction de l'usure par composé, avec des données seulement jusqu'à TW = 0,6, prolongée artificiellement jusqu'à 1. Pas de données pour le médium, déduit de façon heuristique du tendre et du dur (section 1.1.1).
- Ordres de grandeur simulés (section 2.5.2, figure 5) : dur neuf +2 s par tour par rapport au tendre neuf ; le dur devient payant après 18 tours.
- Circuit du cas d'étude : Bahreïn (section 5.1).
- Course : contrôle de l'énergie de la batterie et du carburant, plus la décision d'arrêt ; durée d'arrêt déterministe, valeur non donnée (section 2.5). Ni SC ni trafic. Voie des stands limitée à 80 km/h (section 2.5.1). Tableau 1 : tour nominal 93,1 s, tour d'entrée 104,6 s, tour de sortie 108,2 s, soit +11,5 s et +15,1 s (déduit).
- Méthodes :
  - MINLP (CasADi, BONMIN) : 50 s à 5 min sur un portable (Apple M2 Max), section 3.3 ;
  - apprentissage par renforcement (SAC, environ 4 h d'entraînement, section 4.7) : moins de 1 s par décision ;
  - cas nominal : stratégie (M0, M18, S39) identique à l'optimum, écart 4,96 s soit 0,09 % du temps de course, dû à la gestion d'énergie (section 5.1, tableau 3 : 55 s contre moins de 1 s) ;
  - usure brusquement accrue au tour 22 : optimum recalculé (M0, M18, S34) en 68 s ; agent (M0, M18, S33) à 5,08 s ; « go long » sur dur (M0, M18, H24) à 31,45 s (section 5.2, tableau 4).
- Pas de code publié.
- Pour F1STRAT : l'usure qui dépend de la masse conforte notre facteur(masse_carburant). Le reste porte sur la gestion d'énergie, hors périmètre.
- Bibliographie (30 réf.) : Bekker et Lotz [3] (abandonné) ; sources TUM déjà traitées ([4] à [6]) ; Bonomi [9] (section 3 bis) ; Carrasco Heine et Thraves [10] (section 12) ; Liu et Fotouhi [16] (section 5) ; pistes [7], [11], [12] et [15] (section « Pistes »). Écartées : règlements FIA 2025 ([1], [2], remplacés par le règlement 2026), gestion d'énergie ([8], ERS hors périmètre), endurance électrique ([13], [14]), Formula E par apprentissage par renforcement ([17], même famille que Liu et Fotouhi 2020), modèles physiques d'usure et commande optimale du pneu ([18] à [26], trop fins pour un modèle par tour), outils ([27] à [30]).

### 3 bis. Dépôt de Bonomi, Turri, Iacca (référence [9] de Fieni)
- Référence exacte : Bonomi, Turri, Iacca, « Evolutionary F1 Race Strategy », GECCO '23 Companion, ACM, p. 1925 à 1932, DOI 10.1145/3583133.3596349.
- Dépôt : github.com/bonom/Evolutionary-F1-Race-Strategy, licence GPL-3.0, dernier commit le 22/08/2023, 9 Mo (inventorié par clonage).
- Contenu :
  - 6 circuits : Bahrain, Montreal, Monza, Portimao, Spielberg, Zandvoort ;
  - FullData.csv, 284 lignes au total (code) : Lap, LapTime, DRS, Fuel, Compound et usure de chaque roue (FLWear, FRWear, RLWear, RRWear) ;
  - scénarios météo en texte ;
  - journaux d'une recherche exhaustive.
- Origine : télémétrie du jeu vidéo F1 2021 (lecture indirecte de l'article). Les paramètres Pirelli de 7 circuits 2021 ont servi à l'évaluation, mais l'article indique qu'ils ne sont pas publics.
- Sécurité : les fichiers Car.json, Data.json et RaceData.json ne sont pas du JSON mais des pickles Python. Je ne les ai pas ouverts, car charger un pickle exécute du code.
- Le code dérive les coefficients du médium de ses voisins par des facteurs fixes (35/40 et 40/35 dans classes/Car.py), ce qui rejoint le manque de données signalé par Fieni.
- Modèle d'usure de l'article : linéaire, delta + dégradation × tour (lecture indirecte). Sensibilité au carburant : environ 0,03 s/kg sur les données du jeu ; pour les données réelles, l'outil de lecture rapporte 0,3 s/kg. Non vérifiable : la copie ouverte de l'article est désormais derrière une vérification anti-robots, et le code ne contient aucune de ces deux constantes (il estime l'effet du carburant sur les données du jeu, classes/Car.py, lignes 90 et 284 à 285). Sans conséquence pour F1STRAT, qui ne reprend pas cette valeur.
- Verdict : non réutilisable pour compounds.json (jeu vidéo, saison 2021, usure en pourcentage par roue, très petit échantillon).

### 4. Cappello, Hoegh 2025 (texte intégral)
- Modèle (section 3.2) :
  - observation : y_t = α_t + γ × carburant_t + ε_t ;
  - état : α_{t+1} = α_t + ν (dégradation linéaire), remis à α_reset à chaque arrêt, plus un bruit ;
  - extensions (section 3.3) : ν par composé, ν croissant dans le temps (incrément β par composé), erreurs en t asymétrique à 2 degrés de liberté.
- A priori (section 3.4) : écarts-types de 0,1, jugés « modérément informatifs » ; α_reset centré sur 69 s d'après un long relais de Leclerc en essais libres.
- Carburant : 110 kg au départ décroissant linéairement jusqu'à 0, hypothèse justifiée par « le maximum autorisé par le règlement » (section 2). Pas d'évolution de la piste, pas d'effet pilote.
- Données : FastF1, un seul pilote (Hamilton) et une seule course (GP d'Autriche 2025), environ 20 tours par relais. Seuls les tours d'entrée et de sortie des stands sont retirés ; aucune SC dans cette course.
- Inférence : Stan (HMC), 4 chaînes de 15 000 tirages après 15 000 de chauffe (section 4.2) ; 15 à 30 s par modèle (section 4.4).
- Résultats :
  - dégradation dur 0,054 s/tour [0,004 ; 0,133] et médium 0,060 [0,009 ; 0,120], sans différence significative entre composés (tableau 3) ;
  - incrément β : dur 0,011 [0,003 ; 0,020], médium 0,010 [0,002 ; 0,018] (tableau 4) ;
  - la dégradation estimée est négative en début de relais (montée en température des pneus) puis atteint environ 0,175 s/tour avant l'arrêt (figure 3) ; période de chauffe visible du tour 28 au tour 38 sur les durs (figure 1) ;
  - le modèle en t asymétrique a la meilleure erreur de prédiction (RMSPE 1,082 contre 1,520 pour un ARIMA(2,1,2), tableau 1) ;
  - pas de comparaison avec une régression linéaire.
- Pas de code publié.
- Évaluation pour fit_pace.py :
  - apport : séparer bruit de mesure et bruit d'état, dégradation variable au fil du relais, erreurs asymétriques (erreurs de pilotage) ;
  - coût : un modèle par pilote et par course, 15 à 30 s chacun, soit plusieurs heures pour 2023 à 2026 ; dépendance Stan hors de la pile ;
  - variante sans Stan, à tester (hypothèse) : modèle d'état linéaire gaussien avec statsmodels, déjà dans la pile ;
  - verdict : contrôle ponctuel sur quelques relais, pas remplacement de la régression de Huber groupée.
- Bibliographie : non triée référence par référence (article lu en HTML, sans copie locale) ; une piste relevée, Todd et al. 2025.

### 5. Liu, Fotouhi 2020 (texte intégral)
- Formula E, gestion de l'énergie. Trois réseaux de neurones (5 couches de 10 neurones) prédisent par tour la hausse de température de la batterie, la baisse de charge et le temps au tour, à partir de 7 entrées. Ils remplacent une co-simulation qui prend plus de 20 s par tour ; en 20 s, les réseaux produisent plus de 300 000 résultats (sections 3 et 5).
- Données d'entraînement : 172 800 échantillons générés en plus de 3 jours de simulation (section 2).
- MCTS (section 4) : une décision par tour (profondeur 32 pour 32 tours), jusqu'à 68 combinaisons de réglages par nœud, sélection UCT avec C_p = √2, récompense 2800 − t si la batterie n'est ni vide ni au-dessus de 60 °C, 0 sinon ; résultats obtenus après 100 000 itérations. Les auteurs écrivent que la solution vient « en quelques secondes » (section 5) ; matériel et temps de calcul non publiés.
- Événements rejoués (section 4.2) :
  - plan d'avant course : arrivée avec 0,88 % de charge et 59,8 °C ;
  - pilotage agressif pendant 6 tours ;
  - SC : stratégie replanifiée 3 s plus rapide que le plan initial. Incohérence interne : la SC dure « 2 tours » dans le texte d'introduction du scénario, et occupe les tours 5 à 7 dans sa description ;
  - hausse de la température ambiante : abandon évité au prix de 2 s.
- Pas de VSC. Limite reconnue : la solution du MCTS n'est pas optimale (section 5). Aucune déclaration de disponibilité du code.
- Évaluation pour F1STRAT après la v1 :
  - notre estimateur joue déjà le rôle du substitut rapide, donc aucun réseau n'est nécessaire ;
  - un MCTS par tour (s'arrêter ou non, gomme, mode) sur l'estimateur tiendrait dans un worker avec un budget d'itérations borné ;
  - données nécessaires : aucune au-delà de la calibration ;
  - risque : coût de calcul multiplié par le nombre de voitures pilotées par l'IA ; à réserver aux deux voitures du joueur (assistant) ou à quelques rivaux.
- Bibliographie : non triée référence par référence (article lu en HTML, sans copie locale) ; aucune piste relevée. La suite des mêmes auteurs (Liu, Fotouhi, Auger 2021, apprentissage par renforcement) est citée par Fieni ([17]) et écartée.

### 6. Choo 2015 (texte intégral)
« Real-time decision making in motorsports : analytics for improving professional car race strategy », Christopher Ledesma Weisen Choo, mémoire de master « Engineering and Management » (programme System Design and Management), MIT, juin 2015, dir. Cynthia Rudin. 100 p. ; pages = numéros imprimés. Prolonge le logiciel MATLAB de Tulabandhula et Rudin 2014 sur les saisons 2012 à 2014 de la Cup Series. Version publique caviardée : nom de la série masqué, circuits anonymisés (Southeast_A, Midwest_B, etc.), descriptions des variables retirées (p. 22).

Établi (texte) :
- Modèle : 165 variables, dont 40 retenues ; variable expliquée = variation de rang entre l'entrée aux stands et la fin du relais (p. 22). Découpage du relais en tours de chauffe et « epoch » : en début de relais, retrait des tours plus lents que le meilleur tour d'une fenêtre initiale ; en fin de relais, retrait d'un nombre fixe de tours avant la caution (p. 19 et 20).
- Immobilisations : environ 4 s pour le seul ravitaillement, 6 à 7 s avec 2 pneus, 13 à 14 s avec 4 pneus (p. 31). L'économie de 6 à 7 s d'un arrêt à 2 pneus (p. 75) recoupe les « environ 6 s » de Tulabandhula et Rudin.
- Immobilisation et place finale (6 courses 2014, boîtes à moustaches, p. 31 à 37) : la tête a des arrêts plus courts et plus réguliers, sans règle générale. Un pilote perd environ 20 places sur un arrêt de 111 s, en reperd sur un arrêt de 95 s, puis remonte jusqu'à la 6e place à l'arrivée (p. 34).
- « Driver momentum » : médiane, sur les relais précédents, de la variation de rang par tour (p. 38). Sur 9 courses, le signe reste stable d'un relais à l'autre pour la plupart des pilotes (p. 38 à 48).
- Usure par circuit (p. 54 à 58) : pente d'une régression linéaire sur le temps moyen des 20 premiers à l'arrivée, en début de course, hors 3 premiers tours, cautions et tours précédant l'arrêt, aberrants retirés à la main. 23 circuits : pente de 0,004 à 0,146 s/tour, soit 0,007 % à 0,236 % du temps au tour (fig. 39) ; 4 classes d'usure (fig. 41).
- Rapport arrêts à 2 pneus sur arrêts à 4 pneus (fig. 42, 36 courses 2014, données 2013 quand 2014 manquait) : de 0,02 à 0,78. Élevé sur les circuits peu abrasifs, faible sur les abrasifs, avec des exceptions (Midwest_E, abrasif, à 0,22) (p. 59 à 61).
- Comportements observés sur 5 courses (p. 62 à 66) :
  - circuit peu abrasif : en fin de course, la tête ne s'arrête plus, même sous caution, si l'autonomie suffit ; un pilote arrêté récemment change 2 pneus ou aucun ;
  - contre-exemple : la tête qui misait sur une dernière caution a dû s'arrêter sous drapeau vert (p. 64) ;
  - circuit abrasif : arrêt à chaque caution, même à 7 tours de l'arrivée (p. 66), et 4 pneus sauf arrêts presque consécutifs.
- Construction du jeu d'apprentissage (p. 67 à 71) : 4 courses test, jeux « même circuit », « circuits similaires », « circuits différents », « toutes les courses ». RMSE du rang de 2,16 à 2,82 pour le logiciel, contre 3,35 à 3,81 pour la référence « rang conservé ». Agréger toutes les courses ne fait pas moins bien que sélectionner des courses similaires. Réserve de l'auteur : uniquement des ovales d'environ 1,5 mile.
- Neutralisations : aucun chiffre. La section 7.4 propose seulement d'estimer la probabilité de caution par phase de course à partir de l'historique (p. 76), ce que fait déjà notre calibration d'après Heilmeier et al. 2020.
- Heuristiques proposées, non évaluées (p. 75) : circuit abrasif, s'arrêter à chaque caution et changer 4 pneus ; circuit peu abrasif, 2 pneus tôt dans la course si les pneus sont récents, et pas d'arrêt en fin de course dans le top 10.

Conclusions qui dépassent les éléments :
- Air libre : l'auteur écrit que les voitures en tête et en queue de peloton tournent plus vite (p. 13 et 16). La figure 4 de Tulabandhula et Rudin montre au contraire un temps au tour qui croît linéairement avec le rang ; la forme en U de leur figure 5 porte sur la pente d'usure, pas sur le temps au tour. Lecture erronée de la source.
- Momentum, immobilisations et place finale (p. 31 à 53) : inspection visuelle, sans test statistique. Le lien entre momentum et place finale est en partie mécanique, puisque la place finale cumule les variations de rang.
- Tableaux de la section 5 : trois des quatre RMSE sont identiques entre Midwest_C course 2 (fig. 52) et Southwest_B course 2 (fig. 53), soit 2,1609, 2,192 et 2,2075, les deux dernières permutées. Erreur de copie probable : la conclusion pour Southwest_B n'est pas fiable. Pour les autres courses, écarts de 0,04 à 0,14 entre jeux d'apprentissage, sans mesure de dispersion, sur 3 courses : « l'agrégation ne nuit pas » n'est pas démontré au-delà de ces cas.
- Pente d'usure : la NASCAR ravitaille ; la pente mélange usure, allègement en carburant et gomme déposée sur la piste (ce dernier point est cité p. 54) sans les séparer.
- Classement des circuits : la figure 44 et les heuristiques de la p. 75 ne rangent pas les mêmes circuits dans les mêmes groupes (Midwest_E et Midwest_D en « stratégie mixte » sur la figure 44, en « autres » p. 75 ; Northeast_A et Southeast_D en « 4 pneus » puis en « autres »).

Pour F1STRAT :
- Transfert faible : données NASCAR, rien de chiffré sur les neutralisations.
- Deux idées reprises en amendements, comme cibles à mesurer sur les données F1 et non comme règles d'IA : la décision d'arrêt sous neutralisation croisée avec la sévérité du circuit, la position et l'âge du pneu ; une variable « stratégie observée » (nombre d'arrêts) distincte de la sévérité pour les archétypes de circuits, équivalent du rapport 2 pneus sur 4 qui ne suit pas toujours l'usure.
- La comparaison avec la référence « rang conservé » confirme celle de Tulabandhula et Rudin (section 7).
- Bibliographie (p. 77) : articles de presse et de vulgarisation, plus Tulabandhula et Rudin 2014 ; rien de nouveau.

### 7. Tulabandhula, Rudin 2014 (texte intégral)
Big Data 2(2), juin 2014, p. 97 à 112, DOI 10.1089/big.2014.0018 ; PDF du dépôt MIT (page de garde plus 16 p.). Licence CC BY 3.0 États-Unis (p. 112). Mentions de droits incohérentes : « © 2012 » sur la page de garde du MIT, « Copyright 2013 » p. 112. NASCAR Sprint Cup 2012.

Établi :
- Données (p. 100) : 17 courses (tableau 1), 5 352 tours, 119 178 temps au tour et autant de rangs, 2 932 relais. De 160 à 500 tours, 170 à 373 arrêts et 3 à 14 cautions par course ; 4 à 8,9 arrêts par pilote en moyenne. Courses sur circuit routier et courses aux données de pneus manquantes exclues.
- Définitions (p. 100) : relais (« outing ») = tours de chauffe, aux temps décroissants après un arrêt ou une caution, puis « epoch », tours verts suivants jusqu'à l'arrêt suivant.
- Immobilisations (p. 100 et 101, fig. 1) : 2 pneus au lieu de 4 font gagner environ 6 s en moyenne, avec une forte dispersion. Pics de l'histogramme vers 4, 7 et 14 s (0, 2 et 4 pneus) et à 0 s (pénalités, données manquantes).
- Profil en dents de scie (fig. 2 et 3) : usure mesurée par la pente d'une régression linéaire sur le relais ; la pente s'atténue parfois en fin de relais.
- « Fresh air » (p. 101, fig. 4) : à un tour donné, le temps au tour croît linéairement avec le rang (2 courses, environ 40 voitures). La pente d'usure est plus forte en tête et en queue qu'au milieu, ajustée par un polynôme du second degré (fig. 5).
- Paradoxe de Simpson (p. 101, fig. 6, une course) : les relais après 2 pneus ont une pente médiane bien plus forte qu'après 4 pneus ; par tranches de rang (1 à 5, 6 à 15, 16 à 25), les médianes sont proches. Le rang est la variable cachée : seules les voitures bien placées prennent 2 pneus (aucun cas aux rangs 26 à 43, contre 49 arrêts à 4 pneus). 26 arrêts à 2 pneus, 176 à 4 pneus.
- Arrêts sous drapeau vert (p. 101 et 102) : le rang est artificiel tant que les voitures devant ne se sont pas arrêtées (un 20e devient 1er le temps du cycle). Les arrêts sous caution sont moins dispersés. Correction (p. 104 et 105) : décaler l'entrée du relais pour n'en garder que les tours où les voitures devant ne s'étaient pas encore arrêtées.
- Problèmes de données (p. 102 et 103) : pas d'expérience contrôlée ; déséquilibre (beaucoup plus d'arrêts à 4 pneus, fig. 7a) ; courses très différentes (fig. 7b) ; bruit (accidents, panne sèche, pénalités, arrêts décalés, « free pass », voiture qui reste en piste pour mener un tour).
- Prédiction (p. 103 et 107) : variation de rang entre l'entrée aux stands et la fin du relais suivant, pour 0, 2 ou 4 pneus ; décision myope, la meilleure des trois prédictions. Les cautions terminent la majorité des relais : la stratégie ne décide en général pas de leur fin.
- Hypothèses (p. 105 et 106) :
  - « rank momentum » : dérivées discrètes du rang ;
  - protection : une voiture à 2 pneus garde son rang si les voitures juste derrière ont aussi pris 2 pneus (fig. 8, une course : rangs 13 à 19 à 2 pneus, environ la moitié protégée) ;
  - courses de type A (perte de rang après 2 pneus, 6 courses) et B (pas de perte, 11 courses).
- Variables (p. 106 et 107), plus de 100 : rang au moment de la décision et au départ, rang moyen des relais précédents, âge des pneus gauches et droits, pentes passées, produits pente × rang, statistiques du voisinage, décision de pneus, premier relais, arrêt sous caution, durée des arrêts précédents, relais précédent court.
- Résultats (p. 107 à 109 ; fig. 9, valeurs estimées) :
  - ridge, SVR linéaire et LASSO : RMSE environ 2,7 (A) et 2,9 à 3,2 (B) ; R² environ 0,43 à 0,52 ; exactitude de signe environ 0,6 à 0,65 ; forêts aléatoires moins bonnes ;
  - référence « rang conservé » : RMSE environ 3,6 (A) et 4,3 (B) ; R² proche de 0 ; exactitude de signe environ 0,2, puisque le rang ne change pas dans environ 20 % des cas (texte, p. 108 et 109) ;
  - référence « rang moyen des relais précédents » : RMSE environ 3,8 et 4,4, R² négatif ;
  - validation croisée en 5 blocs répétée 10 fois ; apprentissage sur le début des courses, test sur la fin.
- Poids de l'indicatrice « 2 pneus » dans le LASSO selon la longueur du relais (fig. 11) : positif et croissant en A (jusqu'à environ +3 vers 23 tours), négatif et décroissant en B (jusqu'à environ −10 vers 23 tours).
- Constats (p. 109) : la longueur du relais compte peu au-delà de quelques tours ; la référence « rang conservé » est difficile à battre en RMSE, car les rangs varient le plus souvent de 0, 1 ou 2 places.

Conclusions qui dépassent les éléments :
- L'effet « fresh air » de la figure 4 mêle la qualité des voitures et l'air libre : les meilleures voitures sont devant. La relation linéaire entre rang et temps au tour ne prouve pas un effet aérodynamique ; l'article ne sépare pas les deux.
- L'explication de l'usure plus forte en tête par le rythme plus élevé (p. 101) n'est pas testée.
- La protection repose sur une course illustrative (fig. 8).
- Les types A et B sont obtenus a posteriori sur les données de course ; l'affirmation qu'on peut les déterminer dès les essais et les qualifications n'est pas démontrée (p. 106).
- La validation par des commentaires d'experts (p. 110) est qualitative et porte sur 5 citations.

Pour F1STRAT :
- Le paradoxe de Simpson touche directement la calibration : comparer entre pilotes le gain des stratégies à n+1 arrêts, ou l'effet du trafic, mêle rythme de la voiture et choix stratégique. Amendements ci-dessous : ajustement par effet pilote, estimation du trafic à l'intérieur d'un même pilote.
- Rang artificiel pendant un cycle d'arrêts : l'instantané du jeu expose déjà la sortie projetée, et la calibration compte les dépassements par paires, hors tours d'arrêt. Rien à ajouter.
- Références « rang conservé » et « rang moyen », exactitude de signe : critère de qualité simple pour notre prédicteur. Amendement ci-dessous.
- Protection : dans notre moteur, elle doit émerger du seuil de dépassement et de l'écart minimal (train de voitures), sans règle dédiée.
- Bibliographie : rien à reprendre (analyses de saison NASCAR, cricket, baseball, basket ; [21] Streja 2012, thèse sur la MotoGP, titre seulement, non ouverte).

### 8. Aversa, Cabantous, Haefliger 2018 (texte intégral)
Pages : numéros imprimés sur le manuscrit accepté (le PDF compte deux pages de plus).
- Contexte F1 de l'article (p. 6) : un arrêt mobilise 20 personnes pour 34 actions en environ 2,3 s ; chaque voiture passe 20 à 30 s dans la voie des stands au total ; environ 60 % des données de la voiture servent pendant la course, 40 % sont stockées.
- Cas : Ferrari, GP d'Abu Dhabi 2010, premier GP sur ce circuit (p. 9 et 10).
  - SC au premier tour après l'accident de Schumacher ; plusieurs voitures du milieu de peloton s'arrêtent sous SC, dont Petrov et Rosberg, qui ne s'arrêteront plus (p. 9 et 10).
  - Webber s'arrête au tour 11 sur 55 ; Ferrari arrête Alonso juste après, au tour 15 (tour 16 selon la citation de Sanz, p. 11), pour couvrir Webber.
  - Alonso ressort 12e, reste bloqué derrière Petrov, finit 7e et perd le titre d'un point.
  - Analyse a posteriori : un arrêt environ 20 tours plus tard l'aurait mis 4e (p. 10, d'après Allen 2010). Le stratège lui-même situe l'option manquante à environ 15 tours plus tard, pour une 5e ou peut-être 4e place (p. 12).
  - Le directeur de l'équipe reconnaît n'avoir pas pris en compte la difficulté de dépasser (p. 10).
- L'outil de Ferrari, une simulation Monte-Carlo aux paramètres déterministes (p. 9) :
  - ne proposait que deux options (s'arrêter maintenant ou dans 5 tours), et une règle d'équipe interdisait de s'en écarter (p. 12) ;
  - ne donnait aucune probabilité et n'avait pas de fonction d'apprentissage (p. 13) ;
  - ne permettait pas de réviser en course la probabilité de dépasser (p. 13) ;
  - se concentrait sur la voiture de l'équipe (p. 13) ;
  - n'avait pas d'historique de dépassement pour ce circuit, qui était nouveau (p. 14).
- Facteurs d'organisation (p. 11 à 13) : rôle de stratège tenu à temps partiel, culture de recherche de coupable, équipe d'analyse à distance (Maranello), communication par radio.
- Pour F1STRAT :
  - générer au moins une option de relais long ;
  - afficher des probabilités ;
  - laisser le joueur réviser les hypothèses du prédicteur ;
  - faire primer la règle d'air libre sur la couverture d'un rival.
- Bibliographie : articles de presse sur Abu Dhabi 2010 et sur l'arrêt manqué de Hamilton à Monaco en 2015, travaux de gestion et de systèmes d'information ; rien pour le modèle.

### 9. Bibliographie de l'article ITSC 2018 : tri
17 références (p. 2992 et 2993). Accès vérifié le 20/10/2026.

| Réf. | Source | Accès | Intérêt pour F1STRAT | Décision |
| --- | --- | --- | --- | --- |
| [1] | Porsche 2017, dossier de presse sur la stratégie en endurance | page web de 2017, non vérifiée | vue d'ensemble, endurance | écartée |
| [2] | FIA, règlements | en ligne | déjà prévu (règlement 2026) | déjà couverte |
| [3] à [6] | Siegler 2000, Brayshaw 2005, Colunga 2014, Timings 2014 : simulation du temps au tour (vue microscopique) | payants | hors périmètre : nos temps au tour viennent des données | écartées |
| [7] | Tulabandhula, Rudin 2014 | ouvert | voir section 7 | déjà traitée |
| [8] | Hirst, Wrangling F1 Data with R (livre) | Leanpub | traitement de données en R ; FastF1 couvre le besoin | écartée |
| [9] | McLaren Racing, « Formula One Race Strategy », Royal Academy of Engineering (ressource pédagogique) | PDF fourni par Antoine | méthode du temps de base, de l'effet du carburant et de la perte au stand, citée par l'article p. 2987 et 2988 | traitée en section 11 |
| [10] | Farroni, Sakhnevych, Timpone 2016, usure physique des pneus | payant (SAGE) | modèle thermique et frictionnel, trop fin pour un modèle par tour | écartée |
| [11] | Bekker, Lotz 2009, J. Oper. Res. Soc. 60(7), 952 à 961 | payant (Taylor & Francis) ; aucune copie ouverte trouvée ; Antoine n'a pas pu l'obtenir | simulation à événements discrets par secteurs, même famille que notre moteur ; l'article ITSC en critique le découpage | abandonnée ; contenu connu par Heilmeier et al. 2018 (p. 2987) et Carrasco Heine et Thraves 2023 (p. 242 : pannes, dépassements et arrêts simulés, stratégies fournies en entrée et non optimisées) |
| [12] | Bi 2014, Forbes, big data en F1 | article de presse | aucun | écartée |
| [13] | Phillips 2014, « Building a race simulator », blog f1metrics | ouvert, lu en texte intégral | modèle complet et chiffré (2014), méthodes de calibration | traitée ci-dessous |
| [14] | FIA, chronométrage 2017 | en ligne | remplacé par FastF1 | écartée |
| [15], [16] | Pirelli, gamme 2018 ; Mitchell 2018, écarts entre composés 2018 | en ligne | ère dépassée, remplacée par la calibration | écartées |
| [17] | Roborace | en ligne | aucun | écartée |

### 10. Phillips 2014, « Building a race simulator » (texte intégral)
Billet du 03/10/2014 (modifié le 03/09/2015), blog f1metrics, droits non précisés ; code non publié (Matlab). Ère 2014.
- Temps au tour : rythme prévu sur pneu dur (essais libres 2 et qualifications) + bruit + dégradation + carburant.
- Bruit : gaussien par pilote, écart-type de 0,2 à 0,7 s (Alonso 0,26 s, Chilton 0,65 s), mesuré comme écart à une parabole ajustée par relais.
- Carburant : 0,037 s par tour de carburant embarqué (Autriche 2014, comparaison de relais).
- Pneus : dégradation quadratique ; la gomme tendre s'use 2 fois plus vite et est 0,7 s plus rapide neuve ; croisement vers 14 tours. Multiplicateur d'usure par pilote d'après la longueur moyenne de ses relais.
- Départ : 0,25 s par place de grille (environ 5 s du 1er au 22e) ; bonus ou malus selon les places gagnées en moyenne au premier tour (0,25 s par place) ; 6 s de perte pour le départ arrêté ; écart-type porté de 0,25 à 1,00 s pour obtenir 33,4 changements de position au premier tour au lieu de 10,6, contre environ 30 en réalité.
- Arrêts : +4 s au tour d'entrée et +22,5 s au tour de sortie (Autriche) ; loi log-logistique : 50 % des arrêts à moins de 1 s du meilleur, 80 % à moins de 2 s, 90 % à moins de 4 s (temps de l'entrée à la sortie de la voie).
- Abandons : probabilité d'accident par tour d'après l'historique du pilote ; panne d'après la part d'abandons mécaniques de l'écurie en 2014. Après un abandon, SC avec la probabilité historique du circuit.
- SC : 6 tours ; temps delta environ 120 % du tour normal avec demi-usure ; derrière la SC environ 140 %, sans usure, dès 0,4 s de la voiture devant ; arrêt anticipé si la SC tombe à moins de 12 tours de l'arrêt prévu.
- Dépassement : DRS dès le tour 3 à moins de 1 s, gain net 0,4 s par tour ; usure ×1,1 dans l'air sale ; écart minimal 0,2 s ; seuil de 1,2 s par tour pour deux voitures identiques, modulé de 0,2 s par 10 km/h d'écart de vitesse de pointe ; 0,4 s perdues par la voiture dépassée.
- Calibration du seuil de dépassement : réglé pour reproduire environ 45 dépassements par course sèche en 2014 (hors premier tour et arrêts), contre environ 60 en 2011 et 15 ou moins de 1995 à 2009, soit un seuil de plus de 2 s à cette époque.
- Résultat : 1 000 courses en quelques minutes ; sans SC, temps du vainqueur 87 min 25 s ± 6 s contre 87 min 55 s en réalité (Autriche 2014).
- Pour F1STRAT : même architecture que la nôtre, avec deux méthodes de calibration directement reprenables, le seuil de dépassement réglé sur le nombre de dépassements par course et la dispersion au départ réglée sur le nombre de changements de position au premier tour. L'arrêt anticipé sous SC dans une fenêtre de N tours avant l'arrêt prévu est une règle d'IA simple à reprendre.

### 11. McLaren Racing, « Formula One Race Strategy », Royal Academy of Engineering (texte intégral)
Ressource pédagogique de 7 p. (fichier « 550-14_Car_Racing.pdf », PDF créé le 10/06/2009), référence [9] de l'article ITSC 2018. Aucune licence indiquée, McLaren mentionnée comme marque déposée : usage personnel. L'auteur n'est pas nommé ; l'encadré final présente William Mulholland, ingénieur dynamique du véhicule chez McLaren. Ère du ravitaillement.

Établi (p. 1 à 3 ; réponses aux exercices p. 6 et 7) :
- Scénario fictif : 50 tours, un arrêt au tour 20 ; consommation 3 kg/tour ; effet de masse 0,03 s par kg et par tour ; 100,045 s pour un tour avec 1 tour de carburant ; arrêt = 20 s + 0,5 s par tour de carburant ajouté.
- Modèle : temps au tour = t0 + nombre moyen de tours de carburant à bord pendant le tour × W, avec t0 = tour sans carburant (100 s) et W = consommation × effet de masse = 0,09 s par tour de carburant. La masse est comptée en moyenne sur le tour (début plus fin, divisé par 2).
- Temps d'un relais en forme fermée (éq. 7) : intégrale de t0 + (L2 − l) × W entre L1 et L2.
- Résultats : 2 018 s pour le premier relais, 35 s d'arrêt, 3 040,5 s pour le second, 5 093,5 s au total ; sans arrêt, 5 112,5 s. Tour d'arrêt optimal L2 = L/2 + t_f/(2W) = 27,78, soit le tour 28 : 5 088,06 s, 5,44 s de mieux qu'au tour 20. Tous ces résultats recalculés : exacts (déduit).
- Coquille p. 1 : (20 + 19)/2 × 0,09 donne 1,755 s, valeur du tableau 1, et non 1,775 s.
- L'article ITSC 2018 cite ce document pour la méthode (temps de base, effet de masse du carburant, perte au stand ; p. 2987 et 2988), pas pour des valeurs : ses chiffres sont ceux d'un exercice.

Pour F1STRAT :
- Méthode identique à notre terme k_carbu × masse. Aucune valeur mesurée à reprendre : 0,03 s/kg est une valeur d'exercice, qui tombe dans la plage TUM de 0,017 à 0,045 s/kg.
- Sans ravitaillement (interdit en course depuis 2010), le terme t_f disparaît. La masse au départ et la consommation ne dépendent pas des arrêts : l'effet du carburant sur le temps est le même pour toutes les stratégies d'arrêt et ne les départage que par l'usure liée à la masse (facteur(masse_carburant)) et par le mode de pilotage (déduit).
- Convention de masse : moyenne sur le tour (McLaren) ou masse en début de tour. L'écart vaut k_carbu × consommation / 2 par tour, décalage constant absorbé par le temps de base, sans effet sur les écarts entre voitures (déduit). Rien à amender.
- La forme fermée fournit un cas de référence analytique pour le terme carburant du moteur et de l'estimateur. Amendement ci-dessous.
- Bibliographie : deux manuels de mathématiques et un site de presse ; rien à retenir.

### 12. Carrasco Heine, Thraves 2023 (texte intégral)
« On the optimization of pit stop strategies via dynamic programming », Oscar F. Carrasco Heine (KU Leuven) et Charles Thraves (Universidad de Chile), Central European Journal of Operations Research 31(1), p. 239 à 268, en ligne le 14/06/2022, DOI 10.1007/s10100-022-00806-4. © les auteurs, licence exclusive à Springer : usage personnel. Code publié (p. 248, note 12) : github.com/FCarrascoHeine/F1DP, Julia, licence MIT ; cloné et lu, non exécuté.

Établi (article) :
- Programmation dynamique par tour (p. 244 à 246) : état = (composé, usure w de 0 à 1, carburant, indicateur « deux composés utilisés ») ; décision en fin de tour : rester, ou changer pour un composé donné ; arrêt placé en fin de tour (annexe C). Condition finale : temps infini si un seul composé a servi. La masse de départ est optimisée en plus (éq. 8).
- Usure par tour (éq. 9, p. 247) : d_composé × (1 + δ)^(carburant / capacité). δ = 0,2 n'est qu'un exemple (+20 % d'usure réservoir plein). Pneus inutilisables à w = 1.
- Temps au tour (éq. 10, p. 247) : μ0 + p0 × arrêt + α_composé + β(w) + g × carburant ; infini si les pneus sont usés ou le réservoir vide. β est une spline cubique passant par des couples (usure, perte), qui produit la falaise (annexe B, fig. 6 : +1,2 s à 70 % d'usure).
- Consommation dépendant du composé, le tendre consommant plus (p. 244, note 9) : hypothèse des auteurs, sans source.
- Instance (p. 248), valeurs d'illustration et non mesures : 52 tours ; μ0 = 85 s ; p0 = 21 s ; g = 0,03 s/kg ; consommation 1,92, 1,87 et 1,83 kg/tour (tendre, médium, dur) ; d = 1/25, 1/40 et 1/65 par tour ; α = 0, 0,6 et 0,9 s.
- Résultat déterministe (p. 248 et 249, fig. 1) : départ en tendre, passage en dur au tour 19 ; les départs en médium et en dur perdent environ 2,5 s et 1,5 s.
- Drapeau jaune (p. 249 à 253) :
  - assimilé à une VSC qui couvre des tours entiers, sans regroupement du peloton ; carburant 0,5 kg/tour, pas d'usure, arrêt à 10 s au lieu de 21 s (note 13) ;
  - algorithme 1 : la DP est résolue à nouveau à chaque nouveau jaune, sans anticipation ;
  - un jaune bien placé peut ajouter un arrêt : le départ en médium s'arrête au tour 21 sous jaune puis au tour 37, au lieu d'un seul arrêt au tour 30 ;
  - balayage d'un jaune de 2 tours à chaque tour (fig. 3) : le meilleur départ dépend du tour du jaune (tendre avant le tour 20 ou après le tour 33, médium ou dur entre les deux).
- Version stochastique (SDP, p. 255 à 257) : état augmenté de la météo (chaîne de Markov, matrice de transition par tour) et du nombre de tours de jaune restants ; probabilité d'un jaune par tour selon la météo et le tour. Instance (p. 257, annexe F) : 70 % de chances d'au moins un jaune, jaunes de 2 tours, probabilité uniforme par tour φ = 1 − (1 − π)^(1/N), soit environ 2,3 % pour 52 tours (déduit).
- SDP contre DP résolue à chaque jaune, sur 1 000 scénarios (tableau 1, p. 260) :
  - écart moyen par classe de scénarios de +0,18 à −1,13 s, avec quelques gains de 11 à 16 s ; sans jaune, la DP égale ou bat la SDP ;
  - la SDP retarde les arrêts pour profiter d'un jaune possible (départ en dur : arrêt au tour 34 au lieu de 33 si aucun jaune, p. 259) ;
  - son avantage croît avec la probabilité de jaune (fig. 5) ;
  - les classes publiées couvrent 992 scénarios sur 1 000 : les 8 scénarios à 5 jaunes ou plus ne sont pas rapportés (déduit).
- Calcul (annexe G) : environ 2,1 millions d'états par tour pour la DP et 9,1 millions pour la SDP ; 121 s par résolution DP et 636 s par résolution SDP (Julia, Apple M1 Pro, 6 cœurs).

Établi (code, F1det.jl et F1sto.jl) :
- δ = 0,1 dans l'instance (l'article ne donne que l'exemple 0,2) ; capacité 110 kg ; consommation du dur 1,82 kg/tour (1,83 dans l'article).
- Couples de β : (0 ; 0 s), (0,3 ; 0,3 s), (0,7 ; 1,2 s), (0,9 ; 2,2 s), (1 ; 3,0 s).
- Jaune : tour sans arrêt μ1 = 120 s, perte d'arrêt p1 = 10 s. La note 13 de l'article nomme à tort μ1 la perte de 10 s.
- Instance stochastique à un seul état météo (nr = 1) : la pluie n'est pas calculée.

Conclusions qui dépassent les éléments :
- Le résumé annonce la prise en compte de la pluie : la formulation existe, mais aucun calcul ne l'utilise.
- « La SDP surpasse la DP » : vrai en moyenne sur une seule instance synthétique, pour des gains de l'ordre de la seconde, sans rivaux (limite reconnue p. 262) et avec des jaunes de type VSC seulement.
- La consommation liée au composé est une hypothèse, et c'est elle qui fait varier la masse de départ selon la stratégie.
- Faits de contexte approximatifs, d'après mes connaissances, non revérifiés : la règle des deux composés date de 2007, pas de 2016 (note 2) ; l'obligation pour le top 10 de partir sur les pneus de la Q2 (note 11) a été supprimée en 2022.

Pour F1STRAT :
- Notre planificateur (DP sur les relais, coût d'un relais indexé par son tour de départ) revient à leur DP déterministe pour une masse de départ et un mode donnés, avec beaucoup moins d'états. Leur DP par tour, à 2 millions d'états par tour et 2 min de calcul, ne tiendrait pas dans un worker du navigateur (déduit). On garde notre formulation.
- Leur résolution à chaque jaune correspond à notre « relancé sur événement majeur ». La SDP n'apporte en moyenne qu'environ 1 s dans leur instance : pas de SDP complète en v1. La règle « attente de SC » de reactive.ts doit reproduire l'effet qualitatif, des arrêts plus tardifs quand la SC est probable : à contrôler par un test de propriété et sur les données réelles.
- Masse de départ : notre planificateur ne la choisit pas aujourd'hui.
- Forme d'usure liée à la masse : (1 + δ)^(masse / masse maximale), à reprendre comme forme par défaut de facteur(masse_carburant), δ marqué hypothèse.
- Rapports de contrôle, sur leurs valeurs d'instance (déduit) : arrêt sous jaune sur arrêt en vert 10 / 21 = 0,48 ; tour sous jaune sur tour vert 120 / 85 = 1,41, cohérent avec les 140 % sous VSC de Heilmeier et al. 2020.
- Amendements ci-dessous.
- Bibliographie : pour la stratégie F1, uniquement des sources déjà traitées (Bekker et Lotz, Phillips, Heilmeier et al. 2018 et 2020, McLaren RAEng, Chain Bear, Choo, ce dernier présenté à tort comme une thèse de doctorat) ; le reste porte sur la trajectoire, l'aérodynamique, la voile, la médecine et la maintenance industrielle.

### 13. Dinh, Tran, Reichert, Ametsbichler 2026 (texte intégral)
« A Gradient Boosting Analytics Framework for Predictive Pit Stop Decision Making in Formula One Racing », Dung Hai Dinh et Thang Minh Tran (Vietnamese-German University), Tim Reichert (Heilbronn), Tobias Ametsbichler (Max-Planck-Gesellschaft). Prépublication SSRN 6271405, non relue par des pairs (mention sur chaque page), PDF de février 2026, 36 p. ; pages = pages du PDF. Aucune licence indiquée : usage personnel. Ni code ni données publiés.

Établi :
- Données (p. 11 à 14) : FastF1 3.6.1, extraction du 05/11/2025, saisons 2022 à 2025, 84 courses, 90 023 tours. Retirés : 10 courses humides, courses « anormales » (distance différente de 305 km hors Monaco, et Monaco 2025), pilotes non classés, pilotes à plus de 3 tours, pilotes à plus de 4 arrêts. Reste 53 390 tours.
- Cible : tour d'entrée aux stands, environ 3 % des tours (p. 16).
- Variables (p. 11 à 13 et 17) : année, course, pilote, écurie, qualification, grille ; tour, position, gomme, âge du pneu, relais, statut de piste (codes 1, 2, 4, 5, 6 et 7, comme notre calibration) ; temps au tour (« du tour précédent » selon le tableau 3) ; écarts devant, derrière et au leader en fin de tour ; température de piste, accélérateur moyen et part de freinage sur le tour, usage du DRS. Variables construites : leader, dernier, tour de sortie des stands, voiture devant ou derrière déjà arrêtée.
- Méthode : découpage aléatoire 70 / 30 (p. 21), recherche sur grille avec validation croisée en 5 blocs, score F1 ; pondération des classes.
- Résultats (p. 24 à 28, tableau 8) : forêt aléatoire F1 0,41 (précision 0,29, rappel 0,72, AUC 0,95) ; SVM F1 0,68 (0,71 ; 0,66 ; AUC 0,94) ; XGBoost F1 0,86 (0,87 ; 0,85 ; AUC 0,99). Variables les plus importantes (forêt) : âge du pneu et temps au tour, puis accélérateur moyen et température de piste.

Conclusions qui dépassent les éléments :
- Ce n'est pas une prévision : le modèle classe le tour en cours comme tour d'entrée ou non, avec des variables mesurées en fin de ce tour (accélérateur moyen, freinage, écarts et position à la ligne). Sur un tour d'entrée, la voiture ralentit pour entrer dans la voie des stands : ces variables contiennent la réponse. Fuite d'information probable ; hypothèse non vérifiable sans le code. L'importance de l'accélérateur moyen va dans ce sens.
- Découpage aléatoire par tour, et non par course : des tours de la même course et du même relais se retrouvent des deux côtés, ce qui gonfle les scores.
- Aucune comparaison avec une règle simple (seuil d'âge par gomme plus statut de neutralisation).
- Incohérences : SVM « implémenté avec RandomForestClassifier » (p. 20) ; courbe ROC de XGBoost légendée « SVM » (p. 27) ; score F1 décrit comme la « moyenne » de la précision et du rappel, puis donné comme moyenne harmonique (p. 22).
- Revue de littérature mal attribuée (p. 8) : DP stochastique attribuée à Bekker et Lotz 2009, dont le titre annonce une simulation à événements discrets ; MIQP de « l'Universidad de Chile » attribuée à Garcia Tejada 2023 (Aalto, prévision de résultats), alors que la référence chilienne est Quiroga García 2024 ; probabilité de SC attribuée à van Kampen et al. 2024 (voitures d'endurance électriques). Le résultat « les jaunes retardent les arrêts » qu'elle cite est bien celui de Carrasco Heine et Thraves 2023.
- Monaco 2025 (p. 14) : décrit comme l'obligation d'utiliser trois types de pneus ; d'après mes connaissances, il s'agissait de trois trains de pneus, soit deux arrêts obligatoires (non revérifié).
- La conclusion selon laquelle la stratégie d'arrêt « se modélise avec une grande précision » ne tient pas compte des deux premiers points.

Pour F1STRAT :
- Rien à reprendre comme modèle.
- Une règle de mesure pour la calibration : toute variable d'un comportement stratégique est prise sur l'état connu avant la décision, jamais en fin de tour d'entrée. Elle touche notre mesure des réactions à l'undercut. Amendement ci-dessous.
- Deux pistes tirées de sa bibliographie (section suivante).

### 14. Heilmeier, Thomaser, Graf, Betz 2020, Virtual Strategy Engineer (texte intégral, 19/10/2026)
Applied Sciences 10(21) 7805, DOI 10.3390/app10217805, CC BY 4.0. Notes complètes, avec pages : notes_vse_heilmeier_2020.md. Code : TUMFTM/race-simulation (LGPL-3.0) ; base de chronométrage 2014 à 2019 TUMFTM/f1-timing-database (CC BY-NC-SA 3.0, usage non commercial).
- Deux réseaux de neurones : faut-il s'arrêter à ce tour, puis quelle gomme monter. Leurs entrées (progression de la course et de l'âge du pneu, leader ou poursuivant, gomme relative, catégorie de circuit, statut de neutralisation, arrêts restants, poursuivant qui vient de s'arrêter, écart de moins de 1,5 s) sont les signaux de reactive.ts.
- Valeurs reprises dans les prompts : tours à 140 % sous VSC et 160 % sous SC ; usure ralentie de 50 % sous VSC et de 75 % sous SC (choix de modélisation, pas une mesure) ; 3,1 % des tours avec un changement de pneus sur 121 courses (cohérent avec les environ 3 % de Dinh et al. 2026 sur 2022 à 2025) ; âge normalisé au changement par gomme (tableau 3) ; gomme au départ (tableau 17) ; seuil de 2 s pour un arrêt supplémentaire ; cas de référence de 55 tours (tableau 8).
- Stratégie de base par MIQP, avec un ordre des relais indifférent et une usure indépendante de la masse : nous avons retenu une DP sur les relais, parce que notre usure dépend de la masse.
- Bibliographie : triée par Antoine dans la mission du 20/10. Les 8 références retenues sont traitées ici (sections 1 à 8) ; les autres ont été écartées par la mission (prédiction dans d'autres sports, mathématiques de classement, Ergast, communications Pirelli 2017 à 2019, outils, vulgarisation).
- Statut : déjà intégré aux prompts le 19/10, aucun amendement nouveau.

### 15. McLaren Racing, « Making the right call » (lecture indirecte)
Page de mclaren.com rangée sous le GP du Canada 2019 (adresse listée dans docs/sources_donnees_strategie_f1.md), datée du 07/03/2023 selon l'outil de lecture ; pas d'auteur nommé, propos de Randeep Singh, responsable de la stratégie de course chez McLaren. Le texte s'appuie sur des données 2019 : date de republication probable (hypothèse). © McLaren, usage personnel. Lu le 20/10/2026 par l'outil de lecture web, qui renvoie un résumé et non le texte entier.
- Probabilité de base de SC par GP tirée de l'historique de ce GP. Causes pondérées : débris et accrochages jugés bons indicateurs ; pluie passée ignorée si la course est annoncée sèche ; événements isolés écartés (invasion de piste à Silverstone en 2003).
- Ajustements : changements de règlement et de pneus, variations d'une saison à l'autre ; modèle de pneus remis à jour après les premières courses de la saison.
- Chiffres : 60 % des GP du Canada avec au moins une SC ; une SC dure au moins environ 4 tours, une VSC parfois une minute seulement ; simulations lancées environ trois mois avant la course.
- Le gain d'un arrêt sous neutralisation dépend de ce que font les rivaux ; éviter les doubles arrêts mal préparés.
- Pour F1STRAT : conforte notre calibration des neutralisations (historique par circuit, causes classées, lissage vers la population). Un ajout : séparer les taux entre courses sèches et humides et exclure les causes non reproductibles. Amendement ci-dessous.

## Pistes nouvelles (non lues)
Relevées dans les bibliographies relues ou au fil des recherches ; aucune n'a été ouverte.
- « A simulation framework for Formula 1 race strategy based on pit-stop optimization », Borruso, Avella et un troisième auteur, Optimization Online, février 2026 (mis à jour en avril 2026) : optimisation conjointe des relais, gommes, carburant et ERS ; PDF ouvert. Priorité 3.
- Quiroga García, « Optimization of Pit-Stop Strategies in Formula 1 Racing : A Data-Driven Approach », mémoire de master, Universidad de Chile, 2024 (référence de Dinh et al. 2026) : PDF annoncé ouvert sur repositorio.uchile.cl. Même université que Thraves ; d'après la revue de Dinh et al., peu fiable, modèle MIQP réestimé sur la course en cours. Priorité 2.
- Sulsters, « Simulating Formula One Race Strategies », mémoire de master, Vrije Universiteit Amsterdam, 2018 (réf. [7] du Monte-Carlo) : accès non vérifié. Priorité 3.
- Salminen, « Race Simulator : Downloadable R Program Code », blog f1strategyblog, 10/05/2019 (réf. [6] du Monte-Carlo) : code R d'un simulateur de course, licence non vérifiée. Priorité 3.
- Sasikumar, Leema, Balakrishnan, « Data-driven pit stop decision support for Formula 1 using deep learning models », Frontiers in Artificial Intelligence 8, 2025, DOI 10.3389/frai.2025.1673148 (référence de Dinh et al. 2026) : même famille que Dinh et al., à lire avec la même vigilance sur la fuite d'information. Priorité 3.
- Aguad, Thraves, « Optimizing pit stop strategies in Formula 1 with dynamic programming and game theory », European Journal of Operational Research 319(3), 2024, p. 908 à 919 (réf. [12] de Fieni) : interaction stratégique entre rivaux. Priorité 2.
- Thomas et al., « Explainable reinforcement learning for Formula One race strategy », ACM SAC 2025, p. 1090 à 1097 (réf. [11] de Fieni). Priorité 3.
- Boettinger, Klotz, « Mastering Nordschleife : a comprehensive race simulation for AI strategy decision-making in motorsports », arXiv:2306.16088, 2023 (réf. [15] de Fieni). Priorité 3.
- Todd et al., « Explainable Time Series Prediction of Tyre Energy in Formula One Race Strategy », arXiv:2501.04067, 2025 (cité par Cappello et Hoegh). Priorité 3.
- « Learning-based Multi-agent Race Strategies in Formula 1 », arXiv:2602.23056, 2026 (vu dans une recherche ; auteurs non vérifiés). Priorité 3.
- Heilmeier, thèse de doctorat, TU München, 2022 (réf. [7] de Fieni) : synthèse probable des trois articles de la TUM. Priorité 3.

## Amendements proposés (non appliqués)

### docs/prompt_calibration.md

Contexte, liste des documents de référence, ajouter :
```markdown
notes_montecarlo_heilmeier_2020.md (lois probabilistes 2014 à 2019, code TUM) et veille_biblio_strategie.md (synthèse des sources secondaires).
```

Stack, ajouter à la liste :
```markdown
scipy (scipy.stats : lois log-logistique et Beta ; déjà installé avec statsmodels, à déclarer explicitement).
```

Modèle de rythme, remplacer la phrase sur la masse de départ de 70 kg par :
```markdown
- Masse de carburant au départ par ère, en configuration, marquée hypothèse : 2023 à 2025 : 110 kg (maximum réglementaire selon Cappello et Hoegh 2025 ; 100 à 110 kg dans les fichiers TUM 2014 à 2019), à vérifier dans le règlement technique ; 2026 : à vérifier dans le règlement technique 2026 (ordre de grandeur 70 kg donné par la vidéo Chain Bear). k_fuel par défaut 0,03 s/kg, plage de contrôle 0,017 à 0,045 s/kg (121 courses TUM 2014 à 2019).
- Contrôle optionnel (lot 3) : sur 3 relais contrastés, modèle d'état linéaire gaussien avec statsmodels (rythme latent, dégradation linéaire, remise à zéro à l'arrêt ; d'après Cappello et Hoegh 2025, sans Stan). Comparer sa pente de dégradation à celle de la régression de Huber.
```

Modèle de rythme, ajouter aussi :
```markdown
- Pénalité de trafic : second ajustement sur les tours verts secs, tours en trafic inclus, avec l'écart à la voiture devant par classes (moins de 0,5 s, 0,5 à 1 s, 1 à 1,5 s ; au-delà de 1,5 s en référence ; bornes paramétrables), effet fixe pilote et termes d'âge du pneu conservés. L'effet est ainsi mesuré à l'intérieur d'un même pilote. C'est une borne haute de delta_air_sale, car il inclut le blocage derrière une voiture plus lente. Ne jamais l'estimer en comparant le rythme entre positions : en tête, voiture plus rapide et air libre se confondent (Tulabandhula et Rudin 2014, fig. 4). Export dans field.json.
- Diagnostic optionnel (lot 3) : pente de dégradation par relais selon le tour de départ du relais (même composé, même course). Une pente plus faible pour les relais tardifs est compatible avec une usure liée à la masse (δ de facteur(masse_carburant) côté jeu ; Carrasco Heine et Thraves 2023, éq. 9) mais aussi avec l'évolution de la piste : rapporter, ne pas exporter comme mesure de δ.
```

Événements, ajouter :
```markdown
- Lois à exporter, sur le modèle de Heilmeier et al. 2020 (tableaux 4, 5, A3 et A4) et comparées à leurs valeurs 2014 à 2019 : nombre de SC par course (0, 1, 2, 3 et plus) ; part des SC commencées au premier tour ; début des autres par tranches (2e tour à 20 %, 20 à 40 %, 40 à 60 %, 60 à 80 %, 80 à 100 %) ; durée des SC en tours ; nombre de VSC par course ; durée des VSC en tours.
- P(VSC sachant panne) = nombre de VSC causées par une panne / nombre de pannes, et P(SC sachant accident), à partir des causes classées ci-dessus.
- Taux de SC et de VSC par circuit calculés à part pour les courses sèches et humides : la cause « météo » n'entre pas dans le taux d'une course sèche. Les causes non reproductibles (invasion de piste, par exemple) sont listées, comptées et exclues du taux (méthode décrite par McLaren, « Making the right call », lecture indirecte).
- Rythme sous neutralisation : pour la SC, ne retenir que les tours où elle est en piste depuis plus de 1,5 tour et qui ne sont pas le dernier de la phase ; pour la VSC, que les tours qu'elle couvre entièrement ; pilotes P1 à P3 (critères de Heilmeier et al. 2020, p. 6).
- Perte au stand par régime : comparer aux valeurs 2018 et 2019 du tableau 6 de Heilmeier et al. 2020 (Catalunya, Melbourne, Monza, Suzuka) et aux rapports VSC sur vert et SC sur vert des fichiers TUM (médianes 0,60 et 0,54).
- Durée d'immobilisation : vérifie si FastF1 ou une autre source ouverte la fournit. Sinon, utilise le temps passé dans la voie des stands (PitOutTime − PitInTime), qui l'inclut. Par écurie, ajuste une loi log-logistique (scipy.stats.fisk : forme, position, échelle) sur l'écart à l'arrêt le plus court de la course, en ne gardant que les écarts de 4 s au plus (méthode du tableau A2 de Heilmeier et al. 2020). Rapporte à part la fréquence et la durée des arrêts au-delà de 4 s.
```

Comportements stratégiques, remplacer la puce « Gain de temps des stratégies à n+1 arrêts » par :
```markdown
- Gain de temps des stratégies à n+1 arrêts par rapport à n arrêts, quand les deux sont observées sur une même course : temps de course corrigé de l'effet pilote (a_pilote × nombre de tours), et à part la comparaison entre coéquipiers. Rapporter côte à côte l'écart brut et l'écart corrigé : le choix de stratégie dépend du rythme et de la position, et l'écart brut peut changer de signe (paradoxe de Simpson, Tulabandhula et Rudin 2014, p. 101 et fig. 6).
```

Comportements stratégiques, ajouter :
```markdown
- Arrêts sous neutralisation, croisés : part des voitures qui s'arrêtent au premier tour de SC ou de VSC selon la progression de la course, la sévérité du circuit (terciles de s_circuit), la position (P1 à P3, P4 à P10, au-delà) et l'âge du pneu au déclenchement. Effectif de chaque case rapporté ; cases de moins de 30 cas fusionnées avec leur voisine. Distribution de l'âge du pneu chez les voitures qui s'arrêtent et chez celles qui restent en piste : elle fournit le seuil d'âge de la règle de neutralisation de l'IA. Hypothèse à vérifier, transposée de la NASCAR (Choo 2015, p. 62 à 66) : en fin de course, la tête reste en piste sur circuit peu abrasif et s'arrête sur circuit abrasif ; une voiture arrêtée récemment reste en piste.
- Âge normalisé au premier arrêt sous vert en fonction de la probabilité de SC du circuit (lissée), ajusté de s_circuit et de la perte au stand : coefficient et intervalle. Carrasco Heine et Thraves 2023 (p. 259, fig. 5) prédisent des arrêts plus tardifs quand la SC est plus probable. Les circuits à forte probabilité de SC sont souvent peu abrasifs, d'où l'ajustement ; avec environ 24 circuits, le résultat sera probablement non significatif : le rapporter tel quel. Sert de cible à la règle « attente de SC » de l'IA.
```

Comportements stratégiques, remplacer la puce « Réactions à l'undercut » par :
```markdown
- Réactions à l'undercut : part des cas où un pilote s'arrête au tour suivant l'arrêt de son poursuivant, ce poursuivant étant à moins de 1,5 s à la fin du tour qui précède son tour d'entrée. Règle générale : toute variable d'un comportement est mesurée sur l'état connu avant la décision, jamais en fin de tour d'entrée, où temps au tour, écarts et position sont déjà faussés par l'entrée aux stands (fuite d'information probable chez Dinh et al. 2026).
```

Écuries et pilotes 2026, remplacer la puce « Envol » par :
```markdown
- Envol, mesuré en temps et non en places (Heilmeier et al. 2020, p. 4, montrent que l'approche par places fausse les probabilités) : écart du temps au premier point de chronométrage disponible après le départ à une référence selon la place de grille. Moyenne et écart-type par pilote, lissés vers la population. Vérifie quelles données FastF1 permettent de dater le départ et le franchissement de la ligne ; à défaut, utilise le temps du premier tour et signale-le. Contrôle 2014 à 2019 : μ de −0,10 à +0,10 s, σ de 0,10 à 0,25 s (tableau A1).
```

Écuries et pilotes 2026, compléter la puce « Régularité » :
```markdown
Contrôle : méthode de Heilmeier et al. 2020, p. 4 (écarts à un polynôme du second degré ajusté par relais, hors deux premiers tours, tours d'arrêt et tours de neutralisation). Ordre de grandeur 2014 à 2019 : σ de 0,46 à 0,86 s.
```

Écuries et pilotes 2026, remplacer la puce « Fiabilité et erreurs » par :
```markdown
- Fiabilité et erreurs : probabilité d'accident par pilote et de panne par écurie, par saison, par inférence Beta-Bernoulli (Heilmeier et al. 2020, p. 9 et 10). A priori Beta par la méthode des moments (éq. 11 et 12), sur les pilotes et écuries ayant au moins 30 courses dans les données (2023 à 2026, plus 2014 à 2019 en option, étiqueté par ère) ; a posteriori Beta(α + z, β + N − z) ; exporter la moyenne a posteriori et son intervalle. Accident rattaché au pilote, panne à l'écurie, d'après le statut des résultats et les messages de direction de course.
```

Lissage, ajouter :
```markdown
Pour une probabilité, cette formule revient à un a priori Beta avec k = α + β et une moyenne a priori α / (α + β) : estime α et β par la méthode des moments (Heilmeier et al. 2020, éq. 11 et 12) et documente-les. Pour une moyenne continue, garde le choix de k par validation croisée.
```

Modèle de circuit, ajouter :
```markdown
- Comparer, par circuit, le nombre moyen d'arrêts observé et la part de courses à un arrêt à s_circuit ; signaler les discordances. La stratégie dépend aussi de la perte au stand et de la difficulté de dépasser (équivalent du rapport 2 pneus sur 4 de Choo 2015, fig. 42, qui ne suit pas toujours l'usure). Le nombre d'arrêts reste une cible (targets.json), jamais une entrée du modèle.
```

Données externes 2014 à 2019 (TUM), ajouter :
```markdown
- racesim/input/parameters/pars_mcs.ini : lois du Monte-Carlo 2014 à 2019 (accidents par pilote et pannes par écurie, par saison ; nombre, début et durée des SC ; durée des VSC ; P(VSC sachant panne) ; lois log-logistiques par écurie ; écart-type du temps au tour et envol par pilote). Red Bull et Toro Rosso y diffèrent du tableau A2 de l'article : signale les valeurs que tu retiens.
- Fichiers *.ini, section TRACK_PARS : seuil de dépassement par circuit, effet du DRS, pertes au premier tour et par place de grille, pertes au stand par régime. Une partie des pertes sous neutralisation sont des substituts repris de circuits similaires (Heilmeier et al. 2020, p. 14) : ne pas les traiter comme des mesures.
```

Export vers le jeu, compléter :
```markdown
- events.json : en plus, lois du nombre de SC par course, du début (premier tour puis tranches), des durées de SC et de VSC, P(VSC sachant panne), P(SC sachant accident).
- teams.json : paramètres log-logistiques d'immobilisation par écurie ; probabilité de panne a posteriori.
- drivers.json : envol (μ, σ) ; probabilité d'accident a posteriori.
- field.json : pénalité de trafic par classe d'écart, marquée borne haute de delta_air_sale.
- behaviour.json : arrêts sous neutralisation croisés (progression, sévérité, position, âge du pneu) ; gain des stratégies à n+1 arrêts, brut et corrigé de l'effet pilote ; âge au premier arrêt sous vert selon la probabilité de SC du circuit.
- targets.json : en plus, loi du nombre de SC par course, part des SC au premier tour, durées moyennes de SC et de VSC, nombre de changements de position au premier tour (méthode de calibration de Phillips 2014 pour la dispersion au départ).
```

Tests, ajouter :
```markdown
- Loi log-logistique : retrouver des paramètres connus sur un échantillon synthétique.
- Beta-Bernoulli : z = 0 donne une probabilité non nulle ; N grand donne la fraction observée.
```

### docs/prompt_jeu.md

Contexte, liste des documents de référence, ajouter :
```markdown
- notes_montecarlo_heilmeier_2020.md : lois probabilistes 2014 à 2019 et code TUM.
- veille_biblio_strategie.md : modèle de dépassement TUM, sources secondaires.
```

Pneus, ajouter :
```markdown
- Pneus froids : pénalité au premier tour de chaque relais (défaut 1,0 s, valeur unique du code TUM 2014 à 2019, hypothèse). Elle s'ajoute à la perte au stand calculée par la géométrie.
- facteur(masse_carburant) = (1 + δ)^(masse / masse_max), forme de Carrasco Heine et Thraves 2023 (éq. 9) ; δ par défaut 0,1 (valeur de leur code, non mesurée : hypothèse).
```

Carburant, ajouter :
```markdown
- Consommation sous neutralisation : facteur par régime (défauts 0,5 sous VSC et 0,25 sous SC, estimations de Heilmeier et al. 2020, p. 13), remplaçables par la calibration. Le carburant économisé reste disponible pour la suite de la course.
```

Dépassements et trafic, ajouter :
```markdown
- Écart minimal entre voitures : 0,5 s en vert, 0,8 s derrière la SC (défauts du code TUM).
- Duel : deux voitures à moins de l'écart minimal perdent chacune du temps (défaut 0,3 s par tour) ; la voiture dépassée perd en plus 0,3 s (défauts du code TUM).
- Vitesse de pointe : attribut voiture issu de la calibration (pièges à vitesse FastF1). L'écart de vitesse de pointe entre les deux voitures entre dans la probabilité de dépassement (le code TUM réduit le seuil de 0,009 à 0,061 s par km/h d'avance).
- difficulté_circuit : initialisée à partir du seuil de dépassement TUM du circuit quand il existe (1,26 à 3,75 s, médiane 2,0 s), puis calibrée sur les dépassements en piste 2023 à 2026.
- Dépassements interdits derrière la SC et sur les micro-secteurs couverts par une VSC. Aide au dépassement désactivée pendant N tours après une SC (défaut 2, code TUM 2014 à 2019 ; règle 2026 à vérifier).
- Zones de dépassement : une zone peut couvrir plusieurs micro-secteurs consécutifs (ligne droite plus freinage) ; la tentative se décide sur l'ensemble de la zone, pas dans un seul micro-secteur. Plusieurs voitures peuvent dépasser dans la même zone. La difficulté reste un paramètre par circuit, pas par micro-secteur (critique du modèle par secteurs de Bekker dans Heilmeier et al. 2018, p. 2987).
- L'écart minimal est contrôlé aussi après chaque sortie des stands, pas seulement en piste (Heilmeier et al. 2018, p. 2987 et 2990).
```

Arrêts aux stands, remplacer « temps d'arrêt (distribution à queue lourde) » par :
```markdown
temps d'immobilisation = minimum + tirage log-logistique par écurie (paramètres de teams.json), retiré tant qu'il dépasse 3 fois la moyenne de la loi (borne du code TUM) ; les arrêts ratés au-delà de cette borne suivent une loi séparée, issue de la calibration
```
et ajouter :
```markdown
- Test de vraisemblance : sur chaque circuit, les rapports perte VSC sur vert et SC sur vert calculés par la géométrie sont comparés aux plages observées (médianes 0,60 et 0,54 sur 2014 à 2019 ; tableau 6 de Heilmeier et al. 2020 pour 4 circuits). Un écart est signalé, jamais corrigé à la main.
```

Safety car et VSC, ajouter :
```markdown
- Chaînes causales par défaut : un accident déclenche une SC ; une panne déclenche une VSC avec une probabilité p (défaut 0,227, Heilmeier et al. 2020, 2015 à 2019) ; débris et météo ont leurs propres taux. En batch, ces chaînes doivent reproduire les lois de calibration/export/events.json : nombre de SC par course, part au premier tour (36 % des SC sur 2014 à 2019), début par tranches de course, durées de SC (2 à 8 tours) et de VSC (1 à 4 tours).
- Pas de nouvelle SC à moins d'un tour de l'arrivée, ni de VSC à moins d'un demi-tour (choix du code TUM, en paramètres).
```

Départ, remplacer « Qualité d'envol aléatoire selon le pilote » et la puce « Perte de temps au premier tour fonction de la position sur la grille (terme t_grid de Heilmeier et al.) » par :
```markdown
- Chaque voiture franchit la ligne au temps t_s(p_g) + N(μ_pilote, σ_pilote²). Courbe de référence t_s = √(2 d(p_g) / a) + t_r de Heilmeier et al. 2020 (p. 8 : a = 11,2 m/s², t_r = 0,2 s, 8 m entre deux places, origine décalée de 0,8 place), paramètres dans le JSON. Pilote sans données : μ = 0, σ = 0,146 s. Cette courbe remplace le terme t_grid.
```

IA, planner.ts, ajouter :
```markdown
- Le plan C est toujours une option de relais long, avec un arrêt nettement plus tardif que le plan A, même si l'estimateur la classe moins bien (Aversa et al. 2018 : l'option gagnante manquait à l'outil de Ferrari).
- Masse de carburant au départ : pour chaque stratégie candidate, masse minimale pour finir la course au mode prévu, plus une marge fixée par le profil (valeur par défaut marquée hypothèse), dans la limite du règlement. Option : recherche sur une grille de masses (éq. 8 de Carrasco Heine et Thraves 2023). Le joueur reçoit la masse proposée avec chaque plan.
- Pas de programmation dynamique stochastique complète en v1 : dans Carrasco Heine et Thraves 2023 (tableau 1), elle ne gagne en moyenne qu'environ 1 s sur une DP résolue à nouveau à chaque neutralisation, ce que fait déjà notre planificateur. L'effet d'anticipation passe par la règle « attente de SC ».
```

IA, reactive.ts, remplacer la règle de couverture d'undercut par :
```markdown
- couverture d'undercut : si le poursuivant à moins de 1,5 s vient de s'arrêter et que l'arrêt prévu est dans la fenêtre, s'arrêter maintenant, sauf si la sortie projetée tombe dans un groupe que la voiture ne pourra pas dépasser : la règle d'air libre prime (cas Ferrari, Abu Dhabi 2010, Aversa et al. 2018) ;
```
et, dans la règle de neutralisation, ajouter :
```markdown
fenêtre d'arrêt sous neutralisation : s'arrêter au premier tour de SC ou de VSC si l'arrêt prévu tombe dans les N prochains tours (paramètre du profil ; Phillips 2014 utilisait 12 tours en Autriche) ;
```

Prédicteur du joueur, ajouter :
```markdown
- Le prédicteur part de l'état connu du joueur, pas de l'état réel : usure des rivaux estimée, carburant des rivaux tiré dans une loi plausible, événements futurs tirés. Sinon il révèle des informations cachées. (Constat de relecture du prompt, pas d'une source.)
- Pour chaque candidate, afficher l'intervalle de confiance à 95 % de la position moyenne. Ordre de grandeur (Heilmeier et al. 2020, tableau 8) : ± 0,31 place avec 100 tirages, ± 0,08 avec 1 000 ; avec N = 200, environ ± 0,2 (extrapolation, hypothèse). Les nombres aléatoires communs réduisent l'incertitude sur l'écart entre candidates : à mesurer.
- Le joueur peut corriger en course les hypothèses du prédicteur : difficulté de dépassement, risque de SC.
- Contrôle de qualité (lot 7) : sur un batch de courses à graines fixées, à 25 %, 50 % et 75 % de la course, comparer la position finale prévue pour chaque voiture du joueur (moyenne sur N tirages) à la position obtenue par la simulation complète. Le prédicteur doit faire mieux, en RMSE et en exactitude de signe (gain, perte, stable), que deux références triviales : position actuelle conservée ; position moyenne depuis le départ. Rapporter les trois scores. (Méthode de Tulabandhula et Rudin 2014 et de Choo 2015.)
```

Outillage et tests, cas de référence, ajouter :
```markdown
- Carburant seul (forme fermée du document McLaren, éq. 7, sans ravitaillement) : relais de n tours sans usure, sans aléa ni interaction, masse m0 au départ, consommation c par tour répartie uniformément sur le tour. Temps du relais = n × t0 + k_carbu × (m0 × n − c × n² / 2). Tolérance : écart dû à la consommation par micro-secteur, de l'ordre de k_carbu × c × n / (2 × nombre de micro-secteurs) pour des micro-secteurs de même durée (déduit).
```

Outillage et tests, ajouter :
```markdown
- Propriété de l'IA : sur un circuit de test, à paramètres identiques, l'âge moyen au premier arrêt sous vert ne diminue pas quand la probabilité de SC augmente (retard prédit par Carrasco Heine et Thraves 2023, p. 259 et fig. 5). Mesurer aussi le gain moyen de la règle « attente de SC » contre la même IA sans cette règle ; ordre de grandeur attendu d'environ 1 s, d'après leur tableau 1 (hypothèse : leur instance est synthétique et sans rivaux).
```

Lots, compléter le lot 8 :
```markdown
Cibles supplémentaires : nombre de SC par course, part des SC au premier tour, durées de SC et de VSC, dispersion des immobilisations, changements de position au premier tour, arrêts sous neutralisation croisés avec la sévérité du circuit, la position et l'âge du pneu, âge au premier arrêt sous vert selon la probabilité de SC (behaviour.json). Réglage de difficulté_circuit par une courbe « dépassements par course en fonction de la difficulté », comme Phillips 2014 pour son seuil de dépassement.
```

Hors périmètre, remplacer « IA à réseaux de neurones » par :
```markdown
IA à réseaux de neurones ou à recherche arborescente. Option après la v1 : MCTS par tour sur l'estimateur, sans réseau (d'après Liu et Fotouhi 2020).
```
