# Exemple de carte — ProtoTeX 0.1

Depuis la racine du dépôt, compiler avec :

```sh
TEXINPUTS=.: lualatex -interaction=nonstopmode -halt-on-error examples/first-card.tex
```

Le résultat est `first-card.pdf`. L'illustration `example-image` est fournie par le package LaTeX `mwe`, couramment présent dans TeX Live ; elle sert seulement de substitut.

## API expérimentale

- `\ProtoSetup{width=63,height=88,rows=12,padding=3,...}` configure les dimensions en millimètres.
- `\ProtoLayout{title-row=2,image-from=4,image-to=7,...}` définit les zones.
- `\ProtoCard[title={...},image={...},description={...},number={...}]` crée une carte.

La numérotation des lignes commence à **1 en haut de la carte**. Les alignements disponibles sont `left`, `center` et `right`.

## Limitations connues

- Les champs de texte ne sont pas automatiquement ajustés : un texte trop long peut déborder.
- L'alignement `description-align` gère l'alignement du texte mais pas encore la position globale de son bloc.
- Les images remplissent toute la zone sans déformation : elles sont agrandies proportionnellement puis recadrées au centre (comportement « cover »).
- Pas encore d'import CSV, de génération de planches ou d'icônes sémantiques.
- Les paramètres de mise en page ne sont pas encore validés (plages de lignes, dimensions positives).
