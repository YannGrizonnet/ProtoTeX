# Étude de mise en page inspirée de Disney Lorcana

Exemple **expérimental** de trois modèles de cartes : personnage, action et objet.

Le but est de tester la disposition des champs, non de reproduire les éléments officiels de Disney Lorcana. Les cartes d'exemple utilisent des noms et des effets de démonstration, et des illustrations de remplacement fournies séparément par l'auteur du projet.

## Construction

Depuis le dossier `examples/lorcana-study` :

```sh
lualatex -interaction=nonstopmode -halt-on-error study.tex
```

Le fichier `cards-study.csv` est lu avec `csvsimple` (séparateur `;`). Les images attendues sont `images/img1.jpg`, `images/img2.jpg`, `images/img3.jpg`; elles ne sont **pas publiées dans le dépôt**. Quand elles manquent, le rendu conserve une zone de couleur en remplacement.

Le modèle (`lorcana-style.tex`) reste autonome par rapport au package : il s'agit d'un banc d'essai pour identifier les futures primitives de ProtoTeX, et non d'une nouvelle API stable.

## Ce que l'étude met en évidence

- Zones d'image avec remplissage sans déformation et rognage.
- Bandeau de titre et sous-titre, catégorie, texte d'effet et pied de carte.
- Coût en médaillon, statistiques conditionnelles, valeur de lore conditionnelle.
- Réutilisation d'un même modèle à partir d'un CSV.

Les icônes sont ici remplacées par des pastilles et des valeurs textuelles ; les véritables pictogrammes génériques restent à développer.

**Attention :** ne pas nommer une macro issue d'un CSV `\color`, sous peine d'écraser la commande LaTeX de coloration. La colonne est ici nommée `ink`.
