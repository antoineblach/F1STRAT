# Track DNA 2024 et 2025 : sources, méthode, limites

Version du 21/10/2026. Fichiers : `track_dna_2024_2025.csv` (notes par GP) et `circuits_virages_complement.csv` (composition des virages des 9 circuits absents de 2026).

## Source

Six captures d'écran de formula1dashboard.com, fournies le 21/10/2026 :
- 3 tableaux « Track Characteristics » (notes de 1 à 5 par GP) ;
- 3 cartes « Track Similarity Map » (part de virages rapides et lents, taille de bulle selon le nombre de virages, couleur selon la contrainte pneus).

Les captures ne portent pas l'année. Elle a été identifiée par l'ordre des drapeaux, comparé aux calendriers Jolpica :
- 2024 : Bahreïn, Arabie saoudite, Australie, Japon, Chine... ;
- 2025 : Australie, Chine, Japon, Bahreïn, Arabie saoudite... ;
- 2026 : avec Madrid (Madring) et le GP de Bahreïn à Sepang (Kuala Lumpur).

Le tableau 2026 correspond à `track_dna_2026.csv` (contrôle sur Melbourne et Montréal). Seuls 2024 et 2025 ont donc été transcrits. **Pas de capture 2023.**

Catégories : traction, adhérence de l'asphalte, abrasion, évolution de la piste, contrainte pneus, freinage, charge latérale, appui (absente en 2026). Ce sont les catégories des infographies de présentation de Pirelli. Que le site les reprenne de Pirelli est une hypothèse, non vérifiée.

## Transcription

- Lecture sur les captures agrandies, colonne par colonne ; 8 notes × 24 GP par saison.
- Colonne `site_column` : colonne du site d'où viennent les valeurs. Colonne `correction` : renseignée quand elle diffère du GP.

## Correction appliquée en 2025 (permutation suspectée)

Sur le site, les valeurs 2025 de deux paires de GP semblent permutées : Espagne et Canada, Belgique et Hongrie. Le CSV contient les valeurs corrigées ; la colonne `site_column` garde la trace de l'affichage d'origine.

Éléments en faveur de la permutation :
1. Une fois permutées, les valeurs 2025 sont identiques ou presque à celles de 2026 pour le même circuit :
   - Spa 2025 corrigé = Spa 2026 (4, 3, 3, 3, 5, 4, 5) ;
   - Hungaroring 2025 corrigé = Hungaroring 2026 (4, 3, 3, 4, 3, 3, 3) ;
   - Catalunya 2025 corrigé (3, 3, 4, 3, 5, 3, 5) et 2026 (3, 2, 4, 3, 5, 3, 5) ;
   - Montréal 2025 corrigé (3, 2, 1, 5, 3, 5, 1) et 2026 (4, 2, 1, 5, 3, 5, 1).

   Non permutées, elles s'en écartent sur presque toutes les notes.
2. Telles qu'affichées, elles contredisent les choix de Pirelli en 2025 :
   - Montréal, avec les trois composés les plus tendres (C4, C5, C6), aurait la contrainte pneus 5 ;
   - Barcelone, avec les trois plus durs (C1, C2, C3), aurait 3 ;
   - même inversion entre Spa (C1, C3, C4) et le Hungaroring (C3, C4, C5).
3. Cause probable (hypothèse) : en 2024, le Canada précédait l'Espagne et la Hongrie précédait la Belgique ; en 2025, c'est l'inverse. Les données 2025 de ces deux paires semblent rangées dans l'ordre du calendrier 2024.

La carte de similarité 2025 du site concorde avec l'affichage non corrigé : elle repose sur les mêmes données internes et ne constitue pas un contrôle indépendant.

## Limites

- 2024 est moins discriminant : 51 % des notes valent 3, contre 40 % en 2025 et 37 % en 2026. Plusieurs circuits typés y sont à 3, alors qu'ils sont marqués les deux autres années : l'appui à Monza, Singapour et Mexico, la charge latérale à Bakou. Hypothèse : valeurs par défaut pour une partie de 2024. À prendre en compte dans le poids donné à 2024 dans les régressions.
- Aucune donnée 2023 dans les captures fournies.
- Échelle ordinale (1 à 5) : à traiter comme catégories ou rangs, pas comme mesure continue.

## Composition des virages (`circuits_virages_complement.csv`)

- Les bulles occupent exactement les mêmes positions sur les trois cartes (2024, 2025, 2026) : la composition des virages est un attribut fixe du tracé actuel, pas une donnée annuelle.
- Pour les circuits présents dans `track_dna_2026.csv`, les positions retrouvent exactement les comptes de ce fichier (par exemple Melbourne : 8 rapides et 3 lents sur 14, soit 57 % et 21 %).
- Pour les 9 circuits absents de 2026 :
  - méthode : centres et rayons des bulles détectés par transformée de Hough sur la carte 2025 ;
  - nombre de virages = rayon / 1,9, arrondi ; ce rapport, ajusté sur les 17 circuits de `track_dna_2026.csv`, retrouve leur nombre de virages dans tous les cas (écart avant arrondi de 0,7 virage au plus) ;
  - comptes = arrondi (pourcentage × nombre de virages).

  Les 9 solutions retrouvent exactement les pourcentages entiers affichés. Valeurs marquées « dérivé ».
- La couleur des bulles (contrainte pneus) reprend la note du tableau : information redondante.
