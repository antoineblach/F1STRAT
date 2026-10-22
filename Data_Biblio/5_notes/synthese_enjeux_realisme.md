# F1STRAT : enjeux de réalisme

Synthèse du corpus Data_Biblio et des documents du projet, 20/10/2026. Périmètre : les choix de modélisation qui conditionnent le réalisme. Pas de game design.

Ce document remplace la lecture croisée des notes existantes ; il ne les remplace pas comme sources détaillées (pages, tableaux, critiques) : il renvoie vers elles.

Conventions :
- **[É]** établi : lu dans la source citée (texte, tableau ou code). « secondaire » = presse spécialisée, pas le règlement ni l'article d'origine.
- **[D]** déduit : calcul ou raisonnement de ma part à partir de valeurs établies.
- **[H]** hypothèse : choix de modélisation, valeur d'exercice ou estimation d'auteur sans mesure.
- **[V]** à vérifier sur une source primaire.
- Ères : **14-19** = 2014 à 2019 (V6 hybride, DRS, 100 à 110 kg de carburant, base TUM) ; **23-25** = effet de sol ; **26** = règlement 2026.

---

## 1. État du dossier

### 1.1 Carte des fichiers

| Fichier | Emplacement | Contenu | Statut |
| --- | --- | --- | --- |
| veille_biblio_strategie.md | Data_Biblio et projet | 15 sources lues, valeurs, critiques, 54 amendements aux deux prompts (25 calibration, 29 jeu) | référence bibliographique ; amendements non appliqués (annexe B) |
| notes_montecarlo_heilmeier_2020.md | Data_Biblio et projet | lois SC, VSC, pannes, envol, immobilisation 14-19, code TUM | référence |
| notes_vse_heilmeier_2020.md | projet seulement | VSE : entrées de la décision d'arrêt, cibles de comportement | référence |
| chainbear_strategie_f1_releve.md | Data_Biblio et projet | concepts (blocs, pit delta, undercut, overcut, météo), relevé plan par plan | référence conceptuelle ; valeurs chronométrées à la main |
| sources_donnees_strategie_f1.md | Data_Biblio et projet | sources de données, pièges, grandeurs à dériver | partiellement dépassé (1.2) |
| prompt_jeu.md, prompt_calibration.md | projet seulement | prompts Claude Code | réécrits le 20/10 (décisions, arbitrage, règlement 2026) ; versions du 19/10 dans projet sratf1/archive/ |
| Règlement FIA 2026 (A, B, C) et 2027 (B, C) | Data_Biblio seulement | PDF | articles relevés en section 6 ; à copier dans docs/reglement/ du dépôt |
| track_dna_2026.csv | projet seulement | notes 1 à 5 par circuit, 17 GP 2026 | GP restants du calendrier absents |
| race_review_tracks_2023_2026.csv | Data_Biblio et projet | interruptions, changements de position, pluie par circuit | moyennes qui mélangent 23-25 et 26 |
| 8 PDF | Data_Biblio seulement | articles sources | contrôlés par sondage (1.3) |
| CB Vid/ | Data_Biblio seulement | vidéo, audio (environ 32 Mo), sous-titres Chain Bear | seuls les sous-titres en-GB servent encore ; hors dépôt git |

### 1.2 Corrections à reporter dans les documents existants

1. **Bahreïn 2026 à Sepang.** prompt_calibration.md classe en anomalie la ligne « Bahrain Grand Prix » au nom court « Kuala Lumpur ». Ce n'en est pas une : le GP de Bahreïn 2026, annulé pour raisons de sécurité (conflit au Moyen-Orient), a été couru à Sepang du 2 au 4 octobre 2026 sous son nom d'origine ; le GP d'Arabie saoudite 2026 est annulé sans remplacement [É secondaire, F1Technical]. La ligne « Sepang;BH » de race_review est cohérente. Conséquence [D] : le fichier de correspondance doit rattacher l'événement « Bahrain Grand Prix » 2026 à Sepang, et aucune donnée Sakhir 23-25 ne doit lui servir d'historique.
2. **DRS 2026 : tranché.** Les deux prompts laissent la question ouverte. Le règlement 2026 ne prévoit plus de DRS ; détail des articles en section 6 [É règlement]. À sa place :
   - l'aileron actif (« Driver Adjustable Bodywork », B7.1) : mode « ligne droite » activable par toutes les voitures dans les zones d'activation du circuit quand la direction de course l'autorise, sans condition d'écart ; activation partielle seulement en conditions de faible adhérence ;
   - le mode dépassement (« Overtake », B7.2.2, B7.2.3, C5.2.8 ii, C5.2.10 iii) : activé si la voiture passe la ligne de détection à moins de l'écart de détection de la voiture devant ; il donne une courbe de puissance ERS-K prolongée (350 kW jusqu'à 337,5 km/h au lieu de 290 km/h [D, formules C5.2.8]) et jusqu'à 0,5 MJ de recharge supplémentaire sur le tour. La presse parlait de « +0,5 MJ à déployer » : c'est une recharge supplémentaire autorisée ;
   - le boost : augmentation de la puissance demandée à la discrétion du pilote (C5.12.5).
