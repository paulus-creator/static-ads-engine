# Static Ads Engine

Eine Pipeline aus fünf Claude-Code-Agenten, die aus einer Design-Referenz, einem echten
Produktfoto und einem Text ein fertiges, postbares Static Ad baut, es durch eine Jury
schickt und dem Menschen zur Auswahl vorlegt. Marke, Produkte und Preise kommen aus einem
Ordner `brand/`, den du selbst füllst. Die Engine kennt keine Marke, bis du ihr eine gibst.

```
Konzept  →  Visual  →  Jury  →  Übergabe an dich
(Referenz,   (Bild mit    (drei Fragen,   (Kontaktbogen, Ordner,
 Produkt,     Text im      Verdikt,        optional Figma-Board)
 Text)        Bild)        Auflage)
```

## Was du brauchst

| Was | Wofür | Pflicht |
|---|---|---|
| Claude Code (Desktop oder CLI) mit Zugang zu Opus-Klasse-Modellen | Alle Agenten | ja |
| Higgsfield-Connector mit eigenem Guthaben | Bildgenerierung (Nano Banana Pro) | ja |
| Python 3 + Pillow (`pip3 install Pillow`) | Kontaktbogen, Beschnitt, Text-Layer | ja |
| Trendtrack-Connector | Referenz-Ads aus dem Markt mit Reach-Beleg | empfohlen |
| Figma-Connector | Review-Board für Art Director | optional |
| ClickUp-Connector | Briefings direkt aus Tasks lesen | optional |
| Meta-Marketing-API-Token (nur lesend) | Learnings: was im Konto gewinnt | optional |

## Installation in fünf Schritten

1. Repo klonen (oder auf GitHub «Use this template» und dann klonen).
2. In Claude Code als Projektordner öffnen. `CLAUDE.md` wird automatisch gelesen.
3. `brand/` füllen: `BRAND.md`, `PRODUKTE.md`, `PACKAGING.md`, `OFFERS.md`, `FUNNELS.md`.
   Echte Produktfotos nach `brand/assets/products/`. Vorlage zum Abschauen: `example-brand/`.
4. `.env.example` nach `.env` kopieren und nur die Felder füllen, die du nutzt.
5. Connectoren in Claude Code verbinden (Higgsfield, optional Trendtrack/Figma/ClickUp),
   dann in der Session: «Run 1 gemäss RUNBOOK. Freigabe erteilt.»

Details, Stolpersteine und ein Testlauf ohne Credits: `SETUP.md`.

## Dateien

```
CLAUDE.md        Die sechs Regeln. Wird von jeder Session gelesen.
ARCHITEKTUR.md   Fünf Agenten, Dateifluss, Modelle.
RUNBOOK.md       Ein Run in vier Schritten, Budget, Feedback-Runde.
SETUP.md         Einrichtung, Connectoren, Testlauf.
agents/          Ein Ordner je Agent mit SKILL.md.
brand/           Deine Marke. Vorlagen mit Ausfüll-Anleitung.
knowledge/       Frameworks: Hooks, Relevanz-Gate, Grammatiken, Testing, Urgency.
scripts/         kontaktbogen.py · leak-check.sh
workspace/       Ein Ordner je Run (DATUM/). Nicht im Repo.
example-brand/   Fiktive Marke mit einem Produkt, zum Abschauen.
```

## Was die Engine nicht tut

Sie schreibt keine Ad-Copy (Primary Text, Meta-Headline). Sie schaltet nichts, postet
nichts, versendet nichts. Sie erfindet keine Produktfakten, Preise oder Zitate.
