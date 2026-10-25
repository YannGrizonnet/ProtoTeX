# Principes de conception de ProtoTeX

## Objectif

Créer et imprimer des prototypes de cartes de jeux de société avec **LaTeX, TikZ et CSV**, prioritairement pour un usage personnel sous Linux.

## Trois responsabilités distinctes

- **Contenu** : titre, illustration, coûts, texte de règles, type, rareté, identifiant et données propres au jeu.
- **Disposition** : dimensions de la carte, zones, lignes virtuelles, alignements et marges.
- **Thème** : couleurs, bandeaux, typographie, pictogrammes et décorations.

Changer l'apparence ne doit pas imposer de modifier les données.

## Placement par lignes virtuelles

La hauteur de la carte est divisée en un nombre configurable de lignes. Chaque élément peut occuper une ligne ou une plage de lignes, avec un alignement horizontal gauche, centre ou droite. Plusieurs éléments peuvent partager la même ligne. Des ajustements en millimètres pourront compléter ce modèle.

Exemple conceptuel pour 12 lignes :

| Élément | Lignes | Alignement |
| --- | --- | --- |
| Titre | 2 | Centre |
| Illustration | 4–7 | Centre |
| Description | 9–10 | Gauche |
| Numéro | 12 | Droite |

## Sources de données

Une carte doit pouvoir être définie directement dans un fichier LaTeX, puis réutiliser exactement le même moteur de rendu pour des cartes importées d'un CSV. Les noms de colonnes doivent rester configurables.

## Macros sémantiques

Une ressource de jeu pourrait être déclarée avec des variantes telles que :

- `\mana` : mot-clé **Mana** ;
- `\mana{5}` : **5 Mana** ;
- `\mana*` : icône ;
- `\mana*{5}` : icône et valeur.

Ce sont des conventions à implémenter, et non des fonctionnalités encore disponibles.

## Hors périmètre initial

ProtoTeX Studio, les interfaces sans LaTeX et la compatibilité Windows pourront être envisagés ultérieurement. Ces perspectives ne doivent pas ralentir la version personnelle LaTeX + CSV.
