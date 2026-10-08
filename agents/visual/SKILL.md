# VISUAL — das Konzept mit dem echten Produkt umsetzen

Du baust je Konzept **3 Kandidaten** (`k1…k3`), die das Layout-Muster der Referenz tragen,
mit dem Produkt, dem Text und der Sprache aus `brand/`. Das Bild ist fertig, wenn man
neben der Referenz die Layout-Familie erkennt und trotzdem nur unser Produkt, unsere
Marke und unseren Wortlaut sieht.

## Inputs

`workspace/DATUM/01-konzepte.md` (oder `01-brief.md` im Brief-Lauf) · die Referenz-Datei
· das genannte echte Produktfoto aus `brand/assets/products/` · `brand/PACKAGING.md`
(Etikett-Wortlaut) · `brand/BRAND.md` (Sprache, Farbwelt, Format) · `brand/OFFERS.md` nur
bei Offer-Konzepten.

## Werkzeug: Higgsfield (Connector)

- `balance` als Verbindungs-Test.
- Modell `nano_banana_pro`, `resolution: 2k`, `aspect_ratio: 4:5` → 1856 × 2304 px,
  2.00 Credits je Render. Bei Ausfall: dreimal wiederholen, dann Blocker melden.
- Referenzen: `media_upload` → `media_confirm` (Status `uploaded`), dann im Job
  `medias: [{role: "image_references", value: <media_id>}, …]`. **Immer zwei Referenzen:
  1 = Design-Referenz, 2 = Produktfoto** (3 = Etikett-Vektor, wenn das Etikett lesbar
  gross ist). `generate_image_batch` mit `requests` als Liste; `jobs_wait`;
  `show_generation_by_ids`.
- **Vor jedem Batch prüfen, dass `medias` gesetzt ist.** Renders ohne Referenzen kosten
  Credits und sind wertlos.
- Nach dem Render: Mittel-Beschnitt auf **1840 × 2300** (Pillow, Box 8,2,1848,2302).

## Was das Modell aus Referenz 1 übernimmt

Das Modell übernimmt Schriftgrösse, Produktgrösse und Elemente (auch Emojis) aus
**Bildreferenz 1**, nicht aus dem Prompt. Wer eine andere Grösse will, braucht ein Bild
mit dieser Grösse als Referenz 1, nicht einen Prompt-Befehl. Störende Elemente in der
Referenz (Emoji, fremdes Logo) vorher mit Pillow abdecken.

## Prompt-Prinzip (ein Prompt = ein fertiges Bild)

1. **Struktur zuerst:** «Use the first reference image as the layout guide: [Layout-Muster
   aus dem Konzept in konkreten Worten — Raster, Flächen, Farben, Position und Grösse der
   Typo, Elemente wie timeline/callout lines/labels/badge].»
2. **Eigen:** «Show the product from the second reference image (exact shape, colour,
   cap, label); use our brand and our wording only; do not copy any lettering, logo,
   person or product from the first reference image.»
3. **Text wörtlich, im Bild:** «The headline reads exactly: … Below, smaller: … The
   button/link reads: … [Sprache] text, exact spelling, typographic character:
   [condensed grotesque, heavy / editorial serif italic / …].»
4. **Kein Text ausser diesem.** «No other text, no watermark, no logo except the label
   on the product.»
5. Für den 2. und 3. Kandidaten: gleicher Prompt, andere Seeds oder leichte
   Motiv-Variation (Produktwinkel, Requisite). Nicht das Layout ändern.
6. **Prompt-Regeln aus der Praxis:** Text im Prompt nie in Anführungszeichen oder
   Guillemets setzen, das Modell schreibt sie ins Bild. Fett-Stellen als eigene Liste am
   Prompt-Ende, nicht inline markiert. Verpackungen im Hintergrund **positiv** briefen
   («every carton carries only the words [Marke] and [Produkt]» oder «plain, no
   lettering»); ein Verbot allein hält fremden Wortlaut nicht fern. Das Produktfoto ist in
   **jeder** Generierung Bildreferenz, nie nur Textbeschreibung. Umbruch-Befehle («line
   break after …») erzeugen Trennzeichen im Bild; stattdessen die Zeilen als getrennte
   Elemente beschreiben.

Personen: Gesicht nur, wenn die Referenz ein Gesicht trägt; natürliche Haut, Alter passend
zur Zielgruppe aus `brand/BRAND.md`. Keine Spiegel, keine Handys im Bild, ausser die
Referenz verlangt es.

## Produktwahrheit (die einzige harte Regel)

- Produktreferenz ist ein **echtes Foto** aus `brand/assets/products/`, nie ein
  generiertes Bild.
- Fehlt ein echtes Foto für eine Produktvariante: Hardware (Flakon, Tube, Dose) aus dem
  Foto einer Schwester-Variante + Prompt-Klausel «label is a plain [Farbe] band, ignore
  the colour and wording of the reference label» + **Etikett als Vektor-Layer** mit
  Pillow (Zylinder-Mapping). Nie ein Etikett generieren lassen.
- Etikett lesbar im Bild ⇒ Wortlaut = `brand/PACKAGING.md`, Buchstabe für Buchstabe
  (Zoom-Beleg). Weicht es ab: Layer statt Neu-Render.
- Preise im Bild Ziffer für Ziffer gegen das Konzept prüfen.
- Text im Bild zeichengenau gegen das Konzept prüfen (Zoom auf jede Zeile). Ein
  Rechtschreibfehler ⇒ dieser Kandidat fällt, kein Pillow-Flicken über generiertem Text.
- **Selbstcheck nur per Ausschnitt-Zoom** (Pillow-Crop je Textzeile, Hände, Produkt,
  Kartonaufdrucke, Überdeckungen). Die Vollansicht übersieht kopflose Figuren,
  Fingerstummel und Objekte im Wort. Kartonaufdrucke Buchstabe für Buchstabe gegen den
  eigenen Produktnamen prüfen.

## Pillow (nur hier)

Etikett-Layer · Währungs-Zwillinge (Text-Layer über dem gewählten Final, nach Auswahl
durch den Art Director) · punktuelle Korrekturen auf Auflage der Jury oder des Art
Directors (eine Änderung, Diff ausserhalb der Zone 0). Nicht: Headlines setzen, Layouts
bauen, Collagen montieren.

## Output

`workspace/DATUM/03-visuals/<konzept>/k1.png … k3.png` (1840 × 2300) und je Konzept
`PROMPTS.md`: Referenz-Media-IDs, Prompt je Kandidat, Job-ID, Credits, Selbstcheck
(Text ✓ / Etikett ✓ / Preis ✓ / Layout-Muster erkennbar: ja, weil …). Retry nach Jury:
genau die Auflage umsetzen, `k<n>-r1.png`, einmal.

Zeit per `date`. Budget je Konzept: 3 Renders + 2 Reserve.
