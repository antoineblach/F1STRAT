# compound_allocations.csv : sources, méthode, limites

Version du 21/10/2026. 70 GP : 22 en 2023, 24 en 2024, 24 en 2025. Séparateur « ; », encodage UTF-8.

## Colonnes

| Colonne | Contenu |
| --- | --- |
| saison, manche, gp | Calendrier et noms d'épreuve de l'API Jolpica (`api.jolpi.ca/ergast/f1/<saison>.json`), identiques aux noms d'épreuve de FastF1 |
| format | standard, sprint (présence d'un sprint dans Jolpica, concordante avec les articles qui le mentionnent) ou ATA |
| dur, medium, tendre | Désignation C du composé |
| gamme_saison | Gamme Pirelli de la saison : C0 à C5 en 2023, C1 à C5 en 2024 (C0 retiré), C1 à C6 en 2025 (C6 nouveau) |
| spec_obligatoire_1, spec_obligatoire_2 | NA partout (voir limites) |
| limite_tours_par_train | Limite imposée hors règlement, sinon NA |
| essais_pneus | Pneus d'essai fournis pendant le week-end, d'après les articles ; NA si aucun mentionné |
| correspondance_dms | « explicite » si une source attribue chaque composé au dur, au médium et au tendre ; « ordre » si elle ne donne que les trois composés (le plus dur est alors pris comme dur) |
| note | Particularités |
| url_source | Une ou plusieurs sources, séparées par « \| » |
| citation | Phrase de la première source qui nomme les composés |

## Méthode et fiabilité

- Source principale : la série F1.com « What tyres will the teams and drivers have for the <année> <GP>? », publiée avant chaque GP, qui reprend l'annonce de Pirelli. Sources complémentaires : communiqués Pirelli (press.pirelli.com), F1Technical, Tyrepress, Speedcafe, déclaration FIA (Qatar 2023), Williams (Qatar 2025).
- 30 GP ont deux sources concordantes ; 40 n'en ont qu'une (F1.com dans la plupart des cas, sinon Pirelli ou F1Technical).
- Contrôle croisé de 10 GP sur une seconde source indépendante de la première : tous concordants. Aucune contradiction trouvée.
- Un conflit apparent sur São Paulo 2024 (Speedcafe) a été levé : F1.com, F1Technical et Pirelli concordent sur C3, C4, C5 ; Pirelli indique que 2025 (C2, C3, C4) est « un cran plus dur » que 2024.
- Correspondance déduite de l'ordre pour 11 GP (colonne correspondance_dms) : 2023 Bahreïn, Arabie saoudite, Australie, Monaco, Espagne, Pays-Bas ; 2024 Bahreïn, Japon, Chine, Belgique, Pays-Bas.
- Les articles ont été lus avec un outil de lecture qui résume la page : les composés sont tirés des citations rapportées, pas d'une lecture intégrale de chaque page.

## Points d'attention pour la calibration

1. **Une étiquette C ne désigne pas le même pneu d'une saison à l'autre.** Le C1 de 2022 est devenu le C0 en 2023, avec un nouveau C1. Le C0 a été retiré en 2024. Pendant la saison 2023, Pirelli a fait essayer une nouvelle version du C2 au Japon, « en vue de son homologation pour la saison suivante », et une variante du C4 au Mexique. Un prototype 2025 a été essayé au Mexique en 2024, et le C6 est apparu en 2025. Conséquence : la dégradation doit être estimée par couple (saison, composé), jamais regroupée sur l'étiquette C seule entre saisons. Cela amende le « d_C par composé absolu » de prompt_calibration.
2. **Spécifications obligatoires en course : inconnues.** Le règlement (30.2c ii) prévoit une ou deux spécifications désignées par la FIA à chaque GP ; aucune source consultée ne les publie. Ce n'est pas neutre : si seule la spécification dure est obligatoire, une course sèche en médium puis tendre est interdite. Piste (hypothèse) : les déduire des relais réels de FastF1. Une course sèche terminée en médium puis tendre par un pilote classé exclut que le dur soit la seule spécification obligatoire.
3. **Limites de tours par train.**
   - Qatar 2023 : 18 tours de vie totale par train, imposés par la FIA le 08/10/2023 ; les tours déjà faits comptent, mais les critères de comptage ne sont pas publiés sur la page FIA.
   - Qatar 2025 : 25 tours par train sur toutes les séances, tours sous SC et VSC compris, hors tours vers la grille, tour de formation et tours après le drapeau à damier (F1.com, Williams).
   - Qatar 2024 : aucune limite mentionnée.
4. **Sélections non consécutives en 2025** : Belgique (C1, C3, C4), États-Unis (C1, C3, C4), Mexique (C2, C4, C5).
5. **ATA (allocation alternative de pneus)** : Hongrie et Italie 2023. Imola 2023, prévu en ATA, a été annulé.
6. **Essais de pneus** : relevé non exhaustif (Espagne, Japon et Mexique 2023 ; Mexique 2024). Aucun GP n'a été identifié avec l'allocation réduite à 12 trains pour les gommes d'évaluation en EL2 (règlement sportif 30.1a iii).
7. **Monaco 2025** : au moins 3 trains en course (règlement sportif 30.5m).
