# Data_Biblio : index

Bibliothèque du projet F1STRAT. Rangée le 21/10/2026 par déplacements et renommages, sans aucune suppression. Index mis à jour à chaque ajout.

## Périmètre en vigueur (décisions du 21/10/2026)

- Saisons jouées : 2023 à 2025, voitures et plateau réels, forme des voitures réelle et évolutive par GP.
- Mode saison : classement et points selon le barème réel de chaque saison, relations entre pilotes ; qualification simulée ; pas de sprint.
- Calibration : toute donnée disponible qui aide (décision du 21/10/2026). Pilotes, circuits, neutralisations, météo, géométrie et perte au stand : 2014 à 2026. Voitures, pneus et dépassements : 2022 à 2025, même règlement technique ; 2026 exclu pour ces familles (pneus, aérodynamique active et moteur différents).
- Pneus vus par le joueur : tendre, médium, dur. Paramètres par (saison, GP, rôle), moyenne du rôle en repli.

Statuts utilisés : **à jour** ; **référence** (valable, pas d'évolution prévue) ; **à mettre à jour** (antérieur aux décisions ci-dessus) ; **hors période** ; **brut** (source primaire non retravaillée).

## 1_reglements

Règlements FIA en PDF, noms d'origine (ils portent l'issue et la date). Relevé des articles utiles : `5_notes/reglement_sportif_2023_2025_releve.md`.

| Dossier | Fichiers | Statut |
| --- | --- | --- |
| 2023 | sportif issue 8 (06/12/2023) ; technique issue 7 (31/08/2023) | brut, relevé |
| 2024 | sportif issue 7 (31/07/2024) ; technique issue 8 (17/10/2024) | brut, relevé |
| 2025 | sportif issue 5 (30/04/2025) ; technique issue 03 (07/04/2025) | brut, relevé |
| 2026_2027_hors_periode | 2026 sections A (issue 03), B (issue 09), C (issue 21) ; 2027 sections B (issue 01), C (issue 04) | hors période ; articles 2026 relevés dans la synthèse, section 6 |

## 2_articles

| Fichier | Ancien nom | Référence | Notes | Statut |
| --- | --- | --- | --- | --- |
| Heilmeier_2020_Virtual_Strategy_Engineer.pdf | applsci-10-07805.pdf | Heilmeier, Thomaser, Graf, Betz, Applied Sciences 10(21) 7805, 2020, DOI 10.3390/app10217805 | notes_vse_heilmeier_2020.md ; veille §14 | référence |
| Heilmeier_2020_Monte_Carlo_race_simulation.pdf | applsci-10-04229-v3.pdf | Heilmeier, Graf, Betz, Lienkamp, Applied Sciences 10(12) 4229, 2020 | notes_montecarlo_heilmeier_2020.md ; veille §1 | référence |
| Heilmeier_2018_ITSC_Race_simulation_strategy.pdf | heilmeier2018.pdf | Heilmeier, Graf, Lienkamp, « A Race Simulation for Strategy Decisions in Circuit Motorsports », ITSC 2018, p. 2986 à 2993 | veille §2 | référence |
| CarrascoHeine_Thraves_2023_Pit_stop_strategies_dynamic_programming.pdf | On-the-optimization-of-pit-stop-strategies-via-dynamic-programming.pdf | Carrasco Heine, Thraves, Central European Journal of Operations Research 31, p. 239 à 268, 2023, DOI 10.1007/s10100-022-00806-4 | veille §12 | référence |
| Tulabandhula_Rudin_2014_Tire_changes_fresh_air_yellow_flags.pdf | Tulabandhula-2014-Tire changes, fresh air, and.pdf | Tulabandhula, Rudin, Big Data 2(2), p. 97 à 112, 2014, DOI 10.1089/big.2014.0018 | veille §7 | référence (NASCAR) |
| Choo_2015_MIT_Real-Time_Decision_Making_in_Motorsports.pdf | 931596281-MIT.pdf | Choo, « Real-Time Decision Making in Motorsports », mémoire de master, MIT, 2015 | veille §6 | référence (NASCAR) |
| Dinh_2026_SSRN_Gradient_boosting_pit_stops.pdf | ssrn-6271405.pdf | Dinh, Tran, Reichert, Ametsbichler, prépublication SSRN 6271405, 2026, non relue par des pairs | veille §13 | référence, à lire avec prudence |
| McLaren_RAEng_2009_Formula_One_Race_Strategy.pdf | 550-14_Car_Racing.pdf | McLaren Racing, « Formula One Race Strategy », ressource pédagogique de la Royal Academy of Engineering, 2009 | veille §11 | référence (exercice) |

