# Sources de données pour la stratégie de course F1 (contexte agent)

Contexte : jeu de stratégie de course en navigateur (TypeScript), solo contre IA, course seule, modèle temps au tour. Les données réelles servent à calibrer les paramètres du modèle.

Fiabilité : sauf mention « À VÉRIFIER », chaque point ci-dessous a été vérifié sur la page source le 19/10/2026. Ne jamais inventer une valeur absente des sources : la signaler comme manquante.

Référence conceptuelle (modèle à blocs, pit delta, undercut, overcut) : `chainbear_strategie_f1_releve.md`.

## 1. Sources

| Facteur | Source | Contenu utile | Accès et limites |
| --- | --- | --- | --- |
| Dégradation, relais, arrêts | FastF1 (Python), https://docs.fastf1.dev/core.html | Pour chaque tour : `Compound`, `TyreLife`, `FreshTyre`, `Stint`, `PitInTime`, `PitOutTime`, `TrackStatus` (codes de statut de piste survenus pendant le tour) | Gratuit. Années couvertes non précisées par la doc consultée |
| SC, VSC, drapeaux | FastF1 | `session.race_control_messages` (chargement `messages=True`) ; `session.track_status` (chargement `laps=True`) | Idem |
| Météo en séance | FastF1 | `session.weather_data`, environ une mesure par minute : AirTemp, Humidity, Pressure, Rainfall, TrackTemp, WindDirection, WindSpeed (chargement `weather=True`) | Idem |
| Alternative sans Python | OpenF1, https://openf1.org, base `https://api.openf1.org/v1` | 18 points d'accès : temps au tour, arrêts, relais, direction de course, météo, positions, télémétrie, radio, classements | Historique gratuit sans clé depuis la saison 2023. JSON par défaut, CSV avec `csv=true`. Limite gratuite : 3 requêtes/s et 30/min. Temps réel payant (9,90 €/mois) |
| Données prêtes en JSON | TracingInsights 2026, https://github.com/TracingInsights/2026 | Par GP et par session : tours, pneus (composé, âge, relais), arrêts, télémétrie (environ 3,7 Hz), météo à la minute (`weather.json`), messages de direction de course (`rcm.json`), virages (`corners.json`), pilotes. Généré avec FastF1 | Licence Apache-2.0 (attribution requise). Saison 2026 uniquement |
| Historique long | Jolpica-F1, successeur d'Ergast (fermé début 2025), https://docs.fastf1.dev/api_reference/jolpica.html | Résultats, calendriers, circuits, saisons, classements depuis 1950. Accessible aussi via le module `ergast` de FastF1 | Gratuit, avec limite de débit (valeur non publiée sur la page consultée) |
| Caractéristiques circuits et pneus | Pirelli, https://racingspot.pirelli.com/global/en-ww/race/formula-1-for-dummies-the-choice-of-tyres-in-formula-1 | 3 composés nommés par GP sur l'échelle C (dur : C1 à C3 ; medium : C2 à C4 ; tendre : C3 à C5). Avant chaque GP : abrasivité et adhérence de l'asphalte, traction, freinage, efforts latéraux, contrainte pneu, appui, évolution de la piste. Après les EL2 : écarts entre composés en dixièmes. Avant la course : stratégies jugées les plus efficaces | Communiqués Pirelli, à collecter GP par GP |
| Climat par circuit | Open-Meteo, https://open-meteo.com/ | Archive horaire ERA5 depuis janvier 1940 (température, humidité, vent ; présence de la variable pluie À VÉRIFIER dans la doc de l'API historique) | Sans clé. Gratuit en usage non commercial jusqu'à 10 000 appels/jour. Licence CC BY 4.0 (attribution requise) |
| Règles | FIA, règlement F1 2026, https://www.fia.com/regulation/category/2182 | Section B sportive (version 09 du 1er octobre 2026) et section F opérationnelle (version 11 du 1er octobre 2026) : règles pneus, procédures SC/VSC, voie des stands | Documents publics |
| IA adverse | Heilmeier, Thomaser, Graf, Betz, « Virtual Strategy Engineer », Applied Sciences 10(21) 7805, 2020, DOI 10.3390/app10217805 | Deux réseaux de neurones : faut-il s'arrêter, et quel composé monter. Entraînés sur les données 2014 à 2019, intégrés à une simulation de course | Article. Code source public : À VÉRIFIER |
| Prise de décision SC (qualitatif) | McLaren, 2019, https://www.mclaren.com/racing/formula-1/2019/canadian-grand-prix/how-make-right-call-safety-car/ | Méthode des équipes, voir section 3 | Article |

