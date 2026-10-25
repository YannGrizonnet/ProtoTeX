# Matrice d'attributs — preuve de concept

Ce prototype réutilise le moteur `prototex.sty` existant, sans le remplacer.

- `cards.csv` contient quatre cartes fictives.
- `styles.csv` contient une règle par ligne, éditable dans Calc.
- `tools/build_matrix.py` transforme les CSV en LaTeX.
- `generated.tex` est la sortie de démonstration.

Depuis la racine du dépôt :

```sh
python3 tools/build_matrix.py
TEXINPUTS=.: lualatex -halt-on-error examples/matrix/generated.tex
```

Opérations : `set` pour les propriétés exclusives, `append` pour les badges, `show` / `hide` pour la visibilité. `priority` résout les conflits ; des affectations contradictoires de même priorité sont rejetées.

Il s'agit d'un **pont Python vers LaTeX expérimental**, pas d'un import CSV natif au moteur. Le mapping des composants reste limité, les portraits et paysages sont pris en charge, les masques et les feuilles d'impression restent à développer. Les images de test proviennent de TeX Live, aucune image commerciale n'est incluse.
