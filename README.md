# Analyseur de notes

Programme en ligne de commande qui lit un fichier CSV de notes, calcule les moyennes par élève ou par matière, et affiche la meilleure et la pire note.

## Fonctionnalités
- Lit un fichier CSV au format `nom,matiere,note`.
- Calcule les moyennes par élève ou par matière (`--par`).
- Affiche la meilleure et la pire note.
- Ignore les lignes dont la note n'est pas un entier, et signale combien.
- Affiche un message clair si le fichier est introuvable.

## Installation
Testé avec Python 3.14. Aucune bibliothèque externe pour l'utiliser.
Pour les tests : `py -m pip install pytest`

## Utilisation
```
py analyse.py
py analyse.py --fichier invalid.csv
py analyse.py --par matiere
py analyse.py --help
```

## Tests
Depuis la racine du projet : `py -m pytest`

## Structure
- `analyse.py` : lecture du fichier et calculs
- `test_analyse.py` : tests automatiques
- `notes.csv` : fichier d'exemple
- `invalid.csv` : données de test contenant une ligne invalide

## Limites connues
- Les notes décimales (`14.5`) sont considérées invalides.
- Un nom contenant une virgule casse la lecture.
- Deux orthographes d'un même nom comptent comme deux élèves.

## Améliorations futures
- Accepter les notes décimales avec le module `csv`.
- Exporter les résultats.