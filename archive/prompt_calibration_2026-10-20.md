# Calibration du jeu de stratégie : pipeline Python FastF1

Version du 20/10/2026. Remplace la version du 19/10/2026. Intègre la synthèse des enjeux de réalisme (docs/synthese_enjeux_realisme.md), ses décisions, l'arbitrage des amendements de la veille bibliographique et le règlement FIA 2026.

## Contexte
Le dépôt contient un jeu de stratégie de course en TypeScript (voir CLAUDE.md et docs/prompt_jeu.md). Ce chantier ajoute un outil Python séparé, dans calibration/, qui extrait des données réelles de F1 et produit les paramètres du jeu : circuits, écuries et pilotes réels de la saison 2026, plus les cibles de calibration. Projet personnel, local, non diffusé : les exports contiennent les vrais noms.

Documents de référence (dossier docs/) :
- synthese_enjeux_realisme.md : décisions de modélisation, fenêtres de calibration par paramètre, articles du règlement 2026, valeurs de référence. En cas de conflit entre documents, elle fait foi ; signale le conflit.
- chainbear_strategie_f1_releve.md : concepts (modèle à blocs, pit delta, undercut, overcut, météo).
- sources_donnees_strategie_f1.md : sources et pièges ; partiellement dépassé (synthèse, section 1.2).
- notes_vse_heilmeier_2020.md : Virtual Strategy Engineer (Heilmeier et al. 2020, Appl. Sci. 10(21) 7805), cibles de comportement.
- notes_montecarlo_heilmeier_2020.md : lois probabilistes 2014 à 2019 et code TUM (Heilmeier et al. 2020, Appl. Sci. 10(12) 4229).
- veille_biblio_strategie.md : sources secondaires, modèle de dépassement TUM.
- reglement/ : règlement FIA F1 2026, sections A, B et C (PDF).

Deux articles de Heilmeier et al. datent de 2020 et ont chacun un tableau 8 : cite toujours « VSE » ou « Monte-Carlo ».

Signale tout conflit entre ce prompt et ces documents au lieu de trancher seul. Ne jamais inventer une valeur absente des sources : la signaler comme manquante.

Travaille par lots. Après chaque lot : tests verts, résumé, écarts par rapport à ce document, puis arrêt pour validation. Demande avant toute dépendance hors liste.

## Stack
- Python (version minimale exigée par la release FastF1 courante), fastf1, pandas, numpy, scipy (scipy.stats : lois log-logistique et Beta), statsmodels, scikit-learn (regroupement uniquement), pyarrow, matplotlib, requests (Open-Meteo), pytest. sqlite3 de la bibliothèque standard pour la base externe. Projet géré par pyproject.toml.
- Code et identifiants en anglais, unités SI (s, m, kg).
- Caches FastF1 et Open-Meteo dans calibration/.cache/ et données externes dans calibration/inputs/external/ : dans .gitignore pour leur volume. Dans calibration/out/, seul le rapport est versionné (les fichiers parquet sont ignorés). calibration/export/ est versionné.

## Dépôt git
Même dépôt GitHub privé que le jeu ; règles de la section « Dépôt git » de docs/prompt_jeu.md (branche par lot calib/lot-NN-nom, pull request en fin de lot, fusion par moi uniquement, tag calib-lot-NN, aucun fichier de plus de 50 Mo).

## Ères et fenêtres de calibration
Chaque paramètre est estimé sur une fenêtre fixée par sa dépendance à l'ère technique (synthèse, section 2.4). Étiquettes d'ère obligatoires sur toutes les données et sorties : « 2023-2025 », « 2026 », et « 2014-2019 » pour les données TUM.