Sources lues en ligne, sans PDF local (détail dans la veille) : Fieni et al. 2025 (arXiv:2512.21570), Cappello et Hoegh 2025 (arXiv:2512.00640), Liu et Fotouhi 2020, Aversa et al. 2018, Bonomi et al. 2023, Phillips 2014 (blog f1metrics), McLaren « Making the right call ».

## 3_video_chainbear (ancien dossier « CB Vid »)

Chain Bear, « Building an F1 Strategy from the Bare Basics » (YouTube, 15 min 32). Relevé : `5_notes/chainbear_strategie_f1_releve.md`.

| Fichier | Contenu | Statut |
| --- | --- | --- |
| video.mp4, audio.m4a | vidéo et piste audio | brut |
| sous-titres.en-GB.vtt | piste anglaise saisie à la main, base du relevé | brut |
| sous-titres.en.vtt, sous-titres.en-orig.vtt | deux fichiers identiques (même empreinte), probablement la piste automatique | doublon |

## 4_donnees

| Fichier | Contenu | Source | Période | Statut | Notice |
| --- | --- | --- | --- | --- | --- |
| compound_allocations.csv | composés C (dur, médium, tendre), format du week-end, limites de tours par train, pour 70 GP | F1.com, Pirelli, F1Technical, FIA ; calendrier Jolpica | 2023 à 2025 | à jour | compound_allocations_lisezmoi.md |
| track_dna_2024_2025.csv | 8 notes de 1 à 5 par GP (traction, adhérence, abrasion, évolution, contrainte pneus, freinage, charge latérale, appui) | formula1dashboard.com (captures) | 2024, 2025 ; 2023 imputé par moyenne du circuit | à jour ; deux permutations du site corrigées en 2025 | track_dna_2024_2025_lisezmoi.md |
| track_dna_2026.csv | notes et caractéristiques fixes par circuit (longueur, virages lents, moyens et rapides, dénivelé, lignes droites) | formula1dashboard.com | 2026, 17 GP | référence pour les attributs fixes ; anomalie à Spa (voir plus bas) | aucune |
| circuits_virages_complement.csv | nombre et répartition des virages des 9 circuits absents de 2026 | dérivé des cartes formula1dashboard | fixe | à jour | track_dna_2024_2025_lisezmoi.md |
| race_review_tracks_2023_2026.csv | interruptions, changements de position et taux de pluie moyens par circuit | f1-race-review.com | moyennes 2023 à 2026 mélangées | comparaison seulement | prompt_calibration, section Entrées |
| captures_formula1dashboard/ | 6 captures : tableaux et cartes de similarité 2024, 2025, 2026 | formula1dashboard.com | 2024 à 2026 | brut | track_dna_2024_2025_lisezmoi.md |
| _extraction_api/ | script `extraction_api.py` (OpenF1 2023 à 2025 ; Open-Meteo : week-ends 2014 à 2025, climatologie 2005 à 2024, prévisions archivées 2024 à 2025) et liste des GP avec coordonnées (`gp_2014_2025.csv`) ; sorties dans openf1_2023_2025/ et meteo_open_meteo/ | script du 21/10/2026 ; coordonnées et dates F1DB | 2005 à 2025 | lancé le 21/10/2026, complet ; journal_extraction.txt | en-tête du script |
| openf1_2023_2025/ | arrêts (temps dans la voie, immobilisation), dépassements bruts, sessions de course | OpenF1 | 2023 à 2025 (arrêts : 64 courses ; immobilisation : depuis le GP des États-Unis 2024) | à jour ; dépassements à filtrer | openf1_2023_2025/openf1_2023_2025_lisezmoi.md |
| meteo_open_meteo/ | météo horaire des week-ends ; climatologie de 20 ans autour de chaque GP 2023 à 2025 ; prévisions archivées à 1 à 7 jours | Open-Meteo (CC BY 4.0) ; coordonnées F1DB | 2005 à 2025 | à jour | meteo_open_meteo/meteo_open_meteo_lisezmoi.md |
| tum_2014_2019/ | base SQLite TUM (tours avec gomme et âge du pneu, arrêts, phases SC et VSC, partants, qualifs, accidents et pannes) ; paramètres de simulation des 121 courses (courses, écuries, pilotes, pneus) ; paramètres Monte-Carlo | TUMFTM f1-timing-database (CC BY-NC-SA 3.0) et race-simulation (LGPL-3.0) | 2014 à 2019, 121 GP | à jour ; contrôlée contre F1DB et FastF1 | tum_2014_2019/tum_2014_2019_lisezmoi.md |
| fastf1_2018_2025/ | tours de qualif et de course (gomme, relais, âge du pneu, stands, statut de piste, météo par tour), messages de direction de course, météo par séance, circuits, virages, calendrier relié à F1DB, tracés bruts 2023 à 2025 | FastF1 via dépôts TracingInsights (MIT, Apache 2.0) ; F1DB pour les manches | 2018 à 2025, 173 GP | à jour ; anomalies listées dans la notice | fastf1_2018_2025/fastf1_2018_2025_lisezmoi.md |
| penalites_grille_2014_2025.csv | 493 pénalités de grille et départs des stands : valeur F1DB, qualification, grille, recul effectif, classe | F1DB (CC BY 4.0) | 2014 à 2025 | à jour ; cause absente | 5_notes/penalites_grille_stats.md |

