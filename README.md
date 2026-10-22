# F1STRAT

Jeu de stratégie de course (muret des stands). Projet personnel, dépôt privé.

## Contenu du dépôt
- `Data_Biblio/` : index, notes, lisezmoi, CSV dérivés, script d'extraction (`4_donnees/_extraction_api/extraction_api.py`).
- `archive/` : versions successives des prompts Claude Code (jeu et calibration).

## Hors dépôt (Google Drive, `Mon Drive/F1STRAT`)
Copie complète de l'arborescence, y compris ce que git ignore (voir `.gitignore`) :
- PDF des règlements FIA et des articles (`1_reglements/`, `2_articles/`) ;
- vidéo et audio Chain Bear (`3_video_chainbear/`) ;
- base SQLite TUM 2014-2019 ;
- JSON bruts Open-Meteo et OpenF1 (régénérables par `extraction_api.py`).

## Mise en place sur un nouveau PC
1. `git clone https://github.com/antoineblach/F1STRAT.git` dans un dossier local **hors** du dossier synchronisé par Google Drive.
2. Copier depuis `Mon Drive/F1STRAT` les fichiers ignorés par git, aux mêmes chemins relatifs.
3. Avant de travailler : `git pull`. Après : `git add`, `git commit`, `git push`.

Le dépôt git ne doit jamais se trouver dans un dossier synchronisé par Google Drive (verrous et conflits dans `.git`).