| Paramètre | Fenêtre |
| --- | --- |
| Géométrie, voie des stands | toutes saisons ; vitesse limite 80 km/h sauf exception (règlement B1.6.3 a) |
| Perte au stand en vert | 2023 à 2026, contrôle sur 2026 |
| Rapports de perte VSC/vert et SC/vert | 2023 à 2026 ; 2014 à 2019 en contrôle |
| Taux, causes et durées SC, VSC, drapeau rouge | 2023 à 2026 ; 2014 à 2019 en a priori étiqueté |
| Climat, pluie | le plus d'années possible |
| Immobilisation au stand | 2023 à 2026 |
| Bruit pilote, envol | 2023 à 2026 |
| Dégradation, écarts entre composés, falaise | 2026 seul, modèle groupé |
| k_fuel (s/kg) | 2023 à 2026 ; masse de départ propre à 2026 |
| Difficulté de dépassement, air sale | 2026 seul |
| Fiabilité par écurie | 2026, a priori 2023 à 2025 |
| Comportements stratégiques | niveaux (nombre d'arrêts, composés) : 2026 ; comportements conditionnels (réaction à une neutralisation, à un undercut) : 2023 à 2026 avec étiquette d'ère |

Sous-ère 2026 : les GP d'Australie, de Chine et du Japon précèdent les modifications de gestion de l'énergie appliquées à partir du GP de Miami (3 mai 2026). Ils sont gardés partout. Une indicatrice « pre_miami » entre en covariable dans l'ajustement groupé de la dégradation, dans le delta voiture par écurie et dans les dépassements par course rapportés au modèle de circuit. Rapporte l'écart et son intervalle, avec cette limite : chaque circuit n'a qu'une course en 2026, donc l'écart est confondu avec l'effet circuit et avec le développement des voitures. Écart non significatif : aucune correction.

Les données 2014 à 2019 (TUM) servent d'a priori et de contrôle, jamais de valeur 2026.

## Entrées
- calibration/inputs/track_dna_2026.csv (séparateur ;) : caractéristiques et notes 1 à 5 par circuit 2026, source formula1dashboard.com. Points connus :
  - la ligne « Bahrain Grand Prix », nom court « Kuala Lumpur », est l'édition 2026 du GP de Bahreïn, courue à Sepang du 2 au 4 octobre 2026 : ce n'est pas une anomalie ;
  - conditions vides pour Madring ; colonne « drs » vide pour Madring et Sepang ; colonne downforce vide ;
  - le DRS n'existe plus en 2026 : le sens de la colonne « drs » est à établir sur le site source ; ne l'utilise pas comme variable explicative tant qu'il n'est pas établi.
- calibration/inputs/race_review_tracks_2023_2026.csv (séparateur ;) : par circuit, moyennes d'interruptions (SC + VSC + drapeaux rouges), de changements de position et taux de pluie, GP 2023 à 2026, source f1-race-review.com. Leur « dépassement » compte tout changement de position. Les moyennes mélangent 2023 à 2025 et 2026 : comparaison seulement, jamais cible 2026. Définition de rain_rate_pct (pluie pendant la course ou pendant le week-end) à établir sur le site ; sinon la signaler comme inconnue. La ligne « Sepang;BH » est le GP de Bahreïn 2026.
- calibration/inputs/compound_allocations.csv, à constituer : saison ; manche ; GP ; format (standard ou sprint) ; dur ; medium ; tendre (désignations C1 à C5, ou C6 si une saison antérieure l'a utilisé) ; spec_obligatoire_1 ; spec_obligatoire_2 (spécifications sèches obligatoires en course, règlement B6.1.2 b ii, une ou deux) ; url_source. Une ligne par GP, chaque valeur tirée d'un communiqué Pirelli, d'un document FIA ou d'une source équivalente citée. Valeur introuvable : NA, jamais déduite.
- calibration/inputs/circuit_coords.csv, à constituer : circuit ; latitude ; longitude ; url_source.
- Fichier de correspondance des circuits à créer (nom d'événement et lieu FastF1 ↔ noms des CSV ↔ lieux de la base TUM). « Bahrain Grand Prix » 2026 → Sepang ; aucune donnée Sakhir 2023 à 2025 ne sert d'historique à cet événement. Signale les circuits sans correspondance au lieu de deviner.
- Externe, optionnel (lot 9) : base TUMFTM/f1-timing-database (SQLite, saisons 2014 à 2019) et fichiers de paramètres TUMFTM/race-simulation (racesim/input/parameters/*.ini, 121 courses 2014 à 2019, et pars_mcs.ini), en lecture.

## Architecture
calibration/
  pyproject.toml
  cli.py              sous-commandes : ingest, fit, climate, external, report, export
  src/calib/
    ingest.py         chargement des courses et des séances du week-end via FastF1, cache parquet
    clean.py          filtrage des tours
    features.py       variables dérivées (âge pneu, écart à la voiture devant, statut piste, météo, ère, pre_miami)
    fit_pace.py       rythme, dégradation, pénalité de trafic
    fit_events.py     SC, VSC, drapeaux rouges, pluie, arrêts, perte au stand, immobilisation, dépassements, rythme sous neutralisation
    tyre_sets.py      inventaire de trains au départ
    behaviour.py      cibles de comportement stratégique pour l'IA
    fit_field.py      dispersion des performances voitures et pilotes
    fit_entrants.py   attributs des écuries et pilotes 2026
    geometry.py       géométrie des circuits, voie des stands, micro-secteurs, secteurs officiels
    climate.py        climat par circuit via Open-Meteo, transitions de pluie par secteur
    external_tum.py   lecture de la base TUM 2014-2019 et des paramètres race-simulation
    shrink.py         lissage des grandeurs par circuit
    track_model.py    paramètres de circuit en fonction des notes Track DNA, archétypes
    report.py         rapport avec figures de contrôle
    export.py         paramètres pour le jeu
  tests/
  inputs/  out/  export/  .cache/

## Ingestion
- Courses (pas de sprints pour les mesures de course) saisons 2023 à 2026 jusqu'à la dernière course disponible. Saisons en paramètre CLI. Pour l'inventaire de trains, charger aussi les essais libres, les qualifications, la qualification sprint et le sprint des GP 2026.
- Charger : tours, météo, statut de piste, messages de direction de course, résultats, télémétrie de position pour la géométrie.
- Vérifie les noms de colonnes contre la version installée. Attendus : LapTime, LapNumber, Stint, Compound, TyreLife, FreshTyre, PitInTime, PitOutTime, TrackStatus, IsAccurate, Deleted, DeletedReason, Position, Time, LapStartTime, Sector1Time, Sector2Time, Sector3Time, vitesses aux points de mesure (SpeedI1, SpeedI2, SpeedFL, SpeedST). Liste les écarts.
- TrackStatus est une chaîne qui concatène les codes survenus pendant le tour : 1 piste libre, 2 jaune, 4 SC, 5 rouge, 6 VSC déployée, 7 fin de VSC annoncée (la fin réelle est le retour à 1), 3 jamais observé. Vérifie ce format dans la documentation de la version installée. N'utilise pas le module fastf1.api (privé).
- Une course qui échoue au chargement est journalisée et sautée.
- Cache obligatoire, aucun rechargement si le parquet existe.

## Nettoyage : tours verts représentatifs
Exclure, avec un compteur par motif :
- tour 1, tours d'entrée et de sortie des stands ;
- tours non verts : un tour n'est conservé que si sa chaîne TrackStatus ne contient que le code 1 ; exclure aussi le tour de relance après SC, VSC ou drapeau rouge ;
- tours supprimés ou non précis ;
- gommes intermédiaire et pluie (traitées à part), tours avec précipitation ;
- tours en trafic pour le modèle de rythme principal : écart à la voiture devant sous un seuil au passage de la ligne (défaut 1,5 s, paramétrable) ;
- aberrants : au-delà de 107 % de la médiane du pilote sur la course.
Rapporter la part de tours conservés par course.

Monaco 2025 (deux arrêts imposés pour cette seule édition) est exclu des cibles de comportement et du nombre d'arrêts ; il reste utilisable pour le rythme.

## Modèle de rythme
Par course, sur les tours verts secs :
lap_time = a_pilote + b_gomme + d_gomme * age + c_gomme * age² + g * tour + ε
- Âge du pneu = TyreLife (inclut les tours des séances précédentes), FreshTyre en covariable.
- a_pilote : effet fixe pilote (voiture + pilote).
- b, d, c : offset, dégradation linéaire (s/tour) et courbure par gomme. Courbure conservée seulement si significative, sinon 0.
- g : effet tour combinant allègement en carburant et évolution de la piste. Ne pas les séparer par régression (colinéaires). Décomposition paramétrique : effet carburant = k_fuel * conso_par_tour ; effet piste = g - effet carburant. Signaler un effet piste négatif.
- Masse de carburant au départ, en configuration, marquée hypothèse :
  - 2026 : le règlement technique ne fixe aucune masse maximale en course (débit d'énergie limité à 3 000 MJ/h, C5.2.3) ; ordre de grandeur de consommation environ 70 kg (Chain Bear, PlanetF1) ;
  - 2023 à 2025 : 110 kg, maximum réglementaire de l'époque (règlement non relu : signaler).
  - k_fuel par défaut 0,03 s/kg ; plage de contrôle 0,017 à 0,045 s/kg (121 courses TUM 2014 à 2019).
- Régression robuste (Huber).
- Gommes : rôle du week-end (tendre, médium, dur) et désignation absolue via compound_allocations.csv.
- Ajustement groupé, voie principale pour 2026 (une seule course par circuit) : dégradation = d_C (par composé absolu) * s_circuit (sévérité, moyenne normalisée à 1), estimés ensemble sur toutes les courses de l'ère, avec pre_miami en covariable. Compare s_circuit aux notes Track DNA (abrasion, tyre_stress) et rapporte la corrélation.
- Contrôle de forme : ajuste aussi la forme logarithmique t = k2 * log(k1 * age + 1) + k3 (Heilmeier et al., ITSC 2018) sur les mêmes relais et compare l'erreur de prédiction à la forme retenue. Rapporter, ne pas exporter.
- Contrôle optionnel (lot 3) : sur 3 relais contrastés, modèle d'état linéaire gaussien avec statsmodels (rythme latent, dégradation linéaire, remise à zéro à l'arrêt ; d'après Cappello et Hoegh 2025, sans Stan). Comparer sa pente de dégradation à celle de la régression de Huber.
- Pénalité de trafic : second ajustement sur les tours verts secs, tours en trafic inclus, avec l'écart à la voiture devant par classes (moins de 0,5 s, 0,5 à 1 s, 1 à 1,5 s ; au-delà de 1,5 s en référence ; bornes paramétrables), effet fixe pilote et termes d'âge du pneu conservés. L'effet est ainsi mesuré à l'intérieur d'un même pilote. C'est une borne haute de delta_air_sale, car il inclut le blocage derrière une voiture plus lente. Ne jamais l'estimer en comparant le rythme entre positions : en tête, voiture plus rapide et air libre se confondent (Tulabandhula et Rudin 2014, fig. 4). Export dans field.json.
- Diagnostic (lot 3) : pente de dégradation par relais selon le tour de départ du relais (même composé, même course). L'évolution de la piste et l'usure liée à la masse de carburant sont supposées abaisser toutes deux la pente des relais tardifs (hypothèse) : une absence de baisse borne par le haut le coefficient δ du jeu (usure liée à la masse). Rapporter cette borne, jamais une mesure de δ.
- Sorties par course et par gomme : offset, pente, courbure, intervalles de confiance, nombre de tours, sigma résiduel global et par pilote.
- Agrégation par circuit et par ère : 2023 à 2025, et 2026 séparément.
- La dégradation mesurée est celle du rythme que les équipes ont choisi de tenir, gestion des pneus comprise : documente-la ainsi dans compounds.json ; elle correspond au niveau « neutre » du mode de pilotage du jeu.

## Falaise et relais
- Distribution de l'âge du pneu à l'arrêt par circuit et par gomme : médiane, quantiles 75 et 95 %, maximum.
- Seuil de falaise proposé = quantile 95 % (paramétrable), documenté comme borne basse (données censurées par les arrêts).

## Inventaire de trains au départ (tyre_sets.py)
- Règlement 2026 : 2 durs, 3 médiums, 8 tendres, 5 intermédiaires, 2 pluie par pilote en format standard ; 2 durs, 4 médiums, 6 tendres, 6 intermédiaires, 2 pluie en format sprint (B6.2.4) ; 2 trains des spécifications obligatoires gardés pour la course (B6.3.8 a ii).
- Pour chaque pilote et chaque GP 2026 : nombre de trains neufs de chaque composé disponibles au départ de la course = allocation moins les trains neufs entamés pendant le week-end (FreshTyre vrai au premier tour d'un relais, sur toutes les séances). Âge des trains déjà utilisés quand il est reconstituable par TyreLife.
- Les restitutions de trains ne sont pas publiées : marque le résultat comme estimation et signale les incohérences (plus de trains entamés que l'allocation, par exemple).
- Export dans grids.json avec la grille.

## Événements
- SC, VSC, drapeau rouge, séparément : nombre par course, tour de déclenchement, durée (en tours pour la SC, en secondes et en tours pour la VSC, en minutes de suspension pour le drapeau rouge), transitions VSC vers SC.
- Cause de chaque neutralisation, classée à partir du texte des messages de direction de course : accident, débris, voiture arrêtée ou panne, météo, autre, indéterminé. Part de chaque cause.
- Lois à exporter, sur le modèle du Monte-Carlo (tableaux 4, 5, A3 et A4), calculées sur 2023 à 2026 et comparées à leurs valeurs 2014 à 2019 : nombre de SC par course (0, 1, 2, 3 et plus) ; part des SC commencées au premier tour ; début des autres par tranches (2e tour à 20 %, 20 à 40 %, 40 à 60 %, 60 à 80 %, 80 à 100 %) ; durée des SC en tours ; nombre de VSC par course ; durée des VSC en tours ; nombre de drapeaux rouges par course et cause.
- P(VSC sachant panne) = nombre de VSC causées par une panne / nombre de pannes, et P(SC sachant accident), à partir des causes classées.
- Taux de SC, de VSC et de drapeau rouge par circuit calculés à part pour les courses sèches et humides : la cause « météo » n'entre pas dans le taux d'une course sèche. Les causes non reproductibles (invasion de piste, par exemple) sont listées, comptées et exclues du taux (méthode décrite par McLaren, « Making the right call »).
- Drapeau rouge : pour chaque suspension 2023 à 2026, mode de reprise (départ arrêté ou lancé), changements de composé pendant la suspension, course reprise ou non.
- Rythme sous neutralisation : rapport temps au tour sous VSC et sous SC / médiane verte du pilote, par circuit et global. Pour la SC, ne retenir que les tours où elle est en piste depuis plus de 1,5 tour et qui ne sont pas le dernier de la phase ; pour la VSC, que les tours qu'elle couvre entièrement ; pilotes P1 à P3 (critères du Monte-Carlo, p. 6). Comparer aux valeurs 140 % et 160 % (2014 à 2019).
- Pluie : part de courses avec précipitation, part de tours en intermédiaires ou pluie, tours de transition.
- Arrêts : nombre par pilote classé, séquences de gommes, tours d'arrêt en % de la course, part des arrêts sous SC, VSC ou drapeau rouge.
- Perte au stand par circuit : (tour d'entrée + tour de sortie) - 2 × médiane des tours verts du pilote dans les relais adjacents. Médiane et dispersion.
- Perte au stand par régime (vert, VSC, SC), à partir des arrêts effectués sous chaque régime. Si l'échantillon est insuffisant, rapports globaux VSC/vert et SC/vert. Comparer aux valeurs 2018 et 2019 du tableau 6 du Monte-Carlo (Catalunya, Melbourne, Monza, Suzuka) et aux rapports médians des fichiers TUM (0,60 et 0,54).
- Contrôle des pneus froids (après le lot 6) : par circuit, écart entre la perte au stand mesurée et la perte calculée par la géométrie de la voie des stands. Rapporter à côté de la valeur par défaut du jeu (1,0 s au premier tour de relais, code TUM, hypothèse).
- Durée d'immobilisation : vérifie si FastF1 ou une autre source ouverte la fournit. Sinon, utilise le temps passé dans la voie des stands (PitOutTime − PitInTime), qui l'inclut. Par écurie, ajuste une loi log-logistique (scipy.stats.fisk : forme, position, échelle) sur l'écart à l'arrêt le plus court de la course, en ne gardant que les écarts de 4 s au plus (méthode du tableau A2 du Monte-Carlo). Rapporte à part la fréquence et la durée des arrêts au-delà de 4 s.
- Dépassements en piste : changements de position entre deux tours consécutifs, hors tour 1, hors tours où l'un des deux pilotes s'arrête, hors SC, VSC, drapeau rouge et tour de relance. Fournir aussi le total de tous les changements de position, comparé à race_review_tracks_2023_2026.csv, avec le rapport entre les deux. Cible de difficulté de dépassement : 2026 seul.

## Comportements stratégiques (cibles pour l'IA)
Mêmes grandeurs que Heilmeier et al. 2020, VSE (tableaux 3, 17 et figure 5), recalculées sur 2023 à 2026 pour comparaison d'ère. Pour l'âge normalisé au changement, comparer à la ligne « 2016 et après » du tableau 3 (dur 38,8 %, médium 34,6 %, tendre 31,6 %). Filtres : courses sèches, 1 à 3 arrêts, temps au tour < 200 s, durée d'arrêt < 50 s ; signaler séparément les arrêts après 90 % de course. Niveaux (nombre d'arrêts, composés) sur 2026 ; comportements conditionnels sur 2023 à 2026 avec étiquette d'ère.

Règle de mesure générale : toute variable d'un comportement est mesurée sur l'état connu avant la décision, jamais en fin de tour d'entrée, où temps au tour, écarts et position sont déjà faussés par l'entrée aux stands (fuite d'information probable chez Dinh et al. 2026).

- Âge normalisé du pneu au changement (âge / nombre de tours de la course) par rôle de gomme.
- Part des arrêts faits au premier tour d'une neutralisation, et selon la progression de la course au déclenchement (seuil en dessous duquel une SC précoce ne déclenche pas d'arrêt).
- Arrêts sous neutralisation, croisés : part des voitures qui s'arrêtent au premier tour de SC ou de VSC selon la progression de la course, la sévérité du circuit (terciles de s_circuit), la position (P1 à P3, P4 à P10, au-delà) et l'âge du pneu au déclenchement. Effectif de chaque case rapporté ; cases de moins de 30 cas fusionnées avec leur voisine. Distribution de l'âge du pneu chez les voitures qui s'arrêtent et chez celles qui restent en piste : elle fournit le seuil d'âge de la règle de neutralisation de l'IA. Distribution du nombre de tours entre la neutralisation et l'arrêt prévu (estimé par la fin de relais habituelle) : elle fournit la fenêtre d'arrêt sous neutralisation de l'IA (défaut du jeu 12 tours, Phillips 2014). Hypothèse à vérifier, transposée de la NASCAR (Choo 2015, p. 62 à 66) : en fin de course, la tête reste en piste sur circuit peu abrasif et s'arrête sur circuit abrasif ; une voiture arrêtée récemment reste en piste.
- Comportement du leader et des poursuivants au premier tour de neutralisation.
- Âge normalisé au premier arrêt sous vert en fonction de la probabilité de SC du circuit (lissée), ajusté de s_circuit et de la perte au stand : coefficient et intervalle. Carrasco Heine et Thraves 2023 (p. 259, fig. 5) prédisent des arrêts plus tardifs quand la SC est plus probable. Avec environ 24 circuits, le résultat sera probablement non significatif : le rapporter tel quel. Sert de cible à la règle « attente de SC » de l'IA.
- Réactions à l'undercut : part des cas où un pilote s'arrête au tour suivant l'arrêt de son poursuivant, ce poursuivant étant à moins de 1,5 s à la fin du tour qui précède son tour d'entrée.
- Gomme au départ (part par rôle) et gomme choisie à chaque arrêt (part par rôle et par rang d'arrêt).
- Gain de temps des stratégies à n+1 arrêts par rapport à n arrêts, quand les deux sont observées sur une même course : temps de course corrigé de l'effet pilote (a_pilote × nombre de tours), et à part la comparaison entre coéquipiers. Rapporter côte à côte l'écart brut et l'écart corrigé : le choix de stratégie dépend du rythme et de la position, et l'écart brut peut changer de signe (paradoxe de Simpson, Tulabandhula et Rudin 2014, p. 101 et fig. 6).
- Choix de composé pendant un drapeau rouge (cas 2023 à 2026, effectif rapporté).

## Plateau
- Par course : écart de chaque a_pilote à la référence la plus rapide ; écarts entre écuries (moyenne des deux voitures) et entre coéquipiers.
- Sorties par ère : écart premier-dernier, écart-type entre écuries, écart-type entre coéquipiers.

## Écuries et pilotes 2026
- Entrants depuis les résultats FastF1 : nom, code, numéro, écurie, couleur d'écurie.
- Delta voiture par écurie et par GP : moyenne des a_pilote des deux voitures, lissée sur une fenêtre glissante des dernières courses (forme récente, taille paramétrable), pre_miami en covariable. Exporter aussi la série complète pour suivre le développement.
- Delta pilote : écart au coéquipier (a_pilote - moyenne de l'écurie), moyenné sur la saison, avec intervalle.
- Régularité : sigma résiduel par pilote. Contrôle : méthode du Monte-Carlo, p. 4 (écarts à un polynôme du second degré ajusté par relais, hors deux premiers tours, tours d'arrêt et tours de neutralisation). Ordre de grandeur 2014 à 2019 : σ de 0,46 à 0,86 s.
- Gestion des pneus : écart entre la pente de dégradation du pilote et celle de son coéquipier, sur les mêmes gommes.
- Envol, mesuré en temps et non en places (le Monte-Carlo, p. 4, montre que l'approche par places fausse les probabilités) : écart du temps au premier point de chronométrage disponible après le départ à une référence selon la place de grille. Moyenne et écart-type par pilote, lissés vers la population. Vérifie quelles données FastF1 permettent de dater le départ et le franchissement de la ligne ; à défaut, utilise le temps du premier tour et signale-le. Contrôle 2014 à 2019 : μ de −0,10 à +0,10 s, σ de 0,10 à 0,25 s (tableau A1).
- Pluie : rythme relatif sur les tours en intermédiaires ou pluie, seulement si l'échantillon le permet ; sinon hypothèse marquée.
- Attaque et défense : dépassements en piste réussis et subis, rapportés à l'écart de rythme. Échantillon faible attendu : lisser vers la moyenne et marquer.
- Vitesse de pointe par écurie (proxy) : médiane, sur la course, des vitesses maximales aux points de mesure. En 2026 elle dépend de l'énergie déployée autant que de la voiture : marquer comme proxy. Tester son effet sur les dépassements 2026 ; coefficient non significatif : exporter 0 pour ce terme.
- Fiabilité et erreurs : probabilité d'accident par pilote et de panne par écurie, par inférence Beta-Bernoulli (Monte-Carlo, p. 9 et 10). A priori Beta par la méthode des moments (éq. 11 et 12) sur 2023 à 2025, pilotes et écuries ayant au moins 30 courses (2014 à 2019 en option, étiqueté) ; a posteriori Beta(α + z, β + N − z) sur 2026 ; exporter la moyenne a posteriori et son intervalle. Accident rattaché au pilote, panne à l'écurie, d'après le statut des résultats et les messages de direction de course.
- Grilles : grille de départ réelle de chaque GP 2026 couru.

## Géométrie des circuits
- Tracé : polyligne issue des données de position (X, Y) d'un tour vert propre, rééchantillonnée et lissée. Longueur comparée à la longueur officielle de track_dna_2026.csv, écart rapporté.
- Voie des stands : trajet issu des positions d'une voiture sur un tour d'entrée et de sortie ; indices des micro-secteurs d'entrée et de sortie ; longueur ; vitesse limite 80 km/h (B1.6.3 a), exceptions documentées par GP avec leur source.
- Micro-secteurs : si FastF1 fournit les secteurs de commissaires dans les informations du circuit, les utiliser comme micro-secteurs ; sinon découpage régulier d'environ 20 segments. Vérifie la disponibilité sur la version installée.
- Secteurs officiels (3 par tour) : limites déduites des positions (X, Y) de la voiture aux instants de fin de secteur (LapStartTime + Sector1Time, puis + Sector2Time) sur un tour propre ; indices des micro-secteurs appartenant à chaque secteur. Le jeu résout l'humidité par secteur officiel.
- Type et poids des micro-secteurs depuis la vitesse sur le tour de référence (lent, moyen, rapide ; part du temps au tour).
- Zones de dépassement : ligne droite plus freinage suivant, déduites de la vitesse sur le tour de référence (suite de micro-secteurs rapides terminée par un freinage), alignées sur les zones d'activation de l'aileron actif quand elles sont connues. Une zone peut couvrir plusieurs micro-secteurs. Méthode documentée, résultat marqué dérivé.
- Probabilité d'incident par micro-secteur : drapeaux jaunes localisés dans les messages de direction de course quand ils citent un secteur, agrégés sur les saisons disponibles, lissés.
- Zones d'activation de l'aileron actif, lignes de détection et d'activation et écart de détection du mode dépassement : fixés par la FIA pour chaque compétition (B7.1.1 e, B7.2.1 b vii à ix), hors règlement. Vérifie si une source ouverte les publie, et si le canal DRS de la télémétrie FastF1 2026 porte l'état de l'aileron actif. À défaut : valeurs manquantes signalées, écart de détection 1 s par défaut (hypothèse, presse), ligne de détection avant la plus longue zone d'activation (hypothèse).
- Gommes nommées et spécifications obligatoires par GP 2026 depuis compound_allocations.csv.

## Climat (Open-Meteo, archive historique)
- Aux coordonnées de chaque circuit, séries horaires : rain, precipitation, wind_speed_10m, wind_direction_10m, temperature_2m (vérifie les noms exacts et l'existence de la variable de pluie dans la doc). Modèle ECMWF IFS 9 km pour 2017 et après, ERA5 pour la profondeur historique ; rapporte les deux.
- Fenêtre : date du GP plus ou moins 7 jours, heure de course plus ou moins 2 heures, sur le plus d'années disponibles.
- Sorties par circuit : probabilité de pluie dans la fenêtre de course, distribution des intensités horaires, durée des épisodes de pluie, vent (vitesse, direction dominante), température.
- Comparaison avec l'indicateur Rainfall de FastF1 et les taux de race_review_tracks_2023_2026.csv ; rapporte le biais (hypothèse à tester : sous-estimation des averses courtes due à la maille de 9 km, qui ne résout pas une cellule d'averse).
- Transitions de pluie (courses humides 2023 à 2026) : par secteur officiel, temps de secteur des voitures en slicks et en intermédiaires sur les mêmes tours ; en déduire le point de croisement slick/intermédiaire en temps et sa dynamique pendant la transition. Même chose pour intermédiaire/pluie si l'échantillon le permet. Seule source chiffrée des croisements : rapporter l'effectif. Relever aussi les messages « LOW GRIP CONDITIONS » et « NORMAL GRIP CONDITIONS » de la direction de course 2026 (règlement B1.5.11) et l'état de la piste à ces instants : ils règlent le seuil de faible adhérence du jeu. Si les données le permettent, vitesse de séchage par secteur pendant les transitions : a priori du coefficient de drainage par secteur du jeu ; sinon hypothèse marquée.
- Requêtes groupées, mises en cache, aucune rafale en parallèle.
- Export : paramètres du générateur de cellules de pluie par circuit (taux de naissance, durée de vie, intensité, vent), avec l'archétype comme a priori si les données manquent. Taille et vitesse des cellules : aucune source ; hypothèses marquées.

## Données externes 2014 à 2019 (TUM)
- Base f1-timing-database : fréquence et durée des phases VSC et SC (table fcyphases), abandons par accident et par panne (table retirements), comportements stratégiques de la section précédente. Utilisées comme a priori d'une autre ère pour le lissage, jamais mélangées sans étiquette d'ère.
- racesim/input/parameters/pars_mcs.ini : lois du Monte-Carlo 2014 à 2019 (accidents par pilote et pannes par écurie, par saison ; nombre, début et durée des SC ; durée des VSC ; P(VSC sachant panne) ; lois log-logistiques par écurie ; écart-type du temps au tour et envol par pilote). Red Bull et Toro Rosso y diffèrent du tableau A2 de l'article : signale les valeurs que tu retiens.
- Fichiers *.ini, section TRACK_PARS : seuil de dépassement par circuit (initialisation de la difficulté de dépassement du jeu), pertes au premier tour et par place de grille, pertes au stand par régime. Les effets DRS sont gardés comme historique seulement (pas de DRS en 2026). Une partie des pertes sous neutralisation sont des substituts repris de circuits similaires (Monte-Carlo, p. 14) : ne pas les traiter comme des mesures.
- Paramètres race-simulation (*.ini) : ordres de grandeur de dégradation et de perte au stand de 2014 à 2019, en comparaison avec l'ajustement 2023 à 2026. Lire le format sur les fichiers eux-mêmes, ne rien supposer.

## Lissage
Pour toute moyenne ou fréquence par circuit : (n × moyenne_circuit + k × moyenne_a_priori) / (n + k). A priori par défaut : moyenne globale de l'ère ; en option, valeur 2014 à 2019 du même circuit. Pour une probabilité, cette formule revient à un a priori Beta avec k = α + β et une moyenne a priori α / (α + β) : estime α et β par la méthode des moments (Monte-Carlo, éq. 11 et 12) et documente-les. Pour une moyenne continue, choisis k par validation croisée et documente-le.

## Modèle de circuit
- Joindre les paramètres par circuit (dégradation moyenne, sévérité s_circuit, perte au stand, dépassements, interruptions, effet piste) aux notes Track DNA.
- Régressions à 1 ou 2 variables explicatives (n ≈ 17 en 2026) : par exemple s_circuit ~ abrasion + tyre_stress, dépassements ~ straights_level. Rapporter R², coefficients, intervalles. Ne garder que ce qui est significatif, sinon la moyenne globale.
- Comparer, par circuit, le nombre moyen d'arrêts observé et la part de courses à un arrêt à s_circuit ; signaler les discordances. La stratégie dépend aussi de la perte au stand et de la difficulté de dépasser. Le nombre d'arrêts reste une cible (targets.json), jamais une entrée du modèle.
- Archétypes : 4 à 6 groupes de circuits (k-means ou équivalent sur notes + paramètres). Ils servent d'a priori pour les circuits peu documentés (une seule course, nouveau tracé) ; en 2026, c'est le cas de tous les circuits.

## Rapport
calibration/out/report.html : attributs des écuries et pilotes avec leur provenance, tracés des circuits superposés à la longueur officielle, parts de tours conservés, courbes temps/âge par gomme pour 3 circuits contrastés, comparaison des formes de dégradation (retenue et logarithmique), borne haute de δ, tableau des paramètres par circuit, écart pre_miami et son intervalle, distributions d'événements dont drapeaux rouges, contrôle des pneus froids, inventaires de trains, comportements stratégiques comparés entre ères, climat et transitions de pluie, comparaison avec les CSV d'entrée, hypothèses et limites.

## Export vers le jeu
calibration/export/ :
- circuits/<circuit>.json : un fichier par circuit du calendrier 2026 (géométrie, micro-secteurs, secteurs officiels et coefficients de drainage, voie des stands et vitesse limite, zones de dépassement, zones d'activation de l'aileron actif, lignes et écart de détection du mode dépassement, abrasivité, sévérité, T_ref, perte au stand par régime, probabilités d'incident, gommes nommées et spécifications obligatoires, climat).
- teams.json et drivers.json : attributs des écuries et pilotes 2026, delta voiture par GP ; écuries : paramètres log-logistiques d'immobilisation, probabilité de panne a posteriori, vitesse de pointe (proxy) ; pilotes : envol (μ, σ), probabilité d'accident a posteriori.
- grids.json : grilles de départ réelles des GP 2026 courus et inventaires de trains au départ (estimations marquées).
- compounds.json : offsets relatifs, pentes, courbures, seuils de falaise, par ère et par composé absolu ; mention que la dégradation correspond au rythme géré des équipes.
- field.json : distributions des écarts voitures et pilotes, sigma de régularité, pénalité de trafic par classe d'écart (borne haute de delta_air_sale).
- events.json : taux, durées et causes SC, VSC, drapeau rouge (sec et humide séparés) ; lois du nombre de SC par course, du début (premier tour puis tranches), des durées de SC et de VSC ; P(VSC sachant panne), P(SC sachant accident) ; transitions VSC vers SC ; modes de reprise après drapeau rouge ; rythme sous neutralisation ; pluie ; dépassements en piste.
- behaviour.json : cibles de comportement stratégique de l'IA, dont arrêts sous neutralisation croisés (progression, sévérité, position, âge du pneu), fenêtre d'arrêt sous neutralisation, gain des stratégies à n+1 arrêts brut et corrigé de l'effet pilote, âge au premier arrêt sous vert selon la probabilité de SC, choix de composé au drapeau rouge.
- weather.json : paramètres du générateur de cellules de pluie par circuit, croisements par secteur issus des transitions.
- targets.json : cibles de calibration du jeu avec intervalles (arrêts par voiture, dépassements en piste par course, interruptions par course, drapeaux rouges par course, taux d'abandon, écart vainqueur-second, loi du nombre de SC par course, part des SC au premier tour, durées moyennes de SC et de VSC, nombre de changements de position au premier tour), globales et par circuit.
- Chaque paramètre exporté est un objet { value, unit, method: "measured" | "derived" | "hypothesis", source, era, n, ci }. Aucun nombre nu.
- sources.md : liste des sources effectivement utilisées, pour la traçabilité.

## Tests
- Chaque filtre de nettoyage exclut les cas prévus (fixtures synthétiques).
- Modèle de rythme : sur données synthétiques générées avec des paramètres connus, les retrouver dans la tolérance.
- Ajustement groupé d_C × s_circuit, covariable pre_miami comprise : retrouver des valeurs connues sur données synthétiques.
- Pénalité de trafic : sur données synthétiques où le rythme dépend de la position, l'estimation intra-pilote retrouve la pénalité réelle.
- Loi log-logistique : retrouver des paramètres connus sur un échantillon synthétique.
- Beta-Bernoulli : z = 0 donne une probabilité non nulle ; N grand donne la fraction observée.
- Lissage : n = 0 donne la moyenne a priori, n grand donne la moyenne du circuit.
- Inventaire de trains : sur un week-end synthétique, le compte de trains neufs restants est exact.
- Mesure des comportements : sur une course synthétique, les variables d'une décision sont prises au tour qui précède le tour d'entrée.
- Géométrie : tracé fermé, longueur à moins de 2 % de la longueur officielle (seuil paramétrable), voie des stands raccordée au tracé aux bons micro-secteurs, trois secteurs officiels contigus couvrant le tour.
- Export : schémas respectés, provenance présente partout.

## Lots
1. Squelette, ingestion avec cache, correspondance des circuits (Bahreïn 2026 → Sepang), essai sur 3 courses.
2. Nettoyage, variables dérivées (dont ère et pre_miami), rapport de conservation.
3. Rythme et dégradation (par course puis groupé), contrôle de forme logarithmique, pénalité de trafic, diagnostic de δ, contrôle optionnel par modèle d'état, tests synthétiques.
4. Falaise, arrêts, immobilisation, perte au stand par régime, événements dont drapeaux rouges, dépassements, comportements stratégiques, inventaire de trains.
5. Plateau, écuries et pilotes 2026, fiabilité Beta-Bernoulli, grilles.
6. Géométrie des circuits, secteurs officiels, zones d'activation, contrôle des pneus froids.
7. Lissage, modèle de circuit, archétypes comme a priori.
8. Climat Open-Meteo, transitions de pluie par secteur, paramètres du générateur de pluie.
9. Données externes TUM 2014 à 2019 (optionnel).
10. Rapport et export.