## 5_notes

| Fichier | Contenu | Date | Statut |
| --- | --- | --- | --- |
| reglement_sportif_2023_2025_releve.md | règlements sportifs et techniques 2023 à 2025 : barème, pneus, SC, VSC, drapeau rouge, DRS, carburant | 21/10/2026 | à jour |
| veille_biblio_strategie.md | 15 sources lues, valeurs, critiques, 54 amendements aux prompts | 20/10/2026 | référence ; amendements arbitrés dans la synthèse (annexe B) |
| notes_montecarlo_heilmeier_2020.md | lois des SC, VSC, pannes, envol, immobilisation 2014 à 2019, code TUM | 20/10/2026 | référence |
| notes_vse_heilmeier_2020.md | VSE : entrées de la décision d'arrêt, cibles de comportement | 19/10/2026 | référence ; **à copier depuis le projet** |
| chainbear_strategie_f1_releve.md | concepts (blocs, perte au stand, undercut, overcut, météo), relevé plan par plan | 19/10/2026 | référence conceptuelle |
| synthese_enjeux_realisme.md | enjeux de réalisme, fenêtres de calibration, décisions du 20/10, règlement 2026 | 20/10/2026 | **à mettre à jour** : centrée sur 2026, antérieure aux décisions du 21/10 ; annexe A et section 6 toujours utiles |
| sources_donnees_strategie_f1.md | sources de données, pièges, grandeurs à dériver | 19/10/2026 | **à mettre à jour** : ne couvre ni les sources repérées le 21/10 (section suivante), ni la couverture par saison |
| penalites_grille_stats.md | fréquence et places perdues des pénalités de grille, par classe, saison, pilote, GP ; règles 2023 à 2025 ; pistes pour les jetons | 21/10/2026 | à jour |

## 6_prompts

