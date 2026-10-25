#!/usr/bin/env python3
"""Experimental CSV rule matrix -> ProtoTeX LaTeX. Only trusted local rules."""
import csv
import re
import argparse
from collections import defaultdict
from pathlib import Path

def read(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))

def tex(value):
    chars = {"\\":r"\textbackslash{}", "&":r"\&", "%":r"\%",
             "$":r"\$", "#":r"\#", "_":r"\_", "{":r"\{",
             "}":r"\}", "~":r"\textasciitilde{}", "^":r"\textasciicircum{}"}
    return "".join(chars.get(c,c) for c in str(value))

def applies(card, rule):
    key = rule["attribute"]
    if key not in card:
        raise ValueError(f"Unknown card attribute {key}")
    if key == "keywords":
        return rule["value"] in [v.strip() for v in card[key].split(",")]
    return card[key] == rule["value"]

def build(cards, rules):
    output = [r"""\documentclass[a4paper]{article}
\usepackage[margin=9mm]{geometry}
\usepackage{prototex}
\pagestyle{empty}
\begin{document}
\noindent
"""]
    setters = {("title","fill"),("number","prefix"),("rarity","symbol"),("layout","orientation")}
    appends = {("title-icons","symbol")}
    visibility = {("attack","visible")}
    for index, card in enumerate(cards):
        state = {"title.fill":"gray!70!black", "number.prefix":"",
                 "rarity.symbol":"", "layout.orientation":"portrait",
                 "attack.visible":True}
        additions = defaultdict(list)
        seen = {}
        matching = sorted((r for r in rules if applies(card,r)),key=lambda r:int(r.get("priority") or 0))
        for rule in matching:
            key=(rule["component"], rule["property"])
            op=rule["operation"]
            val=rule["result"]
            priority=int(rule.get("priority") or 0)
            if op=="set" and key in setters:
                if key==("title","fill") and not re.fullmatch(r"[A-Za-z0-9!]+",val):
                    raise ValueError("Invalid color")
                if key==("layout","orientation") and val not in ("portrait","landscape"):
                    raise ValueError("Invalid orientation")
                if key in seen and seen[key][0]==priority and seen[key][1]!=val:
                    raise ValueError(f"Conflicting rules: {key}")
                state[".".join(key)]=val
                seen[key]=(priority,val)
            elif op=="append" and key in appends:
                additions[key].append(val)
            elif op in ("show","hide") and key in visibility:
                state["attack.visible"]=(op=="show")
            else:
                raise ValueError(f"Unsupported rule {rule}")
        portrait=state["layout.orientation"]=="portrait"
        w,h=(63,88) if portrait else (88,63)
        desc=9 if portrait else 8
        output.append(r"\ProtoSetup{width="+str(w)+",height="+str(h)+
                      ",rows=12,padding=3,band-color="+state["title.fill"]+"}\n")
        output.append(r"\ProtoLayout{title-row=2,image-from=3,image-to=7,description-from="+str(desc)+
                      ",description-to="+str(desc+2)+",number-row=12}\n")
        icons=" ".join(tex(v) for v in additions[("title-icons","symbol")])
        badge=(r"\ProtoPanel[from=1,to=1,align=left,width=15,fill=cyan!15,font=\small]{"+icons+"}") if icons else ""
        rarity=tex(state["rarity.symbol"])
        if rarity=="*": rarity=r"$\star$"
        rarepanel=(r"\ProtoPanel[from=12,to=12,align=left,width=13,fill=yellow!20,font=\bfseries\scriptsize]{"+rarity+"}")
        stats=[]
        if state["attack.visible"] and card.get("attack"):
            stats.append("ATQ "+tex(card["attack"]))
        if card.get("defense"):
            stats.append("DEF "+tex(card["defense"]))
        statpanel=(r"\ProtoPanel[from=8,to=8,align=center,width="+str(28 if portrait else 35)+
                   r",fill=white,draw=black!50,font=\scriptsize]{"+r"\quad ".join(stats)+"}") if stats else ""
        img=card["image"]
        if not re.fullmatch(r"[A-Za-z0-9_./-]+",img):
            raise ValueError("Invalid image path")
        output.append(r"\ProtoCard[title={"+tex(card["title"])+"},image={"+img+
                      "},description={"+tex(card["description"])+"},number={"+
                      tex(state["number.prefix"]+card["id"])+
                      "},overlay={"+badge+statpanel+rarepanel+"}]\n")
        continuation=(index+1<len(cards) and portrait and cards[index+1].get("category")==card["category"])
        output.append((r"\hspace{3mm}" if continuation else r"\par\medskip")+"\n")
    output.append(r"\end{document}"+"\n")
    return "".join(output)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--cards",default="examples/matrix/cards.csv")
    p.add_argument("--styles",default="examples/matrix/styles.csv")
    p.add_argument("--output",default="examples/matrix/generated.tex")
    args=p.parse_args()
    target=Path(args.output)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(build(read(args.cards),read(args.styles)),encoding="utf-8")
    print(target)