3. **Masse de carburant 2026.** La section C 2026 (issue 21) ne fixe aucune masse maximale de carburant en course [É sur l'absence, recherche plein texte] ; elle limite le débit d'énergie du carburant à 3 000 MJ/h (C5.2.3 à C5.2.5). La masse au départ est donc un choix d'équipe. « Environ 70 kg » (Chain Bear, PlanetF1) est un ordre de grandeur de consommation, pas une limite [H]. Ne pas reprendre 110 kg (maximum 2022 à 2025) pour 2026.
4. **sources_donnees_strategie_f1.md, points non vérifiés.** Code du VSE : public (TUMFTM/race-simulation, LGPL-3.0) [É]. Codes TrackStatus 1, 2, 4, 5, 6, 7 : ce sont aussi ceux de Dinh et al. 2026, ce qui corrobore sans prouver [V doc FastF1]. Variable de pluie dans l'archive Open-Meteo : toujours [V].
5. **Monaco 2026.** La règle de deux arrêts obligatoires, propre à l'édition 2025, est supprimée pour 2026 [É secondaire, PlanetF1, 28/02/2026]. Le règlement 2026 ne prévoit pour Monaco qu'une distance réduite à 260 km (B2.5.2 b) et aucune règle de pneus particulière (B6.3.6) [É règlement]. Les données Monaco 2025 (deux arrêts imposés) ne sont pas représentatives de la stratégie libre.
6. **Âge normalisé au changement de pneus (VSE, tableau 3).** Les notes reprennent la ligne « toutes saisons » (dur 38,8 %, médium 34,1 %, tendre 29,5 %). La ligne « 2016 et après » (38,8 %, 34,6 %, 31,6 %) correspond aux règles de nomination à trois composés par GP, plus proches des règles actuelles [É] : c'est elle qu'il faut comparer à 23-26.

### 1.3 Fiabilité du corpus

- Sondage du 20/10 : environ 70 valeurs des notes relues dans les PDF (Monte-Carlo 2020, VSE 2020, ITSC 2018, Carrasco Heine et Thraves 2023, Dinh et al. 2026). Aucun écart, hormis la nuance du point 1.2.6.
- Non recontrôlé ici : Choo 2015 et Tulabandhula et Rudin 2014 (NASCAR, transfert faible), McLaren RAEng (exercice), et les sources lues en ligne seulement (Fieni, Cappello, Liu, Aversa, Phillips, page McLaren).
- Les critiques de la veille (conclusions qui dépassent les éléments chez Choo, Tulabandhula, Dinh, Carrasco Heine) restent valables ; elles ne sont pas reprises ici.

---

## 2. Constat structurant : un jeu 2026 calibré avec des sources d'autres ères

### 2.1 D'où viennent les chiffres
- Presque toutes les valeurs mesurées du corpus portent sur 14-19 (TUM : 121 courses ; Phillips : 2014). Les autres sont des instances synthétiques ou des exercices (Carrasco Heine et Thraves, Fieni, McLaren RAEng). Aucune source relue ne porte sur 2026 [É].
- La calibration prévue s'appuie sur FastF1 23-26 [É prompts].

### 2.2 2026 change les quatre leviers de la stratégie [É secondaire]
- **Pneus** : 18 pouces plus étroits, gamme C1 à C5, C6 abandonné (Pirelli, 24/11/2025). Développés sur simulations d'écuries, sans voiture 2026 réelle. Dégradation « assez faible », surtout en début de saison : au 28/09/2026, 9 GP sur 15 courus en un arrêt pour l'essentiel du plateau, vainqueur compris ; Hongrie gagnée en trois arrêts ; pneus plus dégradants prévus pour 2027 (The Race).
- **Carburant** : environ 70 kg par course (1.2.3).
- **Dépassement** : DRS supprimé, aileron actif pour tous, mode dépassement par l'énergie (1.2.2).
- **Énergie** : MGU-K de 350 kW ; recharge au freinage, à charge partielle, par écrêtage en bout de ligne droite (« super clipping ») et par lift and coast ; boost et mode dépassement au déploiement (The Race).

### 2.3 Rupture interne à 2026
Mesures annoncées le 20/04/2026 pour s'appliquer à partir du GP de Miami (3 mai), sous réserve d'un vote électronique du Conseil mondial [É secondaire, Motor Sport Magazine ; confirmées pour Miami selon un titre de Sky Sports, article non lu] :
- recharge maximale en qualification de 8 à 7 MJ ;
- puissance de super clipping de 250 à 350 kW, aussi en course ;
- boost plafonné à +150 kW au-dessus de la puissance du moment ;
- déploiement MGU-K à 350 kW dans les zones d'accélération, 250 kW ailleurs ;
- pluie : couvertures chauffantes des intermédiaires plus chaudes, déploiement ERS maximal réduit.

Les GP courus avant Miami (Australie, Chine, Japon [D, ordre de track_dna et annulations d'avril]) ne sont pas homogènes avec la suite pour l'énergie et le rythme.

Le texte en vigueur (section C, issue 21 du 19/10/2026) fait foi sur la presse : recharge limitée à 8,5 MJ par tour, réductible à 7 MJ par compétition sur décision de la FIA et jusqu'à 4 MJ en qualification (C5.2.10) ; courbe de puissance à 250 kW sur des secteurs désignés en course (C5.2.8 iii) ; écart d'état de charge de 4 MJ au plus (C5.2.9) [É règlement].

### 2.4 Conséquence : une fenêtre de calibration par paramètre
Chaque paramètre se range selon sa dépendance à l'ère technique [D]. Pour les paramètres liés à la voiture, 2026 n'offre qu'une course par circuit (17 à ce jour dans track_dna) : les valeurs par circuit seront bruitées. Le modèle groupé (dégradation = d_C × s_circuit) et les archétypes de circuits deviennent la voie principale, pas une option.

| Paramètre | Dépend de l'ère technique | Fenêtre proposée [D] |
| --- | --- | --- |
| Géométrie, voie des stands | non | toutes saisons ; vitesse limite 80 km/h sauf exception (B1.6.3 a) |
| Perte au stand en vert | faiblement (vitesse en piste) | 23-26, contrôle sur 26 |
| Rapports de perte VSC/vert et SC/vert | non (procédures) | 23-26 ; 14-19 en contrôle |
| Taux, causes et durées SC, VSC, drapeau rouge | en partie (fiabilité) | 23-26 ; 14-19 en a priori étiqueté |
| Climat, pluie | non | le plus d'années possible |
| Immobilisation au stand | faiblement | 23-26 |
| Bruit pilote, envol | faiblement | 23-26 |
| Dégradation, écarts entre composés, falaise | oui | 26 seul, modèle groupé |
| k_fuel (s/kg) | non (physique) ; masse de départ : oui | k_fuel 23-26 ; masse 26 |
| Difficulté de dépassement, air sale | oui | 26 seul |
| Fiabilité par écurie | oui (nouveaux moteurs) | 26, a priori 23-25 |
| Énergie | oui, et sous-ère d'après Miami | 26, écart avant et après Miami estimé à part (décision 8) |
| Comportements stratégiques (cibles de l'IA) | oui pour les niveaux (nombre d'arrêts, composés) | niveaux : 26 ; comportements conditionnels (réaction à une SC, à un undercut) : 23-26 si l'effectif 26 est insuffisant |

---

## 3. Enjeux par phénomène

### 3.1 Temps au tour et dispersion
- Structure additive commune à toutes les sources : base + pneus + carburant + voiture + pilote + premier tour + arrêt [É TUM, Phillips, McLaren, Carrasco Heine]. Notre modèle la reprend.
- Bruit pilote : σ de 0,458 à 0,855 s (14-19, écarts à un polynôme de degré 2 par relais, hors deux premiers tours, tours d'arrêt et de neutralisation) ; 0,2 à 0,7 s chez Phillips 2014, autre méthode [É].
- Enjeu : σ règle la part de hasard dans l'écart entre deux stratégies proches, donc la lisibilité d'une bonne décision. Recalcul 23-26 avec la méthode TUM.
- Erreur ponctuelle (prompt_jeu) : aucune source chiffrée [H]. Piste [D] : la calibrer sur la queue haute des résidus, que Cappello et Hoegh modélisent par une loi t asymétrique [É].

### 3.2 Pneus
**Pourquoi** : la dégradation fixe le nombre d'arrêts, la fenêtre d'undercut et la valeur d'un arrêt sous neutralisation.

**Établi**
- Formes publiées : linéaire (121 fichiers TUM) ; logarithmique, jugée plus fidèle que la quadratique (ITSC 2018) ; quadratique (Phillips) ; linéaire à pente croissante (Cappello et Hoegh : 0,054 à 0,060 s/tour, incrément 0,010 à 0,011, une seule course 2025) ; spline avec falaise (Carrasco Heine et Thraves, exemple +1,2 s à 70 % d'usure) [É]. Aucune n'est ajustée sur 2026.
- Ordres de grandeur 14-19 : pentes linéaires de 0,013 à 0,050 s/tour selon pilote et gomme (Abu Dhabi 2017) [É].
- Pneus froids : +1,0 s au premier tour de chaque relais, valeur unique du code TUM [É code, H sur le fond].
- 2026 : dégradation faible et majorité de courses à un arrêt (2.2) [É secondaire].

**Ce que les données ne donnent pas** [D]
- Les données publiques donnent des temps au tour, pas une usure : l'usure du jeu est une variable latente.
- La falaise s'observe à peine, les équipes s'arrêtant avant : le seuil issu des données (quantile 95 % de l'âge à l'arrêt) est une borne basse.
- La dégradation mesurée est celle du rythme que les équipes ont choisi de tenir (gestion des pneus comprise), pas une propriété physique du pneu. Le mode de pilotage « neutre » du jeu doit donc correspondre au régime observé ; les autres niveaux sont des extrapolations [H].

**Hypothèses en place**
- Couplage usure et masse de carburant, (1 + δ)^(m / m_max) : δ = 0,2 dans l'exemple de Carrasco Heine et Thraves, 0,1 dans leur code ; coefficient « heuristique, faute de données » chez Fieni [É]. **Aucune source ne le mesure.** C'est pourtant ce couplage qui rend l'ordre des relais significatif et justifie la programmation dynamique par relais plutôt que le MIQP du VSE [D].
- Usure sous VSC et SC à 50 % et 25 % : estimations des auteurs TUM [H].

**Ouvert**
- Le diagnostic prévu (pente selon le tour de départ du relais) confond couplage carburant et évolution de la piste [É veille] : δ restera une hypothèse.
- L'arbitrage rythme contre usure, levier principal du pilote en course, n'est chiffré par aucune source du corpus [É sur l'absence] ; dans le jeu, il passe entièrement par les 5 niveaux du mode [H].

### 3.3 Carburant et énergie
**Établi**
- k_fuel : 0,017 à 0,045 s/kg, médiane 0,031 (121 fichiers TUM) ; 0,033 s/kg (Abu Dhabi 2017, ITSC 2018) ; 0,03 s/kg (exercice McLaren et instance Carrasco Heine) [É].
- k_fuel et évolution de la piste ne se séparent pas par régression (colinéaires) [É prompt_calibration].
- Sous-remplissage du réservoir et économie en milieu de course : pratique citée par Chain Bear, sans chiffre [É qualitatif].

**Déduit**
- Avec environ 70 kg et 0,031 s/kg : environ 2,2 s d'écart entre premier et dernier tour.
- Sans ravitaillement, l'effet carburant est le même pour toutes les stratégies d'arrêt : il ne les départage que par le couplage usure-masse (3.2) et par le mode [D veille].

**Énergie 2026**
- Le prompt du jeu met « ERS distinct du mode de pilotage » hors périmètre.
- En 2026, l'énergie est un levier d'attaque et de défense tour par tour (boost, mode dépassement) et une source d'écarts de vitesse de rapprochement entre voitures dans des états de batterie différents ; The Race relie à ce phénomène l'accident de Bearman au Japon [É secondaire].
- Si l'énergie reste agrégée dans le mode, le modèle de dépassement doit en absorber l'effet de façon statistique [D].
- Données : FastF1 ne fournit pas, à ma connaissance, l'état de la batterie [V] ; l'effet ne se lit qu'indirectement, sur les profils de vitesse en bout de ligne droite. La vitesse aux pièges reflète en 2026 l'énergie déployée autant que la voiture [D] : à utiliser avec prudence comme attribut voiture (amendement de la veille).

### 3.4 Arrêts aux stands
- **Perte en vert**, hors immobilisation : 14,1 à 24,6 s, médiane 18,3 s (121 fichiers TUM) [É code]. Chain Bear : Monza 22 s, Monaco 19,5 s, Silverstone 23 s, chronométrés sur images [É, imprécis].
- **Perte sous neutralisation** : rapport VSC/vert médiane 0,60 (0,29 à 0,77) ; SC/vert médiane 0,54 (0,18 à 0,88), une partie étant des substituts de circuits voisins [É code]. Mesures vidéo 2018 et 2019 sur 4 circuits (tableau 6 du Monte-Carlo) ; Monaco 14 s sous VSC et 12 s sous SC chez Chain Bear [É].
- Le facteur unique 0,5 de la littérature est rejeté par TUM : la perte sous neutralisation dépend du tracé [É]. Notre calcul par la géométrie va dans ce sens [D].
- **Immobilisation** : loi log-logistique par écurie, ajustée sur l'écart à l'arrêt le plus court de la course (écarts de 4 s au plus) ; minimum de 1,9 s dans le code [É]. Arrêts ratés au-delà : loi séparée [H]. FastF1 ne donne pas l'immobilisation seule [V] : PitOutTime − PitInTime inclut le roulage.
- **Seuil d'un arrêt supplémentaire** : 2 s minimum dans le VSE, pour couvrir le risque d'arrêt raté [É, choix des auteurs].
- **Règles** (section 6) : au moins deux spécifications sèches en course, dont une spécification « obligatoire course » désignée par la FIA (B6.3.6) ; non-respect = disqualification, ou +30 s si la course est suspendue sans reprise ; vitesse limite 80 km/h, modifiable par la direction de course (B1.6.3 a) ; sous VSC et SC, entrée aux stands autorisée seulement pour changer de pneus (B5.12.3, B5.13.3).
- **Inventaire de trains** [É B6.2.4, B6.3.8 ; D] : 2 durs, 3 médiums, 8 tendres par pilote sur un week-end standard (2, 4, 6 en format sprint), dont 2 trains des spécifications obligatoires gardés pour la course. Le nombre de trains neufs de chaque composé disponibles au départ contraint réellement la stratégie ; le prompt ne prévoit qu'un âge de pneu au départ.

### 3.5 Dépassement et trafic
**Pourquoi** : la difficulté de dépasser fixe la valeur de la position en piste, donc celle de l'undercut, de l'overcut et de la recherche d'air libre. C'est le paramètre le plus influent sur la stratégie et le moins transférable d'une ère à l'autre [D]. Cas Ferrari, Abu Dhabi 2010 : décision perdante faute d'avoir intégré la difficulté de dépasser, que l'outil ne permettait pas de réviser en course [É Aversa et al.].

**Établi**
- TUM, 14-19 (code) : le suiveur passe si son avance projetée dépasse t_gap_overtake (1,26 à 3,75 s, médiane 2,03 s ; Monaco et Singapour 3,75 ; Silverstone 1,35), diminué de 0,009 à 0,061 s par km/h d'avance en vitesse de pointe ; écart minimal 0,5 s (0,8 s derrière la SC) ; 0,3 s de duel aux deux voitures, 0,3 s de plus au dépassé [É].
- Phillips 2014 : seuil de 1,2 s, réduit de 0,2 s par 10 km/h ; DRS 0,4 s net par tour ; usure ×1,1 en air sale ; seuil réglé pour reproduire environ 45 dépassements par course sèche [É].
- Critique des modèles par secteurs (Bekker, via ITSC 2018) : dépassement bouclé dans un seul secteur, difficulté par secteur impossible à régler avec des données publiques [É]. D'où les zones multi-micro-secteurs et la difficulté par circuit proposées par la veille.
- En tête de course, air libre et voiture plus rapide se confondent (Tulabandhula et Rudin, fig. 4) [É] : la pénalité de trafic se mesure à l'intérieur d'un même pilote.
- 2026 : DRS supprimé, mode dépassement (1.2.2, section 6) [É règlement].

**Problèmes de données** [D]
- race_review compte tous les changements de position (arrêts compris), en moyenne sur 23-26 : deux ères mélangées, et une définition différente de nos dépassements en piste.
- track_dna_2026 contient une colonne « drs » alors que le DRS n'existe plus en 2026 ; sens à établir [V] (zones de mode ligne droite ?). Vide pour Madring et Sepang.
- Avec une course par circuit en 2026, la difficulté par circuit se calibre par la courbe « dépassements par course en fonction de la difficulté » (méthode Phillips), régularisée par les notes Track DNA et les archétypes.

### 3.6 Neutralisations
**Pourquoi** : un arrêt sous SC coûte environ la moitié d'un arrêt en vert (rapport médian 0,54) [D] ; la réaction au premier tour de neutralisation et l'attente d'une SC sont des décisions fréquentes.

**Établi, 14-19 (TUM, Monte-Carlo)**
- Nombre de SC par course : 0 : 45,5 % ; 1 : 41,3 % ; 2 : 9,9 % ; 3 et plus : 3,3 %.
- 36,4 % des SC commencent au premier tour (part des SC, pas des courses).
- Durée de SC de 2 à 8 tours, espérance 3,99 tours [D].
- VSC causées uniquement par des pannes dans le modèle : P(VSC | panne) = 0,227 (2015 à 2019) ; durée 1 à 4 tours.
- Rythme : environ 140 % du tour normal sous VSC, 160 % sous SC.
- Comportements (VSE) : arrêt le plus souvent au premier tour de neutralisation ; une SC vers 17 % de course ne déclenche pas d'arrêt dans leur exemple ; le leader décide souvent autrement que ses poursuivants.

**Autres sources**
- Méthode d'écurie (McLaren, lecture indirecte) : historique du GP, causes pondérées, pluie passée ignorée si le sec est annoncé, événements isolés exclus [É].
- Anticipation : la programmation dynamique stochastique de Carrasco Heine et Thraves retarde les arrêts et gagne environ 1 s en moyenne sur une instance synthétique sans rivaux [É ; portée limitée].
- 23-26 : interruptions moyennes par circuit de 0,2 (Budapest) à 4,0 (Melbourne), SC, VSC et drapeaux rouges confondus (race_review) [É fichier].

**Trou du corpus et du prompt : le drapeau rouge**
- Aucune source du corpus ne traite le drapeau rouge [É sur l'absence] ; le prompt du jeu n'en fait qu'un statut de l'instantané.
- Règle 2026 [É règlement, section 6] : pendant la suspension, les voitures attendent dans la voie rapide dans l'ordre d'arrivée, sans dépassement (B5.14.2) ; changement de roues et de pneus et réparation des dégâts d'accident autorisés (B5.14.4 a vii et viii) ; ordre de reprise pris au dernier point où toutes les positions étaient connues (B5.15.1 b iii) ; les retardataires se dédoublent avant la reprise (B5.15.2 c) ; reprise derrière la SC puis départ arrêté ou lancé au choix de la direction de course (B5.15.4, B5.15.5) ; la durée de suspension s'ajoute à la limite de 2 h, plafond 3 h (B2.5.3 b). Pneus montés pendant la suspension : « utilisés » dès la sortie de la voie (B6.3.2), donc comptés pour la règle des deux spécifications [D].
- Exemple de l'effet : Sao Paulo 2024, où les voitures qui ne s'étaient pas encore arrêtées ont changé de pneus gratuitement [É secondaire, Sky Sports].
- Effet stratégique majeur [D] : modélisé (décision 6).

**Hypothèses**
- Usure et consommation sous neutralisation : estimations [H].
- Déclencheurs causaux (prompt_jeu) plutôt que lois tirées avant la course (TUM) : légitime en temps continu, mais les causes doivent reproduire les marges (nombre par course, part au premier tour, durées) [É veille].

### 3.7 Météo
**Établi**
- Qualitatif seulement (Chain Bear) : croisement slick, intermédiaire, pluie selon l'humidité ; intermédiaire qui surchauffe sur le sec ; variabilité spatiale ; rôle du pilote [É].
- Aucune source du corpus ne chiffre les points de croisement, la vitesse de séchage ou la taille et la vitesse des cellules [É sur l'absence]. Carrasco Heine et Thraves formulent une météo markovienne sans la calculer [É].
- Fréquences de pluie 23-26 par circuit dans race_review ; définition du taux non établie (pluie pendant la course ou pendant le week-end) [V].
- 2026 : en conditions de faible adhérence déclarées, aileron actif partiel, mode dépassement désactivé et courbes ERS propres (B1.5.11, B7.1.2 b, B7.2.2 d, C5.2.8 iv) [É règlement] ; pneus pluie imposés derrière la SC sur décision (B6.3.7).

**Enjeu** [D]
- Le modèle spatial du prompt (cellules, vent, humidité et drainage par micro-secteur, radar) est la partie la plus détaillée du moteur et la moins calibrable : presque tous ses paramètres seront [H].
- Open-Meteo (maille de 9 km, pas horaire) ne résout pas une cellule d'averse.
- Donnée exploitable pour les croisements : tours de transition des courses humides 23-26 dans FastF1 (slicks et intermédiaires sur les mêmes tours).

### 3.8 Départ et premier tour
- Envol mesuré en temps, pas en places, celles-ci faussant les probabilités en tête de grille [É TUM]. Courbe t_s = √(2 d / a) + t_r, avec a = 11,2 m/s² et t_r = 0,2 s ; écart pilote μ de −0,10 à +0,10 s, σ de 0,10 à 0,25 s (14-19) [É].
- Perte au premier tour : médiane 3,82 s plus 0,139 s par place (code TUM) [É] ; 0,25 s par place chez Phillips, dont la dispersion au départ est réglée sur environ 30 changements de position au premier tour [É].
- Avantage du tendre au départ : qualitatif (Chain Bear) ; 63,1 % des départs en tendre de 2016 à 2019 (VSE) [É].
- 2026 : MGU-K utilisable au départ seulement au-delà de 50 km/h, sauf assistance imposée par l'ECU FIA pour garantir une accélération minimale (C5.2.12) [É règlement].

### 3.9 Fiabilité et accidents
- Inférence Beta-Bernoulli, accident rattaché au pilote, panne à l'écurie. 14-19 : accidents de 0,045 à 0,114, pannes de 0,041 à 0,225 par course [É].
- Nouveaux moteurs 2026 : rien dans le corpus [É sur l'absence] ; calibration 26 avec a priori 23-25 [H].
- Dégâts par contact : non modélisés par TUM faute de données ; 1 % par dépassement chez Salminen, sans source [H].

### 3.10 Décisions des équipes (cibles de l'IA)
- Signaux de décision : ceux du VSE (progression de la course et de l'âge du pneu, leader ou poursuivant, composé relatif, sévérité du circuit, statut de neutralisation, arrêts restants, poursuivant qui vient de s'arrêter, écart de moins de 1,5 s) [É].
- Prévisibilité réelle : F1 ≈ 0,59 pour le VSE, qui s'arrête souvent trop tôt ; 0,86 chez Dinh et al., score probablement gonflé par une fuite d'information et un découpage aléatoire par tour [É et critique veille]. Conséquence [D] : à partir de l'état public, les décisions réelles ne sont que partiellement prévisibles ; une IA réaliste reproduit des distributions de comportements, pas l'optimum.
- Fréquence : 3,1 % des tours avec changement de pneus (14-19) ; environ 3 % (2022 à 2025, Dinh et al.) [É].
- Biais de mesure à éviter [É] : variables prises sur l'état connu avant la décision (Dinh) ; paradoxe de Simpson sur les gains de n+1 arrêts et l'effet du trafic (Tulabandhula et Rudin) ; rang artificiel pendant un cycle d'arrêts (idem).
- Leçon Aversa et al. : l'outil de Ferrari ne proposait pas de relais long, ne donnait pas de probabilités et ne permettait pas de réviser la difficulté de dépasser [É].
- Interaction entre rivaux (théorie des jeux) : seule piste identifiée, Aguad et Thraves 2024 (EJOR), non lue.

---

## 4. Décisions à prendre

Décisions d'Antoine du 20/10/2026.

| N° | Question | Éléments | Décision |
| --- | --- | --- | --- |
| 1 | Fenêtre de calibration par paramètre | 2.4 | **retenu** : tableau 2.4 ; 14-19 seulement comme a priori étiqueté |
| 2 | Énergie 2026 | levier réel majeur en 2026 ; pas de donnée directe sur l'état batterie | **retenu** : énergie agrégée dans les 5 niveaux du mode, sauf le mode dépassement (décision 5). Limite connue : boost et recharge ne sont pas des décisions distinctes |
| 3 | Couplage usure-masse | aucune mesure ; justifie la DP par relais | **retenu** : δ marqué [H] ; test de sensibilité : si δ entre 0 et 0,2 ne change pas l'optimum sur les circuits 2026, l'ordre des relais ne compte pas en pratique |
| 4 | Forme de la dégradation | 5 formes publiées, aucune sur 2026 | **retenu** : linéaire + courbure si significative + falaise ; forme logarithmique (ITSC 2018) en contrôle d'ajustement |
| 5 | Aide au dépassement 2026 | DRS supprimé ; mode dépassement (B7.2) | **retenu** : mode dépassement explicite selon B7.2.2 et B7.2.3 ; écart de détection et lignes par circuit (valeurs FIA hors règlement, défaut 1 s [H]) ; difficulté par circuit calibrée sur 26 seul |
| 6 | Drapeau rouge | absent du corpus et du prompt | **retenu** : modélisé selon B5.14 et B5.15 (section 6) |
| 7 | Résolution de la météo | humidité par micro-secteur presque entièrement [H] ; FastF1 donne des temps par secteur | **retenu** : générateur de cellules conservé, humidité résolue par secteur officiel (3 par tour), calibrée sur les tours de transition 23-26 |
| 8 | GP d'avant Miami | énergie et rythme non homogènes | **retenu** : Australie, Chine et Japon gardés partout ; indicateur « avant Miami » en covariable, écart estimé et rapporté avec son intervalle. Limite [D] : chaque circuit n'a qu'une course en 2026, donc l'écart est confondu avec l'effet circuit et avec le développement des voitures ; il n'est estimable qu'à travers les modèles groupés et les a priori de circuit (Track DNA, archétypes). Non significatif : aucune correction appliquée |
| 9 | Cibles de comportement de l'IA | effectif 26 faible | **retenu** : niveaux sur 26 ; comportements conditionnels sur 23-26 avec étiquette d'ère |
| 10 | Amendements de la veille | annexe B | **tranché** : arbitrage du 20/10 en annexe B ; report dans les prompts réécrits en entier |

Conséquences pour les prompts [D] :
- prompt_jeu, Météo spatiale : « humidité par micro-secteur » devient « humidité par secteur officiel » ; le coefficient de drainage passe au secteur ; la pluie locale reste calculée aux positions des micro-secteurs, puis agrégée par secteur. Instantané et tests météo à adapter (une cellule mouille les secteurs dans l'ordre de son passage).
- prompt_jeu, Dépassements : remplacer l'« aide au dépassement » générique par le mode dépassement 2026 (détection, activation, désactivation au départ, à la reprise, sous SC et en faible adhérence : B7.2.2, B7.2.3). Mode ligne droite de l'aileron actif : commun à toutes les voitures, absorbé dans T_ref et les poids des micro-secteurs.
- prompt_jeu, Safety car et VSC : ajouter le drapeau rouge (B5.14, B5.15) ; course qui peut finir sous SC (B5.13.8) ; entrée aux stands sous VSC et SC seulement pour changer de pneus. prompt_calibration : taux et causes des drapeaux rouges par circuit, déjà comptés, à exporter comme loi.
- prompt_jeu, Arrêts : règle des spécifications selon B6.3.6 (spécification obligatoire, disqualification) au lieu d'une pénalité en temps ; inventaire de trains par voiture au départ (composé, âge). prompt_calibration : colonne des spécifications obligatoires dans compound_allocations.csv ; reconstitution des trains disponibles au départ depuis TyreLife et FreshTyre, sinon valeur par défaut [H].
- prompt_jeu, Carburant : pas de masse maximale réglementaire en 2026 ; masse de départ bornée par une capacité de réservoir [H].
- prompt_jeu, Hors périmètre : « ERS distinct du mode de pilotage » reste hors périmètre, avec la mention de la limite (décision 2).
- prompt_calibration, Géométrie : secteurs officiels nécessaires dans l'export de chaque circuit.
- prompt_calibration, Modèle de rythme, Plateau et Événements : indicateur « avant Miami » en covariable dans l'ajustement groupé de la dégradation, dans le delta voiture par écurie et dans les dépassements par course rapportés au modèle de circuit ; écart et intervalle dans le rapport, avec la mention de la confusion avec l'effet circuit et le développement.

---

## 5. À vérifier

Le règlement 2026 a tranché les points de la section B et de la section C (voir section 6). Restent :

**Documents FIA par compétition, hors règlement**
- Écart de détection, lignes de détection et d'activation du mode dépassement, zones d'activation de l'aileron actif, par circuit (B7.1.1 e, B7.2.1 b vii à ix). Défaut : écart de 1 s (presse) [H].
- Spécifications obligatoires de course par GP (B6.1.2 b ii), à reprendre des communiqués Pirelli ou FIA.
- Vitesse limite dans la voie quand elle diffère de 80 km/h (B1.6.3 a).

**Autres**
- FastF1 : codes TrackStatus ; absence d'état batterie ; absence de durée d'immobilisation ; disponibilité des secteurs de commissaires.
- race_review : définitions de rain_rate_pct et de « overtakes ».
- track_dna_2026 : sens de la colonne « drs » ; valeurs vides pour Madring et Sepang ; GP restants du calendrier 2026.
- Open-Meteo : variable de pluie dans l'archive historique.
- Allocations Pirelli 2026 par GP (compound_allocations.csv, à constituer).

---

## 6. Règlement 2026 : articles relevés

Sources : FIA 2026 F1 Regulations, section A (issue 03, 25/06/2026), section B sportive (issue 09, 01/10/2026), section C technique (issue 21, 19/10/2026), PDF déposés dans Data_Biblio. La section F n'a pas été nécessaire : tous les points ouverts sont dans B et C. Références à reporter dans rules.json.

| Sujet | Article | Contenu utile au modèle |
| --- | --- | --- |
| Distance | B2.5.2 | plus petit nombre de tours complets au-delà de 305 km (260 km à Monaco) ; départ derrière la SC : tours retirés |
| Durée | B2.5.3 | 2 h au plus ; suspension ajoutée, plafond 3 h |
| Classement | B2.5.5 | ordre au passage de la ligne ; non classé sous 90 % des tours du vainqueur |
| Voie des stands | B1.6.3 a | 80 km/h, modifiable par la direction de course ; excès en course : 5 s, 10 s, passage ou stop-and-go |
| Pénalités en course | B1.9.5, B1.9.6 | 5 s et 10 s purgées au prochain arrêt (ajoutées au temps si aucun arrêt) ; passage et stop-and-go sous 2 passages de ligne, interdits sous VSC et SC ; dans les 3 derniers tours : +20 s ou +30 s |
| VSC | B5.12 | aucun dépassement, temps minimal par secteur de commissaires ; entrée aux stands seulement pour changer de pneus ; fin annoncée, vert 10 à 15 s après ; tours comptés |
| SC | B5.13 | file à 10 longueurs au plus ; aucun dépassement jusqu'à la ligne après la rentrée de la SC ; entrée aux stands seulement pour changer de pneus ; retardataires autorisés à se dédoubler sur décision ; SC rentrée à la fin du tour suivant ce message ; tours comptés |
| Fin sous SC | B5.13.8 | SC présente au dernier tour : arrivée derrière elle, sans dépassement |
| Suspension | B5.14.2, B5.14.4 | voie rapide dans l'ordre d'arrivée ; pneus et réparation des dégâts d'accident autorisés ; course non reprise : résultat de l'avant-dernier tour avant le drapeau rouge |
| Reprise | B5.15 | ordre au dernier point connu ; dédoublement avant reprise ; tours derrière la SC puis départ arrêté ou lancé |
| Pneus fournis | B6.1.1, B6.1.2 b | 3 spécifications sèches, 1 intermédiaire, 1 pluie ; jusqu'à 2 spécifications sèches obligatoires en course, annoncées 2 semaines avant |
| Allocation | B6.2.4, B6.3.8 | 2 durs, 3 médiums, 8 tendres, 5 intermédiaires, 2 pluie (format standard) ; 2 trains des spécifications obligatoires gardés pour la course |
| Pneus utilisés | B6.3.2 | un train monté dans la voie compte dès que la voiture en sort |
| Règle des spécifications | B6.3.6 | au moins 2 spécifications sèches dont 1 obligatoire, sauf usage d'intermédiaires ou de pluie ; sinon disqualification ; +30 s si course suspendue sans reprise |
| Pluie | B6.3.7, B5.15.2 a | pneus pluie obligatoires derrière la SC sur décision de la direction de course |
| Faible adhérence | B1.5.11 | « Low Grip Conditions » déclarées par la direction de course : aileron actif partiel (B7.1.2 b), mode dépassement désactivé (B7.2.2 d), courbes ERS propres (C5.2.8 iv) |
| Aileron actif | B7.1 | mode ligne droite dans les zones d'activation, quand il est autorisé |
| Mode dépassement | B7.2.2, B7.2.3 | désactivé au départ et à la reprise jusqu'au premier passage du leader sur la ligne de détection ; désactivé sous SC jusqu'à ce que toutes les voitures aient passé la ligne après la rentrée de la SC ; activé à la ligne d'activation si la voiture était à moins de l'écart de détection à la ligne de détection |
| Puissance ERS-K | C5.2.7, C5.2.8 | 350 kW au plus ; sans mode dépassement P = 1800 − 5 v (soit 350 kW jusqu'à 290 km/h) ; avec : P = 7100 − 20 v (350 kW jusqu'à 337,5 km/h) [D pour les vitesses] |
| Recharge | C5.2.9, C5.2.10 | état de charge sur une plage de 4 MJ ; recharge de 8,5 MJ par tour (7 MJ sur décision FIA) ; +0,5 MJ avec le mode dépassement |
| Carburant | C5.2.3 à C5.2.6 | débit d'énergie de 3 000 MJ/h ; aucune masse maximale en course trouvée ; pouvoir calorifique du carburant de 38 à 41 MJ/kg (annexe carburant) |
| Masse minimale | C4.1 | 724 kg plus la masse nominale des pneus en course |

**2027** (section B issue 01, section C issue 04, 19/10/2026) [É règlement] : aucun changement sur les articles ci-dessus de la section B. Section C : débit d'énergie porté à 3 150 MJ/h, puissance ERS-K à 375 kW, plage d'état de charge à 4,5 MJ, recharge de 10 MJ sur certains tours. Hors du périmètre 2026 du jeu ; à reprendre si le jeu passe à 2027.

---

## Annexe A. Valeurs de référence consolidées

Valeurs par défaut ou de contrôle. Aucune n'est une valeur 2026 mesurée.

| Grandeur | Valeur | Ère | Source | Statut |
| --- | --- | --- | --- | --- |
| Bruit pilote σ | 0,458 à 0,855 s ; 0,625 s pilote inconnu | 14-19 | Monte-Carlo, tableau A1 et code | [É] |
| Bruit pilote σ (autre méthode) | 0,2 à 0,7 s | 2014 | Phillips | [É] |
| Pente de dégradation linéaire | 0,013 à 0,050 s/tour | 2017 | ITSC 2018, tableau III | [É] |
| Pente de dégradation (dur, médium) | 0,054 et 0,060 s/tour | 2025, une course | Cappello et Hoegh | [É] |
| Pneus froids | +1,0 s au premier tour du relais | 14-19 | code TUM | [É code, H] |
| Couplage usure-masse δ | 0,1 (code) ; 0,2 (exemple) | synthétique | Carrasco Heine et Thraves | [H] |
| Usure sous VSC, SC | 50 %, 25 % | 14-19 | Monte-Carlo | [H auteurs] |
| Âge normalisé au changement, dur / médium / tendre | 38,8 / 34,6 / 31,6 % | 2016-19 | VSE, tableau 3 | [É] |
| Composé au départ, dur / médium / tendre | 4,4 / 32,5 / 63,1 % | 2016-19 | VSE, tableau 17 | [É] |
| Tours avec changement de pneus | 3,1 % ; environ 3 % | 14-19 ; 22-25 | VSE ; Dinh et al. | [É] |
| k_fuel | 0,017 à 0,045 s/kg, médiane 0,031 | 14-19 | code TUM | [É] |
| Masse de carburant au départ | 100 à 110 kg | 14-19 | code TUM | [É] |
| Masse de carburant par course | environ 70 kg (consommation, pas de limite réglementaire) | 26 | Chain Bear, PlanetF1 ; C5.2.3 | [É secondaire, H] |
| Perte au stand en vert (hors immobilisation) | 14,1 à 24,6 s, médiane 18,3 s | 14-19 | code TUM | [É] |
| Rapport de perte VSC/vert | médiane 0,60 (0,29 à 0,77) | 14-19 | code TUM | [É, en partie substituts] |
| Rapport de perte SC/vert | médiane 0,54 (0,18 à 0,88) | 14-19 | code TUM | [É, en partie substituts] |
| Perte vert / VSC / SC, Catalunya | 19,04 / 10,03 / 7,88 s | 2018-19 | Monte-Carlo, tableau 6 | [É] |
| Perte vert / VSC / SC, Melbourne | 17,85 / 12,95 / 12,61 s | 2018-19 | idem | [É] |
| Perte vert / VSC / SC, Monza | 20,60 / 15,42 / 10,16 s | 2018-19 | idem | [É] |
| Perte vert / VSC / SC, Suzuka | 19,48 / 15,05 / 13,60 s | 2018-19 | idem | [É] |
| Pit delta Monaco vert / VSC / SC | 19,5 / 14 / 12 s | date de mesure non donnée | Chain Bear, chronométré | [É, imprécis] |
| Immobilisation minimale | 1,9 s | 14-19 | code TUM | [É code] |
| Immobilisation : loi | log-logistique par écurie, écarts ≤ 4 s au plus court | 14-19 | Monte-Carlo, tableau A2 | [É] |
| Seuil d'un arrêt supplémentaire | 2 s | 14-19 | VSE | [É, choix] |
| Seuil de dépassement t_gap_overtake | 1,26 à 3,75 s, médiane 2,03 s | 14-19 | code TUM | [É] |
| Effet de la vitesse de pointe | −0,009 à −0,061 s par km/h | 14-19 | code TUM | [É] |
| Écart minimal entre voitures | 0,5 s ; 0,8 s derrière la SC | 14-19 | code TUM | [É] |
| Pertes de duel | 0,3 s aux deux ; +0,3 s au dépassé | 14-19 | code TUM | [É] |
| Usure en air sale | ×1,1 | 2014 | Phillips | [É, H] |
| Dépassements par course sèche (cible de Phillips) | environ 45 | 2014 | Phillips | [É] |
| Mode dépassement | +0,5 MJ de recharge, 350 kW jusqu'à 337,5 km/h, sous l'écart de détection (environ 1 s) | 26 | B7.2, C5.2.8, C5.2.10 ; écart : The Race | [É règlement ; écart H] |
| Vitesse dans la voie des stands | 80 km/h, modifiable | 26 | B1.6.3 a | [É] |
| SC par course 0 / 1 / 2 / 3+ | 45,5 / 41,3 / 9,9 / 3,3 % | 14-19 | Monte-Carlo, tableau A3 | [É] |
| Part des SC au premier tour | 36,4 % | 14-19 | Monte-Carlo, tableau A4 | [É] |
| Durée de SC | 2 à 8 tours, espérance 3,99 | 14-19 | Monte-Carlo, tableau 4 | [É ; espérance D] |
| P(VSC sachant panne) | 0,227 | 2015-19 | Monte-Carlo, éq. 15 | [É] |
| Durée de VSC | 1 à 4 tours | 14-19 | Monte-Carlo, tableau 5 | [É] |
| Rythme sous VSC, SC | 140 %, 160 % | 14-19 | VSE, Monte-Carlo | [É] |
| Interruptions par course | 0,2 (Budapest) à 4,0 (Melbourne) | 23-26 | race_review | [É fichier] |
| Accidents par pilote et par course | 0,045 à 0,114 | 14-19 | code TUM | [É] |
| Pannes par écurie et par course | 0,041 à 0,225 | 14-19 | code TUM | [É] |
| Courbe d'envol | a = 11,2 m/s², t_r = 0,2 s | 2019 | Monte-Carlo, éq. 10 | [É] |
| Envol pilote | μ de −0,10 à +0,10 s, σ de 0,10 à 0,25 s | 14-19 | Monte-Carlo, tableau A1 | [É] |
| Perte au premier tour | médiane 3,82 s + 0,139 s par place | 14-19 | code TUM | [É] |
| Changements de position au premier tour | environ 30 | 2014 | Phillips | [É] |
| Courses à un arrêt pour l'essentiel du plateau | 9 sur 15 | 26, au 28/09 | The Race | [É secondaire] |
| Incertitude sur la position moyenne (IC 95 %) | ±0,31 place (100 tirages), ±0,08 (1 000) | course d'exemple, saison non précisée | Monte-Carlo, tableau 8 | [É] |

---

## Annexe B. Amendements de la veille : modifications avant application

Les amendements de veille_biblio_strategie.md (section « Amendements proposés ») restent valables, avec ces modifications [D] :

1. **prompt_calibration, masse de carburant** : 2026 = pas de masse maximale réglementaire (section 6) ; ordre de grandeur de consommation environ 70 kg [H] ; 2023 à 2025 = 110 kg, maximum réglementaire de l'époque [V, règlement 2025 non lu].
2. **prompt_calibration, entrées** : retirer « Bahrain Grand Prix porte le nom court Kuala Lumpur » des anomalies ; ajouter la correspondance Bahrain Grand Prix 2026 → Sepang.
3. **prompt_jeu et prompt_calibration, aide au dépassement** : remplacer « le DRS a peut-être été remplacé » par la description 1.2.2. L'amendement « aide désactivée pendant N tours après une SC (défaut 2, code TUM) » porte sur le DRS 14-19 : le remplacer par B7.2.2 b et c (désactivation au départ, à la reprise et sous SC, réactivation selon l'article).
4. **prompt_jeu, vitesse de pointe** : préciser qu'en 2026 la vitesse aux pièges dépend de l'énergie déployée ; attribut voiture à extraire sur des tours où l'état d'énergie est comparable, sinon [H].
5. **prompt_calibration, comportements** : comparer l'âge normalisé au changement à la ligne « 2016 et après » du tableau 3 du VSE.
6. **prompt_calibration, Monaco** : exclure Monaco 2025 (deux arrêts imposés) des cibles de comportement et du nombre d'arrêts.
7. **prompt_calibration, sous-ère** : indicateur « avant Miami 2026 » sur les trois premiers GP 2026, en covariable et non en exclusion (décision 8).
8. **prompt_jeu, drapeau rouge** : modélisé (décision 6).
9. **prompt_jeu, difficulté de dépassement** : l'amendement prévoit une calibration « sur les dépassements en piste 2023 à 2026 » ; remplacer par 2026 seul (décisions 1 et 5), le seuil TUM ne servant qu'à l'initialisation.
10. **Citations** : « Heilmeier et al. 2020, tableau 8 » est ambigu. Deux articles de 2020 des mêmes auteurs ont un tableau 8 : celui du VSE (cas de référence à 55 tours) et celui du Monte-Carlo (convergence, ±0,31 place). Citer « VSE » ou « Monte-Carlo », ou le DOI, dans les deux prompts.

### Arbitrage du 20/10/2026

Numérotation : C1 à C25 pour prompt_calibration, J1 à J29 pour prompt_jeu, dans l'ordre de la section « Amendements proposés » de la veille. C2, C20, C21 validés par Antoine ; le reste arbitré par Claude à sa demande.

- **Retenus tels quels** : C1, C2, C4 (optionnel, lot 3), C5, C7 à C14, C16 à C18, C20 à C22, C24, C25 ; J1, J3 (avec le test de sensibilité de la décision 3), J4 à J6, J10 à J13, J16 à J20, J22, J25 à J29.
- **Retenus avec modification** :
  - C3 : modification 1 ci-dessus.
  - C6 : gardé. Évolution de la piste et couplage au carburant sont supposés abaisser tous deux la pente des relais tardifs [H] : une absence de baisse borne δ par le haut. Rapporté comme borne, jamais comme mesure.
  - C15 : rapporté même non significatif (environ 24 circuits).
  - C19 : a priori Beta sur 23-25, a posteriori sur 2026 (décision 1).
  - C23 : seuils de dépassement et pertes repris ; effets DRS gardés comme historique seulement.
  - J2 : 1,0 s par défaut [H] ; la calibration rapporte en contrôle l'écart entre perte au stand mesurée et perte géométrique.
  - J7 : vitesse de pointe par écurie = médiane des vitesses aux pièges sur la course [H, proxy] ; terme mis à 0 si son coefficient n'est pas significatif sur les dépassements 2026.
  - J8 : modification 9 ci-dessus.
  - J9 : modification 3 ci-dessus ; dépassement interdit sous VSC (B5.12.2 c) et derrière la SC (B5.13.2 c).
  - J14 : marges cibles calculées sur 23-26, valeurs 14-19 en contrôle.
  - J21 : N calibré par C14 et C15, 12 tours par défaut.
  - J23 : intervalle fourni dans la sortie du prédicteur ; citation selon la modification 10.
- **Rejeté** : J15 (pas de SC à moins d'un tour de l'arrivée). C'est une contrainte technique du modèle TUM tour par tour, pas une règle : une course peut finir derrière la SC. Remplacé par : SC possible jusqu'à la fin, arrivée derrière la SC si elle est en piste au dernier tour (B5.13.8).
- **Reporté** à la phase game design : J24.
- **Tranché par le règlement 2026** (section 6) : masse de carburant (C3), mode dépassement (J9, décision 5), drapeau rouge (décision 6), vitesse dans la voie, fin de course sous SC (J15), sanction de la règle des spécifications.

---

## Sources ajoutées le 20/10/2026 (presse spécialisée)

- The Race, « Boost, overtake mode, active aero : key 2026 F1 terms explained » : https://www.the-race.com/formula-1/boost-overtake-mode-active-aero-recharge-key-2026-terms-explained
- The Race, « Why key 2026 F1 rules fix will create another problem », 20/04/2026 : https://www.the-race.com/formula-1/why-key-2026-f1-rules-fix-will-create-another-problem/
- Motor Sport Magazine, « 2026 F1 mid-season rule changes : what's been agreed and why », 20/04/2026 : https://www.motorsportmagazine.com/articles/single-seaters/f1/2026-f1-mid-season-rules-changes-whats-been-agreed-and-why/
- The Race, « F1's plan for higher-degradation tyres in 2027 », 28/09/2026 : https://www.the-race.com/formula-1/f1-plan-higher-degradation-tyres-2027-pirelli/
- Pirelli, « The range of compounds for the 2026 season has been set », 24/11/2025 : https://press.pirelli.com/the-range-of-compounds-for-the-2026-season-has-been-set/
- F1Technical, « Formula 1 returns to Sepang as Malaysia to host 2026 Bahrain Grand Prix » : https://www.f1technical.net/news/29047
- PlanetF1, « Explained : the 2026 engine regulations » : https://www.planetf1.com/features/explained-2026-formula-1-engine-regulations
- PlanetF1, « Monaco Grand Prix drops controversial two-stop rule for 2026 season », 28/02/2026 : https://www.planetf1.com/news/monaco-grand-prix-two-stop-rule-scrapped-2026-fia
- Sky Sports, « F1 red flag tyre change rules explained », 05/11/2024 : https://www.skysports.com/f1/news/12433/13248475/f1-red-flag-tyre-change-rules-explained-lando-norris-regulation-complaints-after-sao-paulo-gp-disappointment