| Fichier | Statut |
| --- | --- |
| prompt_jeu.md | version du 20/10/2026, **à copier depuis le projet** ; **à réécrire** (saisons 2023 à 2025, mode saison, pneus par rôle, DRS au lieu du mode dépassement, carburant sans plafond réglementaire, drapeau rouge selon le règlement 2023 à 2025) |
| prompt_calibration.md | version du 20/10/2026, **à copier depuis le projet** ; **à réécrire** (fenêtres par famille de paramètres sur l'ère hybride, Jolpica et base TUM dans la pile, Track DNA par saison, composés par rôle, indicateur « avant Miami » à revoir selon la place de 2026) |

Versions du 19/10/2026, remplacées : dossier voisin `projet sratf1/archive/` (`prompt_jeu_2026-10-19.md`, `prompt_calibration_2026-10-19.md`), laissé en place.

## Sources en ligne repérées, non téléchargées

| Source | Contenu utile | Couverture | Accès, licence | Usage prévu |
| --- | --- | --- | --- | --- |
| FastF1 (docs.fastf1.dev) | tours, pneus (rôle par GP), arrêts, statut de piste, messages de direction de course, météo de séance, télémétrie et positions | 2018 et après ; résultats depuis 1950 via Jolpica | Python, gratuit ; API bloquée par le proxy (cloud et VM) | extrait via TracingInsights (4_donnees/fastf1_2018_2025) |
| Jolpica-F1 (api.jolpi.ca), successeur d'Ergast | calendriers, résultats, grilles, qualifications, temps au tour (depuis 1996), arrêts (depuis 2011) | 1950 et après | API REST, limite de débit | écarté le 21/10/2026 : F1DB et base TUM couvrent le besoin |
| OpenF1 (openf1.org) | arrêts avec durée d'immobilisation (champ stop_duration, couverture à vérifier), dépassements (bêta), radio, intervalles | 2023 et après | API REST gratuite pour l'historique ; 3 requêtes/s, 30/min | extrait (4_donnees/openf1_2023_2025) |
| F1DB (github.com/f1db/f1db) | base complète ; version de tracé de chaque course (circuitLayoutId) ; tracés en SVG | 1950 et après | CC BY 4.0, SQLite | versions de tracé, contrôle des résultats |
| TracingInsights (github.com/TracingInsights) | JSON par séance générés avec FastF1 ; tables des SC, drapeaux rouges et estimations de VSC | 2018 et après ; tables historiques depuis 1950 | dépôt 2026 sous Apache-2.0 ; autres licences à vérifier | cache FastF1, causes des SC avant 2018 |
| TUM f1-timing-database et race-simulation (github.com/TUMFTM) | base SQLite (gommes, phases de neutralisation, abandons) ; paramètres de 121 courses | 2014 à 2019 | CC BY-NC-SA 3.0 et LGPL-3.0 | extrait (4_donnees/tum_2014_2019) |
| FIA, « Race Pit Stop Summary » (un PDF par course, fia.com) | chaque arrêt : tour, heure, durée dans la voie des stands | 2014 et après | public | arrêts 2014 à 2017 |
| FIA, notes d'épreuve | vitesse dans la voie des stands, zones DRS | par GP | public | contrôle optionnel |
| Pirelli (press.pirelli.com) et F1.com (« What tyres will the teams and drivers have... ») | composés par GP, limites de tours par train | 2023 à 2025 | public | déjà exploités dans compound_allocations.csv |
| julesr0y/f1-circuits-svg ; bacinger/f1-circuits | versions de tracé en SVG ; tracés géoréférencés en GeoJSON (35 circuits) | tous circuits | bacinger : MIT | tracés, placement de la météo |
| Open-Meteo (open-meteo.com) | archive horaire : ERA5 depuis 1940, modèle IFS à 9 km depuis 2017 | 1940 et après | CC BY 4.0 | extrait (4_donnees/meteo_open_meteo) |
| Open-Meteo, Previous Runs API | prévisions archivées à échéance fixe de 1 à 7 jours | depuis janvier 2024 (GFS depuis mars 2021) | même licence qu'Open-Meteo | extrait (4_donnees/meteo_open_meteo), 48 week-ends 2024 à 2025 |
| F1.com, « Pirelli Strategy Guide » (un article par GP) | stratégies jugées les plus rapides avant la course ; contenu chiffré à vérifier (lecture partielle) | 2023 à 2025 | public | contrôle du planificateur et du plan d'avant course de l'IA |
| Jolpica, grille et qualifications | écart entre place de qualification et place sur la grille (pénalités de grille réelles) | 2014 et après | API REST | remplacé par F1DB (penalites_grille_2014_2025.csv) ; contrôle éventuel |
| FIA, décisions des commissaires (fia.com, documents par GP) | cause de chaque pénalité de grille (moteur, sportive, parc fermé) | par GP | public | optionnel : cause des pénalités, absente de F1DB et des messages de direction de course |
| Meteostat (meteostat.net) | observations horaires de stations (SYNOP, METAR) | variable selon la station | données sous résolution 40 de l'OMM ; bibliothèque Python | écarté le 21/10/2026 : station du circuit déjà dans FastF1, climat par Open-Meteo |
| DHL Fastest Pit Stop | 10 arrêts les plus rapides par GP seulement | 2015 et après | public | écarté : échantillon biaisé |

## Anomalies et points ouverts

- `track_dna_2026.csv`, Spa-Francorchamps : 20 virages annoncés, mais 4 + 6 + 9 = 19. La carte du site calcule ses pourcentages sur 19.
- Track DNA 2025 sur le site : valeurs permutées entre Espagne et Canada, et entre Belgique et Hongrie ; corrigées dans le CSV.
- Track DNA 2023 : aucune donnée ; moyenne du circuit sur 2024 à 2026.
- Spécifications obligatoires de course par GP : introuvables (NA dans compound_allocations.csv).
- Prompts et synthèse antérieurs aux décisions du 21/10.
- Accès réseau (21/10/2026) : API Jolpica, FastF1 (livetiming), OpenF1, Open-Meteo et Meteostat bloquées depuis le cloud et depuis la VM ; GitHub accessible par git. Contournement retenu : script lancé sur le PC (`_extraction_api/`). Autre possibilité : ajouter les domaines dans les paramètres claude.ai (Capacités).
- Pénalités de grille : cause inconnue (ni F1DB ni messages de direction de course) ; 7 valeurs de 1 et 2 places en 2023 à 2025 de nature non vérifiée.
