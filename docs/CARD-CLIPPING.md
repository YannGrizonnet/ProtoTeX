## Masque global de carte — jalon 0.5

Le rendu de `\ProtoCard` est désormais entièrement découpé selon une silhouette extérieure. La clé de configuration `corner-radius` fixe le rayon de ses coins (en mm), par défaut `2`.

Le clip inclut l'illustration, les aplats, les bandeaux et les composants `overlay`. Le contour extérieur est tracé ensuite, en dehors de la portée de découpe. Le recadrage local de l'illustration continue à fonctionner et se combine avec ce masque global.

Compiler le test depuis la racine du dépôt :

```sh
TEXINPUTS=.: lualatex -halt-on-error examples/clip-test.tex
```

Ce test dessine volontairement des blocs rouges et bleus à cheval sur les coins : ils doivent être découpés par la silhouette arrondie. La commande `\ProtoSetup{corner-radius=4}` modifie conjointement le clip et le contour.

La prise en charge des masques intérieurs décoratifs reste prévue pour un futur jalon.