## 2. Pièges établis

- `Compound` ne distingue pas C1 à C5 : un SOFT d'un GP n'est pas le même pneu qu'un SOFT d'un autre GP. Toujours croiser avec la nomination Pirelli du GP concerné.
- `TyreLife` inclut les tours faits avec ce train lors des séances précédentes.
- SC et VSC n'ont pas la même dynamique. La SC regroupe le peloton et dure en général au moins 4 tours environ. La VSC ne regroupe pas le peloton, peut ne durer qu'une minute environ, et peut se transformer en SC.
- Les tours sous SC, VSC ou drapeau rouge faussent toute mesure de rythme : les exclure via `TrackStatus` avant de calibrer quoi que ce soit.
- OpenF1 : 30 requêtes/min en gratuit. Ne jamais l'appeler pendant une partie.

## 3. Grandeurs à dériver (aucune source ne les publie toutes prêtes)

1. **Pit delta par circuit**
   - Définition : temps passé dans la voie des stands moins le temps du même tronçon en piste.
   - Calcul : à partir de `PitInTime`, `PitOutTime` et des temps au tour, en comparant le tour d'entrée et le tour de sortie à des tours normaux du même pilote, hors SC/VSC.
   - Stocker aussi la valeur sous VSC et sous SC quand des arrêts ont eu lieu dans ces régimes.
2. **Dégradation par composé et par circuit**
   - Calcul : régression du temps au tour sur `TyreLife`, par composé C, sur tours valides uniquement.
   - Correction carburant : la voiture perd environ 70 kg de carburant sur la course (ordre de grandeur cité par Chain Bear), donc corriger cet effet. Le coefficient de correction n'est pas établi par les sources ci-dessus : le signaler comme hypothèse.
3. **Probabilité de SC et de VSC par circuit**
   - Calcul : compter, dans les messages de direction de course, les courses avec au moins un déploiement, et la durée de chaque phase.
   - Méthode des équipes (McLaren) : partir de l'historique du GP ; considérer débris et accrochages comme de bons prédicteurs ; écarter les événements exceptionnels ; ne pas compter la pluie passée si le sec est annoncé ; ajuster selon les changements de règlement. Exemple publié : environ 60 % des courses au Canada avec au moins une SC (donnée 2019).
4. **Probabilité de pluie à la date du GP** : à partir de l'archive Open-Meteo aux coordonnées du circuit.
5. **Écart de rythme entre composés** : à partir des écarts publiés par Pirelli après les EL2, ou des longs relais des EL2 dans FastF1.

## 4. Architecture recommandée

- Extraction hors ligne en Python avec FastF1 (et Jolpica-F1 pour l'historique long), production de fichiers JSON de paramètres par circuit.
- Le jeu TypeScript charge ces JSON. Aucun appel d'API pendant une partie.
- Chaque paramètre du JSON porte sa source et son mode d'obtention (mesuré, dérivé ou hypothèse), pour pouvoir recalibrer.
- Mentionner dans le jeu les attributions requises : TracingInsights (Apache-2.0) et Open-Meteo (CC BY 4.0).

## 5. Points non vérifiés

- Codes de statut de piste FastF1 : 1 vert, 2 jaune, 4 SC, 5 drapeau rouge, 6 VSC, 7 fin de VSC. Donnés de mémoire, à confirmer dans la doc FastF1 avant usage.
- Premières saisons couvertes par FastF1 pour les tours et la télémétrie.
- Disponibilité dans Jolpica-F1 des temps au tour et des arrêts, et dès quelle saison.
- Variable pluie dans l'API historique Open-Meteo.
- Publication du code du Virtual Strategy Engineer.
