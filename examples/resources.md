# Ressources et capacités — essai du jalon 0.3

Compiler à la racine :

```sh
TEXINPUTS=.: lualatex -interaction=nonstopmode -halt-on-error examples/resources.tex
```

## Commandes expérimentales

Déclarer une ressource avec `\ProtoDeclareResource{mana}{Mana}{blue!65!black}{M}`.

La déclaration crée une commande `\mana` avec quatre variantes :

| Appel | Résultat |
| --- | --- |
| `\mana` | **Mana** |
| `\mana{5}` | **5 Mana** |
| `\mana*` | Icône ronde portant le glyphe M |
| `\mana*{5}` | **5** suivi de l'icône ronde M |

Le dernier argument de la déclaration est un glyphe arbitraire (lettre ou symbole LaTeX), pas une image imposée. Le thème pourra lui substituer un véritable pictogramme dans une prochaine évolution.

`\ProtoAbility{Activation}{Texte}` produit un intitulé en gras suivi du texte de capacité.

`\ProtoFlavor{Texte}` produit un paragraphe en italique.

Ces commandes sont utilisables dans les zones de texte et cartouches LaTeX. Elles ne décrivent aucune règle propre à un jeu.

## Limites

API provisoire, pas de contrôles de collision et pas de diminution automatique de la taille de police. Une ressource ne doit pas réutiliser un nom de commande déjà défini. Les icônes sont intentionnellement rudimentaires pour ce jalon.
