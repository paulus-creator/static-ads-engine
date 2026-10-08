# KONZEPT — Referenz, Produkt, Angle, Text

Du lieferst je Run **5 Konzepte**. Ein Konzept = **eine Design-Referenz** (Ad mit
Reach-Beleg aus dem Markt oder Art-Director-Auswahl) + **ein Produkt** aus
`brand/PRODUKTE.md` + **ein Angle** + **der Text im Bild**. Du schreibst genau eine Datei:
`workspace/DATUM/01-konzepte.md`. Keine Ad-Copy.

## Inputs (in dieser Reihenfolge)

1. `brand/BRAND.md` — Sprache, Märkte, Währungen, Zielgruppen, Formate.
2. `brand/REFERENZ-ADS.md` — Teil A (Art-Director-Auswahl) hat Vorrang: Ist dort eine Ad
   noch nicht umgesetzt, nimm sie zuerst. Teil C (eigene Winner) sind die beste Referenz
   für Iterationen (gleiches Layout, neuer Hook oder neues Produkt).
3. `workspace/` — die letzten 3 `01-konzepte.md` (keine Wiederholung derselben Referenz
   oder desselben Arguments).
4. Trendtrack (MCP, falls verbunden): `search_ads` mit `media_type: image`, Länder und
   Sprache aus `brand/BRAND.md`, Sortierung `reachDelta7d` oder `longestRunning`;
   zweiter Durchgang in der eigenen Kategorie, dritter Durchgang in **fremden Nischen mit
   starkem Layout** (Layout-Muster sind produktunabhängig). `scan_ad` auf Kandidaten.
   Winner-Kriterium: `status: active` **und** (`daysRunning ≥ 30` oder `reach ≥ 100'000`
   oder `duplicates ≥ 2`). Zahlen mit Feldnamen zitieren, nie runden.
   Ohne Trendtrack: Referenzen aus `brand/assets/swipes/` (vom Owner abgelegt).
5. `brand/PRODUKTE.md` (erlaubte Claims, Priorität der Produkte), `brand/FUNNELS.md`
   (Destination je Produkt und Awareness-Stufe), `brand/OFFERS.md` (Offer-Konzepte: Preis
   nur von dort oder von der Live-Seite), `00-leitung.md` (Lage des Tages).
6. `knowledge/frameworks/relevanz-gate.md` und `hooks-und-angles.md` für den Anker und
   die Hook-Muster, `visuelle-grammatiken.md` für die Vielfalt der Layout-Familien.

## Was ein Konzept braucht

- **Fünf Referenzen = fünf Layout-Familien.** Kein Layout-Typ doppelt im Run (z. B.
  Split-Karte · annotiertes Foto · Zeitleiste/Schritte · Review-Grid · Poster/Text-only ·
  Vorher/Nachher-Tabelle · Collage mit Typo-Block). Auf dem Kontaktbogen müssen die fünf
  auf 270 px sofort als fünf verschiedene Ads erkennbar sein.
- **Referenz:** Marke, Ad-ID, Beleg (`daysRunning`, `reach`, `duplicates`, `status`),
  lokale Datei. **Download-Pflicht:** `curl` auf die Media-URL nach
  `brand/assets/swipes/<thema>/<brand-slug>__<ad-id>.<ext>` + Zeile in dessen `INDEX.md`.
  Optional per `add_board_item` in ein Trendtrack-Board (ID in `brand/BRAND.md`), damit
  der Owner jede Referenz dort sehen kann.
- **Layout-Muster der Referenz (3 Zeilen):** Layout (Raster, Flächen, Produktposition) ·
  Typo (Schnitt-Charakter, Gewicht, Grösse relativ zum Format, Farbe) · Elemente
  (Zeitleiste, Callout, Label-Paar, Badge, Pfeil, Sticker …). **Das übernimmt VISUAL als
  Struktur.**
- **Was eigen ist:** Produkt (welches echte Foto aus `brand/assets/products/`), Marke,
  Personen/Motiv, Sprache, Wortlaut, Farbwelt, wenn `brand/BRAND.md` eine vorgibt.
- **Zielprodukt + Destination** (URL) + Zielgruppe (aus `brand/BRAND.md`; Mix über den Run).
- **Angle in einem Satz** (wen spricht das Bild an, mit welchem Versprechen). Die
  Angle-Zeile geht so an den Copywriter. Relevanz-Anker sichtbar im Bild: erwogene oder
  gescheiterte Lösung, gelebter Moment oder Fehlannahme (`relevanz-gate.md`). Eine fremde
  Person versteht in einer Sekunde, worum es geht.
- **Text im Bild, wörtlich:** Headline (≤ 8 Wörter), optional Zeile, optional CTA-Element
  (nur wenn die Referenz eines hat). Gesamt ≤ 15 Wörter, ≤ 3 Ebenen. Claim-Regeln aus
  `brand/PRODUKTE.md` gelten; Zahlen nur belegt.
- **Offer-Konzepte:** Preis, Streichpreis, Ersparnis je aus `brand/OFFERS.md`; je Währung
  den Wortlaut angeben (Schreibweise aus `brand/BRAND.md`).

## Format `01-konzepte.md`

```markdown
# Konzepte — JJJJ-MM-TT (Zeit per date)

## Lage in 3 Sätzen
[Was läuft im Konto, was im Feed skaliert, welche Referenz-Ads offen sind]

## Konzept 1: [Kurzname]  ·  Produkt: [Kürzel]  ·  Zielgruppe: […]
- **Referenz:** [Marke] · `<ad-id>` · daysRunning … · reach … · duplicates … · status …
  · Datei `brand/assets/swipes/<thema>/<datei>`
- **Layout-Muster:** Layout: … · Typo: … · Elemente: …
- **Eigen:** Produkt → `brand/assets/products/<…>` · Motiv → … · Wortlaut → unten
- **Angle-Zeile:** …
- **Destination:** [URL] — Message Match: [welcher Einstieg der Seite]
- **Text im Bild:** Headline «…» · Zeile «…» · CTA «…»
- **Offer (nur Offer-Konzepte):** [Währung 1] … / [Währung 2] … · Streichpreis … · Ersparnis …
- **Hinweis:** [Risiko, Legal, was VISUAL wissen muss — ein Satz]

## Konzept 2 … 5

## Verworfen
[2–3 Kandidaten, je ein Satz]
```

## No-Gos

Keine Meta-Headline, kein Primary Text. Keine zwei Konzepte mit demselben Argument. Keine
Referenz ohne lokale Datei und Beleg. Keine Produktfakten, die nicht in
`brand/PRODUKTE.md` oder auf der Website stehen. Nichts auf Trendtrack löschen.
