# Exemple de superpositions — jalon 0.2

Compiler à la racine du dépôt :

```sh
TEXINPUTS=.: lualatex -interaction=nonstopmode -halt-on-error examples/zones.tex
```

Le fichier utilise les images fictives `example-image-a` et `example-image-b` de TeX Live (package `mwe`). Aucune image commerciale n'est utilisée.

## Primitives expérimentales

Les composants facultatifs sont fournis dans la propriété `overlay` de `\ProtoCard` et dessinés **après** l'image et le texte, dans l'ordre donné :

- `\ProtoBand[row=7,fill=teal!75!black]{DÉFENSEUR}` : bandeau couvrant toute la largeur de la carte.
- `\ProtoPanel[from=3,to=4,align=right,width=15,fill=orange]{5}` : cartouche rectangulaire. La largeur est en millimètres ; la hauteur dépend des lignes virtuelles.
- Le cartouche admet `draw`, `text-color`, `font` et `inset`.

`align` pour les cartouches vaut `left`, `center` ou `right`. Le fond et le texte peuvent recouvrir les illustrations, bandeaux et descriptions. Chaque composant gère son contenu LaTeX, y compris le gras et l'italique.

## Limites

API provisoire ; pas de calcul des collisions ni d'adaptation des textes longs. Les cartouches recouvrent les éléments placés en dessous. Les fonds des bandeaux sont toujours rectangulaires et sans réglage de transparence pour l'instant.
