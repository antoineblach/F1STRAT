# Chain Bear, Building an F1 Strategy : relevé plan par plan

19 octobre 2026 · Antoine

## Sources et méthode

Relevé établi à partir de la vidéo en 1080p (15 min 32) et de la piste de sous-titres en-GB, écrite à la main par l'auteur.

- **Vidéo** : « Building an F1 Strategy from the Bare Basics », chaîne Chain Bear ([lien](https://www.youtube.com/watch?v=TNQuUZYHJdE)).
- **Images** : 192 images clés repérées par détection des changements d'affichage, plus 8 états transitoires contrôlés. Chaque écran a été lu visuellement, les petits textes agrandis.
- **Narration** : reformulée en français, idée par idée, à partir des sous-titres en-GB. Le texte exact est dans le fichier `sous-titres.en-GB.vtt`.
- **Textes à l'écran** : entre guillemets, en anglais, tels qu'affichés.
- **Mentions** : « (estimé) » = lecture sur un graphique sans valeur écrite ; « (déduit) » = calculé à partir de la règle annoncée.
- **Codes visuels constants** : rouge = soft, jaune = medium, pastille bleue « P » = arrêt aux stands, « bloc » = unité de temps du modèle.

## 0:00 à 0:26, introduction

L'auteur annonce une approche visuelle et volontairement simplifiée de la stratégie de course.

**À l'écran**

- 0:00 à 0:06 : animation de titre, mot « STRATEGY » en lettres jaunes sur un bandeau gris foncé, puis formes géométriques en transition.
- 0:07 à 0:12 : texte qui s'écrit mot à mot, « VISUAL WAYS OF UNDERSTANDING RACE STRATEGY », en magenta, les deux derniers mots en bleu.
- 0:13 à 0:21 : « KEEPING IT REALLY SIMPLE ».
- 0:24 : le texte se réduit et laisse place à quelques petits carrés rouges.

**Narration**

- La stratégie compte beaucoup en F1 et l'auteur en parle souvent ; il cherche une façon visuelle de comprendre les stratégies de course.
- Il simplifie à l'extrême : ni course de 60 tours, ni modèle statistique d'usure, tout est ramené à des petits carrés.

## 0:26 à 1:28, modèle 1 : course de 10 tours

Avec un soft à 3 blocs par tour et un medium à 4, la stratégie la plus rapide est 9 tours en soft puis 1 en medium : 31 blocs, plus le coût de l'arrêt.

**À l'écran**

- 0:37 : titre « MODEL 1: 10-LAP DRY RACE », axe horizontal « Laps » de 1 à 10.
- 0:46 : deux pneus apparaissent à droite, flanc rouge (soft) et flanc jaune (medium).
- 0:50 : axe vertical « Lap time (blocks) » ; une pile de 3 blocs rouges au-dessus du soft.
- 0:52 : tour 1 en soft, 3 blocs rouges. 0:56 : tours 1 à 5, 3 blocs chacun.
- 1:03 : pile de 4 blocs jaunes au-dessus du medium ; tour 1 en medium, 4 blocs.
- 1:15 : tours 1 à 9 en soft (3 blocs), tour 10 en medium (4 blocs).
- 1:17 : barre de total rouge sous le graphique, « 27 ».
- 1:26 : pastille « P » entre les tours 9 et 10 ; total « 27 | 4 = 31 + P ».

**Narration**

- Course de 10 tours sur le sec. Comme en F1, deux composés sont obligatoires ; seuls le soft et le medium sont retenus.
- Les secondes sont remplacées par des unités : le soft coûte 3 unités par tour, soit 15 après 5 tours ; le medium en coûte 4, un bloc de plus par tour.
- Avec ces seules données et l'obligation des deux pneus, le plus rapide est 9 tours en soft puis 1 en medium : 27 + 4 = 31 unités, plus le temps de l'arrêt, traité ensuite.

## 1:28 à 3:38, modèle 2 : softs limités à 4 tours

Quand le soft ne tient que 4 tours, le one-stop 4 soft + 6 medium fait 36 + P et le two-stop 4 + 4 soft + 2 medium fait 32 + 2P : le two-stop gagne si un arrêt coûte moins de 4 blocs.

**À l'écran**

- 1:32 : titre « MODEL 2: 10-LAP DRY RACE (SOFTS LAST 4 LAPS) ».
- 1:44 : légende à droite, « Softs : 4 lap max, 3 blocks/lap » et « Mediums : 10 lap max, 4 blocks/lap ».
- 1:46 : 4 tours en soft, pastille « P » après le tour 4, barre « RACE TIME » sous le graphique.
- 1:56 à 1:59 : 6 tours en medium ; « RACE TIME 12 | 24 = 36 + P ».
- 2:00 à 2:22 : seconde ligne pour 3 tours soft + 7 medium, « 9 | 28 = 37 + P », sous « 12 | 24 = 36 + P ».
- 2:37 à 2:49 : two-stop, 4 tours soft, P, 4 tours soft, P, 2 tours medium ; barre « 12 | 12 | 8 ».
- 2:59 : « 12 | 12 | 8 = 32 + PP » au-dessus de « 12 | 24 = 36 + P ».
- 3:11 : équation « 36 + P = 32 + PP ».
- 3:23 : « 4 = P », puis « P longer than 4: do a one-stop ».
- 3:33 : ajout de « P shorter than 4: do a two-stop ».

**Narration**

- Nouvelle contrainte : le soft garde 3 blocs par tour mais meurt après 4 tours, sans usure progressive à ce stade ; le medium tient les 10 tours.
- One-stop 4 soft + 6 medium : 12 + 24 = 36, plus l'arrêt. Avec seulement 3 tours de soft : 9 + 28 = 37, un peu plus long.
- Pouvoir faire 9 tours en soft ferait gagner 5 blocs sur le meilleur one-stop. C'est impossible, mais deux arrêts permettent 8 tours de soft : 12 + 12 + 8 = 32, plus deux arrêts.
- En retirant 32 et un arrêt de chaque côté, les deux stratégies s'égalisent pour un arrêt de 4 unités. Au-dessus, le one-stop gagne ; en dessous, le two-stop.
- Les chiffres sont exagérés (un arrêt aussi long qu'un tour), mais le choix dépend toujours du coût de l'arrêt.

## 3:38 à 5:08, le pit delta

Le pit delta est le temps passé dans la voie des stands moins le temps du même tronçon en piste ; l'auteur l'estime à 22 s à Monza, 19,5 s à Monaco et 23 s à Silverstone.

**À l'écran**

- 3:44 : titre « THE PIT DELTA » ; « Delta = Δ », complété à 3:45 par « = difference/change ».
- 3:50 : « Pit Delta = time difference between normal lap and pit lap ».
- 3:52 à 3:56 : tracé blanc d'un circuit, puis zoom sur une ligne droite ; trajet violet « PIT STOP » et « Pit Delta = time spent in pit roads ».
- 4:15 : trajet bleu « RACING PATH » ajouté ; « – time spent on track », avec la précision « (between same points) ».
- 4:23 à 5:05 : trois circuits, avec un cercle noir aux points d'entrée et de sortie des stands, et le calcul complété ligne par ligne :

| Circuit (apparition) | Voie des stands | Même tronçon en piste | Pit delta affiché |
| --- | --- | --- | --- |
| Monza (4:23) | 38 s | 16 s | 22 s |
| Monaco (4:33) | 32 s | 12,5 s | 19,5 s |
| Silverstone (4:45) | 45,5 s | 23,5 s | 23 s |

**Narration**

- Delta est la lettre grecque utilisée en équation pour une différence ; le mot revient sans cesse en F1 pour les écarts de vitesse ou de temps.
- Mesure : de l'entrée des stands jusqu'au premier point de freinage après la sortie, là où la vitesse redevient celle d'un tour normal.
- Le delta varie selon le circuit : limitation de vitesse dans la voie, vitesse en piste, nombre de virages court-circuités.
- Monza : la voie longe toute la ligne droite principale, très rapide ; environ 16 s en piste contre 38 s avec arrêt, soit un delta d'environ 22 s, jugé important.
- Monaco : circuit lent, l'entrée et la sortie coupent un peu le premier et le dernier virage ; 12,5 s en piste contre 32 s, soit environ 19,5 s.
- Silverstone : l'entrée coupe une grande portion de fin de tour, mais la limitation de vitesse est basse ; 23 s au chronomètre de l'auteur.
- Réserve de l'auteur : temps pris au chronomètre sur des images, donc imprécis ; les stratèges mesurent l'écart sur un tour complet, pas sur ce seul tronçon.

## 5:08 à 6:11, l'ordre des pneus compte-t-il

Partir en soft aide au départ mais use le soft plus vite avec le plein de carburant ; garder le soft pour la fin lui permet de tenir 4 tours au lieu de 3 dans le modèle.

**À l'écran**

- 5:11 : « RACE STRAT » avec une barre « SOFT | MEDIUM » ; 5:13 : titre « DOES TYRE ORDER MATTER? ».
- 5:19 : seconde barre « RACE STRAT », « MEDIUM | SOFT ».
- Avant 6:00, sous « SOFT | MEDIUM » : triangle vert « Quick off the start line », triangle rouge « Softs degrade faster under more fuel ».
- 6:03 : le segment SOFT de la première barre se raccourcit (3 tours sur 10).
- 6:07 : sous « MEDIUM | SOFT », triangle vert « Softs last longer at end of race » ; 6:10 : triangle rouge « Mediums slower off the line ».

**Narration**

- Avantage du soft en premier : adhérent et performant tout de suite, il aide à gagner ou défendre des places au départ. Prendre la position en piste tôt compte, car dépasser n'est pas garanti.
- Inconvénient : la voiture est la plus lourde au départ à cause du carburant, pas encore modélisé. Le soft travaille davantage et s'use plus vite.
- Dans le modèle de 10 tours : soft en premier, 3 tours seulement ; soft à la fin, 4 tours. Il faut alors accepter de perdre des places au départ.

## 6:11 à 9:06, dégradation, modèle 3 sur 20 tours

Avec dégradation, le meilleur one-stop sur 20 tours est 9 tours soft + 11 medium (92 blocs + P) ; quatre two-stops atteignent 79 blocs + 2 arrêts, plus rapides si le pit delta est inférieur à 13 blocs.

Profils de temps au tour selon l'âge du pneu (lus à l'écran entre 6:48 et 7:20) :

| Tour du relais | Soft (blocs) | Medium (blocs) |
| --- | --- | --- |
| 1 | 3 | 4 |
| 2 | 3 | 4 |
| 3 | 3 | 4 |
| 4 | 4 | 4 |
| 5 | 4 | 4 |
| 6 | 5 | 5 |
| 7 | 5 | 5 |
| 8 | 6 | 5 |
| 9 | 6 | 6 |
| 10 | 7 | 6 |
| 11 | 7 | 6 |
| 12 | 8 | 7 |
| 13 | 8 | 7 |
| 14 | 9 | 7 |
| 15 | 9 | 8 |
| 16 | non affiché | 8 |
| 17 | non affiché | 8 |
| 18 | non affiché | 9 (déduit) |
| 19 | non affiché | 9 (déduit) |
| 20 | non affiché | 9 (déduit) |

Le medium, plus lent d'un bloc au départ, égale le soft au tour 4 puis devient plus rapide au tour 8.

**À l'écran**

- 6:18 : titre « TYRE DEGRADATION ». 6:25 : « Possible factors: », liste « Track temperature », « Abrasiveness of track surface », « Speed of corners », « Amount of fast corners per lap », « Car setup ».
- 6:31 : titre « MODEL 3: 20-LAP RACE W. TYRE DEG », axe des tours de 1 à 20.
- 6:37 : soft, tours 1 à 3 à 3 blocs. 6:48 : profil soft complet jusqu'au tour 15 ; flèche bleue au tour 10 avec « laptime = 7 on softs » en rouge et « laptime = 6 on softs » en jaune (voir les écarts).
- 6:50 : le profil soft devient un trait rouge en escalier. 6:52 à 7:04 : le medium se remplit, 4 blocs sur les tours 1 à 5 puis en hausse, jusqu'au tour 17. 7:13 : étiquette jaune corrigée en « laptime = 6 on mediums ».
- 7:20 : soft puis medium sur 20 tours, ligne bleue d'arrêt (pastille P) qui se déplace ; barre « TOTAL TIME » sous le graphique.
- 8:05 : « Optimal one-stop strategy ». 8:27 : « Optimal two-stop strategy? » avec quatre lignes, chacune avec le nombre de tours sous chaque relais, (S) pour soft et (M) pour medium.
- 8:48 : « 92 + P = 79 + PP », puis « 13 + = 0 + P », soit un arrêt de 13 ; texte « Two-stop strategy better if Pit Delta takes less than 13 time units ». 9:07 : rappel des barres du one-stop optimal et du premier two-stop.

| Stratégie (apparition) | Tours par relais | Temps par relais (blocs) | Total affiché |
| --- | --- | --- | --- |
| One-stop (7:27) | 3 S, 17 M | 9, 98 | 107 + P |
| One-stop (7:35) | 4 S, 16 M | 13, 90 | 103 + P |
| One-stop optimal (7:49) | 9 S, 11 M | 39, 53 | 92 + P |
| Two-stop optimal (8:27) | 5 S, 7 S, 8 M | 17, 27, 35 | 79 + PP |
| Two-stop optimal (8:27) | 6 S, 6 S, 8 M | 22, 22, 35 | 79 + PP |
| Two-stop optimal (8:27) | 6 S, 7 S, 7 M | 22, 27, 30 | 79 + PP |
| Two-stop optimal (8:27) | 7 S, 7 S, 6 M | 27, 27, 25 | 79 + PP |

**Narration**

- La dégradation dépend de nombreux facteurs, dont la température de piste, l'abrasivité du revêtement et le nombre de virages rapides.
- La course passe à 20 tours. Soft : 3 blocs pendant 3 tours, puis un bloc de plus tous les deux tours ; au tour 10, 7 blocs.
- Medium : stable pendant 5 tours, puis un bloc de plus tous les 3 tours. Plus lent au départ, il dure plus et se dégrade moins vite : au tour 10, 6 blocs contre 7 pour le soft.
- One-stop : l'ordre des relais n'importe pas ici, soft d'abord. La ligne marque l'arrêt ; en la déplaçant, on lit le temps du relais soft à gauche et celui du medium à droite. Avec 4 + 16 tours : 13 + 90 = 103.
- L'optimum est 9 tours soft + 11 medium, qui minimise le total (l'auteur dit 93, l'écran affiche 92). C'est la stratégie de référence, le « Plan A ».
- Two-stop : il existe 19 façons de faire un one-stop et 90 façons de faire un soft-soft-medium sur 20 tours. Avec ces profils, quatre atteignent le minimum de 79 blocs, mais avec deux arrêts. Grands nombres = durée du relais, petits = nombre de tours.
- Même algèbre qu'avant : le two-stop est plus rapide si le pit delta est inférieur à 13 blocs.
- En réalité, les modèles d'usure sont plus complexes, les facteurs se superposent, et l'on compare un nombre énorme de scénarios, pas 90.

## 9:06 à 9:58, masse de carburant et modèle 4

Le carburant, environ 70 kg au départ selon l'auteur, rend la voiture plus lente en début de course ; le modèle 4 le traduit en biseautant le haut de chaque pile de blocs.

**À l'écran**

- 9:14 : titre « THE FUEL WEIGHT FACTOR » ; graphique en aires « Total car mass /kg » (axe de 0 à 800) en fonction de « Race completed » (0 à 100 %), légende « Fuel » (bleu) et « Rest of Car » (bleu nuit). L'aire se déroule de 0 à 100 % entre 9:14 et 9:21.
- Lecture du graphique (estimé) : reste de la voiture vers 770 kg, total au départ vers 840 kg, couche carburant réduite à presque rien à 100 %.
- 9:23 : mot « Slower » sous le début de l'axe ; 9:32 : « Faster » sous la fin.
- 9:39 : retour aux blocs, 9 tours de soft dégradé puis 11 tours de medium, soit le one-stop optimal du modèle 3.
- 9:42 : titre « MODEL 4: 20-LAP ONE-STOP W. FUEL WEIGHT » ; une droite descend en diagonale au-dessus des piles.
- 9:44 : le haut de chaque pile est biseauté selon cette pente.
- 9:47 : légende humoristique en rouge, qui compare ces toits en pente à l'architecture des lotissements modernes.

**Narration**

- Sans ravitaillement, la voiture part avec environ 70 kg de carburant et finit presque à vide. Elle est plus lente au départ par le seul effet du poids, puis plus rapide et plus agile.
- Cela joue sur les temps au tour et sur la maniabilité ; les blocs ne peuvent pas modéliser la maniabilité, mais elle pèse sur le choix du pneu pour chaque phase de la course.
- Le gain de poids peut se représenter par une petite coupe en biais sur les blocs ; les vrais modèles sont bien plus riches en données.
- Les stratèges sous-remplissent souvent un peu le réservoir pour gagner du temps, et demandent au pilote d'économiser en milieu de course pour compenser.

## 9:58 à 11:42, stratégie face aux autres voitures

Coincé derrière une voiture plus lente, on perd un bloc par tour ; il faut des plans de repli et un arrêt qui fait ressortir en air libre, ce qui se calcule avec le pit delta.

**À l'écran**

- 10:08 : titre « STRATEGISING AROUND OTHER CARS ».
- 10:10 : graphique « Actual » (rouge) contre « Predicted » (orange clair). Tours 1 à 6 réels à 3 blocs, tours 7 à 18 prévus à 3 blocs. En dessous, bande de piste grise avec deux monoplaces vues de dessus : la bleue devant, la magenta derrière (les voitures roulent vers la gauche).
- 10:15 à 10:25 : tours 7 à 12 passent en réel, chacun avec un bloc bleu ajouté au-dessus des 3 blocs rouges.
- 10:35 : schéma circulaire d'un tour, « Finish Line » à gauche. Légende : « Our Car » (magenta), « Car behind » (bleu), « Car ahead » (blanc), « +0 Time gap to us ». Graduations de -20 à +70 autour du cercle, centrées sur notre voiture ; les points tournent avec la course.
- 10:47 : arc vert « Pit Delta » de 0 à +20 derrière notre voiture.
- 10:51 : flèche magenta au point de sortie des stands (+20), juste derrière un groupe serré de trois voitures.
- 10:53 à 11:01 : la flèche reste à +20 pendant que le cercle tourne.
- 11:07 : le groupe se trouve maintenant au-delà de +20 ; la sortie prévue passe devant lui.
- 11:14 : tour de chronométrage « LAP 38/67 » à gauche (tableau ci-dessous). 11:17 : flèche rouge sur LEC. 11:32 : barre verte de « +15.2 » à « +35.2 », flèche rouge à +35.2, entre VER (+32.6) et LAW (+50.1).

| Pos. | Pilote | Écart au leader | Pneu affiché |
| --- | --- | --- | --- |
| 1 | ANT | Leader | S |
| 2 | PIA | +13.7 | S |
| 3 | LEC | +15.2 | S |
| 4 | RUS | +15.7 | M |
| 5 | NOR | +23.4 | M |
| 6 | HAM | +25.0 | S |
| 7 | GAS | +32.3 | H |
| 8 | VER | +32.6 | M |
| 9 | LAW | +50.1 | S |
| 10 | OCO | +51.2 | M |
| 11 | HUL | +52.2 | H |
| 12 | HAD | +56.1 | H |
| 13 | BOR | +59.0 | S |
| 14 | LIN | +59.8 | M |
| 15 | SAI | +65.0 | H |
| 16 | COL | +65.7 | S |
| 17 | PER | +92.4 | S |
| 18 | ALO | +1 lap | H |
| 19 | BOT | +1 lap | M |
| 20 | ALB | +2 laps | M |
| 21 | STR | DNF | M |
| 22 | BEA | DNF | H |

**Narration**

- Le modèle ignore les autres voitures : impossible de tourner en 3 blocs derrière une voiture à 4. Chaque tour coincé ajoute un bloc et la stratégie ne tient plus.
- D'où les plans B, C et D : prévoir des bascules hors de la stratégie idéale.
- Sans dépassement possible, on cherche l'air libre : s'arrêter et exploiter les pneus neufs sans être gêné.
- Les stratèges suivent la position de chacun en temps. Le cercle représente un tour, par exemple 100 s ; avec un pit delta de 20 s, l'arrêt fait ressortir à +20.
- À ce moment, ce point tombe juste derrière trois voitures en lutte : on ne pourrait pas attaquer, mieux vaut attendre.
- Quelques tours plus tard, quelques secondes ont été prises sur ce groupe et la sortie prévue passe devant : c'est le moment de rentrer.
- Pour le téléspectateur : connaître le pit delta du circuit permet de lire la tour de chronométrage. Leclerc à 15 s, plus 20 s de delta, ressortirait à 35 s, quelques secondes derrière Verstappen, à 32 s du leader.
- L'auteur préfère l'affichage des écarts au leader à l'affichage par intervalle, plus commode pour ce calcul mental.

## 11:42 à 12:42, attendre une safety car

Sous VSC ou safety car, le tronçon en piste se parcourt plus lentement, donc l'arrêt coûte moins cher : à Monaco, 14 s sous VSC et 12 s sous safety car, au lieu de 19,5 s.

**À l'écran**

- 11:41 : cercle de tour, notre voiture sur la ligne d'arrivée, arc vert « Pit Delta ». 11:44 : titre « HOLDING OUT FOR A SAFETY CAR ».
- 11:53 : trois arcs superposés, « Pit Delta » (vert), « VSC Pit Delta » (bleu nuit) et « SC Pit Delta » (turquoise), les deux derniers plus courts.
- 11:55 à 12:20 : tracé de Monaco, trajet des stands (violet) et trajet en piste (bleu), avec des marqueurs de progression. Trois colonnes s'affichent tour à tour :

| Régime (apparition) | Voie des stands | Même tronçon en piste | Coût de l'arrêt |
| --- | --- | --- | --- |
| Green Flag (11:55) | 32 s | 12,5 s | 19,5 s |
| Virtual Safety Car (12:11) | 32 s | 18 s | 14 s |
| Safety Car (12:19) | 32 s | 20 s | 12 s |

- 12:28 : phrase en haut de l'écran : avec un risque élevé de safety car, il peut valoir la peine de prolonger le relais idéal. Coquille à l'écran, « change » au lieu de « chance ». En bas, rappel « MONACO Pit Deltas » : 19,5 s, 14 s et 12 s.
- 12:32 : triangle vert « Maybe benefit from cheap pit stop ». 12:43 : triangle rouge « Maybe lose time from increasingly worn tyres ».

**Narration**

- On peut devoir adapter la stratégie en direct : voiture de devant impossible à passer, pneus qui ne se comportent pas comme prévu, ou attente d'une safety car.
- S'arrêter sous safety car fait gagner beaucoup de temps et peut faire gagner plusieurs places.
- La raison tient au calcul du pit delta. À Monaco, 12,5 s en piste contre 32 s dans les stands ; sous VSC, le tronçon en piste prend environ 18 s et l'arrêt ne coûte que 14 s au lieu de 19,5 ; sous safety car, seulement 11 à 12 s.
- Certains circuits ou situations, comme la pluie, présentent un risque plus élevé de safety car. Si ce risque est fort, on peut prolonger le relais en espérant en profiter.
- Le temps qu'on accepte de perdre sur des pneus qui se dégradent est un arbitrage risque/bénéfice, calculé en partie en direct avec la télémétrie des pneus et le ressenti du pilote.

## 12:42 à 13:59, la météo

La pluie rend la stratégie peu prévisible ; le graphique simplifié montre le soft le plus rapide sur le sec, l'intermédiaire sur piste humide et le pneu pluie seulement sur piste très mouillée.

**À l'écran**

- 12:51 : titre « ACCOUNTING FOR WEATHER », deux colonnes. « DRY WEATHER » (soleil) : « Slick Tyres », « More Grip », « Hotter track », « Faster pace ». « WET WEATHER » (nuage de pluie) : « Inter/Wet Tyres », « Less Grip », « Cooler track », « Slower pace », puis « Less predictable » à 12:52.
- 12:56 à 13:20 : la colonne du sec disparaît ; à côté de « Less predictable », une liste s'allonge : « Intensity of rain », « Length of rainfall time », « Depth of standing water », « Variation across circuit », « Rate of evaporation », « Driver skill/feedback ».
- 13:24 : graphique « Laptime » (« SLOWER » en haut, « FASTER » en bas) en fonction de « Wetness of track » ; courbe « Soft » (rouge, trait plein) qui monte très vite.
- 13:40 : courbes « Inter » (vert, tirets) et « Wet » (bleu nuit, pointillés) ; petite zone orange à gauche, là où le soft est le plus rapide.
- 13:50 : mention « Inters overheat » sur la partie sèche de la courbe Inter ; zone verte « Inters Fastest ».
- 13:51 à 13:59 : une zone grise s'étend vers la droite, puis reçoit la légende « Wets Fastest ».

**Narration**

- La pluie ralentit la piste et impose des pneus pluie, mais elle n'est pas régulière : forte ou faible, elle touche différentes parties du circuit en se déplaçant. Les flaques se forment et sèchent selon le relief de la piste et la température.
- Le calculateur de stratégie ne peut donc pas s'appuyer sur un seul modèle de piste mouillée.
- Il faut aussi compter avec le pilote : s'il sait gérer des slicks sur piste humide, on peut éviter un arrêt lors d'une averse passagère.
- Le graphique est volontairement simplifié, sans données réelles. Le soft est excellent jusqu'à une piste légèrement humide, puis devient très lent très vite.
- Plus la courbe est basse, plus le tour est rapide : l'intermédiaire prend vite le relais quand l'eau stagnante augmente. Sur piste trop sèche, il surchauffe à cause du mouvement de la bande de roulement.
- Sur piste très mouillée, le pneu pluie est le plus rapide car il évacue le plus d'eau. L'auteur ironise : la course sera arrêtée avant qu'on s'en serve, et il s'étonne qu'on les apporte encore.

## 13:59 à 15:00, décalage de stratégie, undercut et overcut

Deux pilotes sur la même stratégie soft puis medium : celui qui s'arrête plus tôt tente l'undercut ; celui qui prolonge pour finir sur des pneus bien plus frais tente l'overcut, plus difficile.

**À l'écran**

- 14:02 : titre « STRATEGY OFFSET » ; bande de piste avec la voiture bleue devant la rose (les voitures roulent vers la gauche).
- 14:04 à 14:06 : deux barres identiques, « 24 Laps » (rouge, soft) puis « 46 Laps » (jaune, medium), pour la voiture rose et la bleue, soit 70 tours ; ligne pointillée « Planned Strategy » au tour 24.
- 14:10 : la voiture rose passe à « 21 Laps » + « 49 Laps », avec la note manuscrite « Pink car faster on fresh tyres » ; sur la piste, une bande rose relie les deux voitures.
- 14:14 à 14:26 : cercle de tour avec « Pink car », « Blue car » et « +0 Time gap to pink » ; arc vert du pit delta derrière la voiture rose. Sur la piste, l'écart affiché diminue : « +22.1 s » (14:18), « +20.9 s » (14:20), « +18.0 s » (14:22), « +17.4 s » (14:24 à 14:26).
- 14:28 : la voiture bleue s'arrête et ressort derrière la rose ; de 14:30 à 14:36, la rose est devant sur la piste.
- 14:42 : barre bleue « 26 Laps » + « 44 Laps » ; 14:45 : « 33 Laps » + « 37 Laps », avec la note « Blue car much faster on fresh tyres » ; 14:50 : note « Blue car loses more time on old tyres ».
- 14:45 à 15:01 : sur la piste, la voiture bleue reste derrière la rose, à une distance qui varie.

**Narration**

- Deux pilotes sur des stratégies proches, soft puis medium ; l'un s'arrête deux tours plus tôt pour signer des temps rapides en pneus neufs, même idée que la recherche d'air libre vue plus haut.
- Le but : avant l'arrêt du rival, reprendre assez de temps pour entrer dans sa fenêtre de pit delta, afin qu'il ressorte derrière. C'est l'undercut.
- Le pilote qui s'arrête plus tard peut se retrouver derrière, mais sur des pneus plus frais et plus rapides ; en théorie, il reprend la place s'il parvient à dépasser.
- Pour accentuer l'écart de rythme, ce pilote, voyant l'undercut venir, peut prolonger encore son relais afin d'avoir des pneus beaucoup plus rapides que son rival.
- La contrepartie : il perd davantage de temps en attendant, puis doit rattraper et dépasser. C'est l'overcut, plus délicat, surtout sur un circuit où l'on dépasse mal.

## 15:00 à 15:32, conclusion et générique

L'auteur clôt sur un résumé d'une phrase et un au revoir ; le reste est le générique.

**À l'écran**

- 15:03 à 15:08 : transition, formes gris foncé qui envahissent l'écran puis un petit carré jaune.
- 15:11 : « Produced by STUART TAYLOR » sur un logo stylisé (ours à engrenages).
- 15:15 à 15:31 : « LOVELY PATREON FOLK », liste défilante des contributeurs Patreon, sur deux colonnes (noms non relevés).

**Narration**

- Fin du tour d'horizon des bases de la stratégie. L'auteur espère avoir donné une image mentale utile pour suivre les courses, ou au moins le plaisir de voir des carrés colorés bouger. Au revoir.

## Écarts entre écran, narration et sous-titres

Un seul écart touche un résultat chiffré : le one-stop optimal du modèle 3 vaut 92 blocs à l'écran, 93 à l'oral ; le calcul 39 + 53 donne 92.

| Moment | Écart constaté | Ce qui fait foi |
| --- | --- | --- |
| 7:46 à 7:52 | Narration : 93 unités pour 9 soft + 11 medium. Écran : relais de 39 et 53 blocs, total « 92 + P ». | Écran (39 + 53 = 92) |
| 6:48 | Étiquette jaune « laptime = 6 on softs » au tour 10, alors que la valeur 6 est celle du medium. | Écran corrigé à 7:13 : « laptime = 6 on mediums » |
| 12:28 | Phrase à l'écran avec « change » au lieu de « chance ». | Coquille, sens évident |
| 12:17 à 12:19 | Narration : 11 ou 12 s sous safety car à Monaco. Écran : 32 − 20 = 12 s. | Écran pour la valeur, narration pour la fourchette |
| 4:45 à 5:05 | Silverstone : l'écran détaille 45,5 s et 23,5 s, la narration ne donne que le delta de 23 s. | Les deux sont cohérents |
| 6:25 | Cinq facteurs de dégradation à l'écran, trois cités à l'oral (température, abrasivité, virages rapides). « Speed of corners » et « Car setup » ne sont qu'à l'écran. | Écran |
| 7:20 | Profil medium des tours 18 à 20 : un cran au-dessus de 8 à l'écran, sans valeur écrite. | 9 blocs (déduit de la règle un bloc tous les 3 tours) |

Coquilles de la piste en-GB, sans effet sur le sens : « effect » pour « affect » (2:03), « blocks or time » (2:08), « totally » pour « totalling » (2:09), « take out pitstop » pour « take our pitstop » (7:22), « blocks on time » (7:41), « weight-gaining » (9:53) alors que le gain de temps vient de l'allègement.
