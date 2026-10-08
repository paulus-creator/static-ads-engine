# SETUP — Engine einrichten

## 1. Marke anlegen (`brand/`)

Jede Datei in `brand/` ist eine Vorlage mit Kommentaren, was hineingehört. Fülle sie in
dieser Reihenfolge, die Agenten lesen sie genau so:

| Datei | Inhalt | Wer liest sie |
|---|---|---|
| `BRAND.md` | Markenname, Sprache, Märkte, Währungen, Tonalität, Rollen im Team, optionale Tool-IDs | alle |
| `PRODUKTE.md` | Je Produkt: Name, Form, Farbe, erlaubte Claims, verbotene Claims, Foto-Pfad | Konzept, Visual, Jury |
| `PACKAGING.md` | Wortgenauer Etiketten-Text je Produkt | Visual, Jury |
| `OFFERS.md` | Aktive Angebote mit Preis, Streichpreis, Gültigkeit, Quelle | Konzept, Visual |
| `FUNNELS.md` | Ziel-URLs je Produkt und Awareness-Stufe | Konzept |
| `REFERENZ-ADS.md` | Messlatte: Ads, die dein Art Director als Niveau markiert, plus belegte Winner | Konzept, Jury, Learnings |

Echte Produktfotos nach `brand/assets/products/<PRODUKTKUERZEL>/`. Freisteller, Packshot,
Flakon von vorn, bei Bedarf Schachtel. Nie generierte Bilder dort ablegen (Regel 3).

Ein ausgefülltes Beispiel liegt in `example-brand/` (fiktive Marke, ein Produkt).

## 2. Secrets (`.env`)

```bash
cp .env.example .env
```

Nur füllen, was du nutzt. Higgsfield, Trendtrack, Figma und ClickUp laufen über
Connectoren in Claude Code, nicht über `.env`. Die `.env` ist per `.gitignore` vom Repo
ausgeschlossen. Niemals Tokens in Markdown-Dateien notieren.

## 3. Connectoren in Claude Code

- **Higgsfield** (Pflicht): Connector verbinden, in der Session `balance` aufrufen. Wenn
  ein Guthaben zurückkommt, ist alles bereit. Modell `nano_banana_pro`, 2k, 4:5 kostet
  2.00 Credits je Render. Ein Standard-Run mit 5 Konzepten braucht rund 30 Renders.
- **Trendtrack** (empfohlen): liefert Referenz-Ads mit Reach- und Laufzeit-Beleg. Ohne
  Trendtrack nimmt KONZEPT Referenzen aus `brand/REFERENZ-ADS.md` oder du legst Bilder
  manuell in `brand/assets/swipes/` ab (Meta Ad Library, Screenshots).
- **Figma** (optional): Review-Board, auf dem Referenz und Ergebnis nebeneinander liegen.
  Ohne Figma gibt es den Kontaktbogen als PNG plus den Übergabe-Ordner.
- **ClickUp** (optional): BRIEF-INTAKE liest Tasks direkt. Listen-ID und Mention-IDs
  trägst du in `brand/BRAND.md` ein. Ohne ClickUp: Brief als Markdown-Datei ablegen.

## 4. Python

```bash
pip3 install Pillow
python3 scripts/kontaktbogen.py --help
```

## 5. Testlauf ohne Credits

Bevor du Guthaben ausgibst: Kopiere `example-brand/` testweise nach `brand/` und starte
in Claude Code «Konzept-Lauf gemäss RUNBOOK, ohne Visual». Du bekommst
`workspace/DATUM/01-konzepte.md` und siehst, ob die Agenten deine Brand-Dateien richtig
lesen. Danach `brand/` mit deiner echten Marke füllen.

## 6. Leak-Check (empfohlen, wenn du das Repo weitergibst)

`scripts/leak-check.sh` prüft vor jedem Commit, dass keine Secrets, keine grossen
Dateien und keine Begriffe aus einer Sperrliste ins Repo gelangen. Die Sperrliste liegt
**ausserhalb** des Repos (sonst würde sie verraten, was sie schützt):

```bash
cp scripts/leak-check.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
echo "/pfad/zu/deiner/sperrliste.txt" > .git/leak-sperrliste-pfad
```

Die Sperrliste ist eine Textdatei, ein Begriff je Zeile (Markennamen, Personennamen,
interne IDs). Ohne Sperrliste laufen nur die generischen Prüfungen (Token-Muster,
`.env`, Dateien über 1 MB). Vollständiger Scan: `scripts/leak-check.sh --all`.

## Stolpersteine aus der Praxis

- Das Bildmodell übernimmt Schriftgrösse, Produktgrösse und Elemente aus **Bildreferenz 1**,
  nicht aus dem Prompt. Referenz 1 ist darum immer die Design-Referenz, Referenz 2 das Produktfoto.
- Text im Prompt nie in Anführungszeichen setzen, das Modell schreibt sie ins Bild.
- Verpackungen im Hintergrund positiv briefen («every carton carries only the words X»),
  ein Verbot allein hält fremden Wortlaut nicht fern.
- Vor jedem `generate_image_batch` prüfen, dass `medias` gesetzt ist. Renders ohne
  Referenzen kosten Credits und sind wertlos.
- Selbstcheck nur per Ausschnitt-Zoom je Textzeile. Die Vollansicht übersieht Fehler.
