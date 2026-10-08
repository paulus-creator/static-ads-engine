# Static Ads Engine — Konstitution

Engine für Static Ads. **Zweck: fertige, postbare Statics mit echtem Produkt und Text im
Bild, gebaut auf bewährten Layout-Mustern, geprüft von einer Jury, entschieden von einem
Menschen.** Marke, Produkte, Preise und Tonalität stehen in `brand/`. Die Engine liest sie,
sie erfindet nichts dazu.

## Sechs Regeln (mehr gibt es nicht)

1. **Referenz führt, Inhalt ist eigen.** Jedes Konzept hat eine Design-Referenz: eine Ad
   mit Reach-Beleg aus dem Markt oder eine vom Art Director markierte Ad aus
   `brand/REFERENZ-ADS.md`. Die Referenz gibt Layout-Familie, Hierarchie, Typo-Charakter
   und gestaltete Elemente vor und geht als Bildreferenz 1 in die Generierung. Produkt,
   Marke, Motiv, Sprache und Wortlaut sind eigen. Ergebnis ist eine eigenständige
   Umsetzung, bei der man das Layout-Muster der Referenz wiedererkennt.
2. **Pipeline über Dateien, Mensch am Ende.** Konzept → Bild → Jury → Übergabe. Agenten
   reden nicht miteinander, sie lesen und schreiben Dateien in `workspace/DATUM/`. Nichts
   wird geschaltet, gepostet oder versendet ohne ausdrückliches Go des Owners.
3. **Echtes Produkt.** Produktreferenz ist immer ein echtes Foto aus
   `brand/assets/products/`, nie ein generiertes Bild. Etiketten-Wortlaut aus
   `brand/PACKAGING.md`. Preise nur aus `brand/OFFERS.md` oder der Live-Seite. Claims nur,
   was `brand/PRODUKTE.md` erlaubt.
4. **Text gehört ins Bild.** Headline, Zeile, CTA werden im Modell generiert, mit dem
   Typo-Charakter der Referenz. Pillow nur für Etikett-Layer, Währungs-Zwillinge und
   punktuelle Korrekturen auf Auflage. Wortbudget im Bild: 12–15 Wörter, drei Ebenen.
5. **Kein Ballast.** Eine neue Regel kommt nur mit einem Bild-Beleg (welches Bild wäre
   ohne sie schlecht geworden?) und ersetzt eine bestehende. Kein Agent liest mehr als
   diese Datei, sein SKILL.md, das RUNBOOK, `brand/` und seine Input-Dateien.
6. **Briefings werden nicht challenged.** Ein Brief des Art Directors (Datei oder Task)
   wird 1:1 umgesetzt: keine Claim-Flags, keine Nachfragen, keine Ziel-URL-Vorschläge.
   Der Art Director entscheidet, Legal prüft intern.

## Struktur

```
CLAUDE.md · ARCHITEKTUR.md · RUNBOOK.md · SETUP.md
agents/        konzept/ · visual/ · jury/ · brief-intake/ · learnings/   (je SKILL.md)
brand/         BRAND.md · PRODUKTE.md · PACKAGING.md · OFFERS.md · FUNNELS.md · REFERENZ-ADS.md
               assets/products/ (echte Fotos) · assets/swipes/ (Referenz-Ads, lokal)
knowledge/     frameworks/ (Hooks, Relevanz-Gate, visuelle Grammatiken, Testing, Urgency, Copy)
workspace/     YYYY-MM-DD/ → 00-leitung.md · 01-konzepte.md · 03-visuals/ · 03b-jury.md · uebergabe/
scripts/       kontaktbogen.py · leak-check.sh
example-brand/ fiktive Marke zum Abschauen
```

## Modelle

| Rolle | Empfehlung |
|---|---|
| Session-Leitung, Konzept (Referenz-Wahl, Angle, Text im Bild) | stärkstes verfügbares Modell (Opus-Klasse oder höher) |
| Visual (Prompt, Generierung, Layer) | Opus-Klasse |
| Jury (frische Augen, Referenz neben Ergebnis) | Opus-Klasse |
| Brief-Intake, Learnings | Sonnet-Klasse |

Kein Haiku. Qualität ist der Engpass, nicht Tokens. Richtwert je Run: ≤ 2 Mio
Subagenten-Tokens, ≤ 60 Credits, ≤ 90 Minuten bis zur Übergabe.

## Sprache und Zeit

Sprache und Orthografie stehen in `brand/BRAND.md` (Default: Deutsch, Schweizer
Orthografie mit ss). Zeitstempel nur per `date`. Keine Läufe gegen Trendtrack, Higgsfield
oder ClickUp ohne Startbefehl des Owners (RUNBOOK).
