# RUNBOOK — ein Run in vier Schritten

Start nur auf Startbefehl des Owners. Eine Session = ein Run. Zeit per `date`.

| Zweck | Startbefehl |
|---|---|
| Regulärer Run (Statics + Offer) | «Run N gemäss RUNBOOK. Freigabe erteilt.» — optional Fokus-Produkt, Anzahl Konzepte |
| Nur Konzepte, keine Bilder (Testlauf) | «Konzept-Lauf gemäss RUNBOOK, ohne Visual.» |
| Brief-Lauf, Run 1 | «Brief-Lauf für `<brief-id oder datei>` gemäss RUNBOOK. Freigabe erteilt.» |
| Brief-Lauf, Run ≥ 2 (nach Feedback) | «Brief-Lauf für `<id>`, Run 2 gemäss RUNBOOK. Freigabe erteilt.» |
| Feedback-Runde zu einer Übergabe | «Art Director hat kommentiert, Feedback-Runde zu Run N.» |
| Learnings | «LEARNINGS-Lauf gemäss agents/learnings/SKILL.md.» |

Die Freigabe deckt: lesende Zugriffe (Trendtrack, Umsatz-Tool, Werbekonto, Tasks,
Websites), Bild-Generierung (Higgsfield), alle Dateien im Projekt. Nicht gedeckt:
irgendetwas live schalten, posten oder senden. Ein Post in einen Task oder Kanal braucht
ein eigenes Go je Lauf.

## Umfang und Budget (Default)

- **5 Konzepte je Run** (4 Statics + 1 Offer, oder wie im Startbefehl). Je Konzept **eine
  Referenz, ein Produkt, ein Text**, daraus **3 Kandidaten** (Neu-Renders derselben
  Umsetzung). Jury liefert die besten **bis zu 3** je Konzept (Minimum 2; darunter ein
  Retry, max. 1 je Konzept).
- **Budget:** ≤ 30 Renders / ≤ 60 Credits (2.00 je Render, Nano Banana Pro 2k) ·
  ≤ 2 Mio Subagenten-Tokens · Übergabe nach ≤ 90 Minuten. Überschreitung ist kein
  Fehler, steht aber in `06-kosten.md`.
- **Format:** 4:5, 1840 × 2300 px (Render 1856 × 2304, Mittel-Beschnitt). Andere Formate
  in `brand/BRAND.md` festlegen. Offer-Konzepte zusätzlich als Währungs-Zwillinge
  (deterministischer Text-Layer, 0 Credits), erst nach Auswahl durch den Art Director.
- **Keine Ad-Copy.** Übergabe je Konzept: Bilder + eine Angle-Zeile + Destination.

## Ablauf

0. **Leitung:** `date`, Ordner `workspace/YYYY-MM-DD/`, Higgsfield `balance` (Referenz),
   optional eine Umsatz-Abfrage (welches Produkt läuft) → 5 Zeilen in `00-leitung.md`.
   Bei Offer-Konzepten: Preis der Ziel-Offer auf der Live-Seite nachsehen und in
   `brand/OFFERS.md` mit Datum bestätigen.
1. **KONZEPT** (ein Subagent) → `01-konzepte.md`. Liest zuerst `brand/REFERENZ-ADS.md`
   (Art-Director-Auswahl hat Vorrang), dann Trendtrack.
2. **VISUAL** (1–2 Subagenten parallel, Konzepte aufgeteilt) → `03-visuals/`.
3. **JURY** (ein Subagent, frische Augen, liest VISUALs Prompts nicht vorab) →
   `03b-jury.md` + Kontaktbogen. Bei RETRY: VISUAL einmal nachbessern, JURY nachjurieren.
4. **Leitung:** `uebergabe/<konzept>/bild-01…03.png` (nur SCHALTBAR) + `README.md`
   (je Konzept: Referenz, Angle-Zeile, Destination, Bilder) · `06-kosten.md` (Credits aus
   Higgsfield `transactions` im Zeitfenster, Tokens aus den Subagenten-Bilanzen, Wanduhr)
   · **Review-Artefakt** (unten) · Abschluss-Meldung: 3 Zeilen je Konzept, Link, Kosten, Blocker.

## Review-Artefakt

Minimum: `03b-kontaktbogen.png` mit Referenzen als markierte Kacheln plus der
Übergabe-Ordner. Empfohlen, wenn Figma verbunden ist: neues Design-File «Run N — Statics
Review (JJJJ-MM-TT)», je Konzept eine Sektion, **Referenz links, eigene Bilder rechts**,
je Bild ein Urteilsfeld «behalten / ändern: __ / raus, weil: __», Fragen direkt am Bild,
Ausschuss mit Bild. Bau: `create_new_file` → `upload_assets` → `use_figma` (Sektionen,
Textknoten, Urteilsfelder) → `get_screenshot` zur Kontrolle.

Der Art Director wählt eine Idee und gibt Änderungen. Das Board fragt nicht «3 behalten»,
sondern bietet Einzelurteile.

## Feedback-Runde

Kommentare lesen (Board, Task oder Datei) → `FEEDBACK-RUN-N.md` im Run-Ordner (Tabelle:
Bild · Urteil · Wortlaut) → Auflagen an VISUAL (eine Änderung je Bild, deterministisch
wo möglich) → JURY → `uebergabe/` v2 → Review-Artefakt Seite 2.

## Brief-Lauf

Quelle des Briefs steht in `brand/BRAND.md` (ClickUp-Liste, Notion, Ordner mit
Markdown-Dateien). Status «briefing» oder «in revision» = Engine darf starten.

1. **BRIEF-INTAKE** → `01-brief.md` (Copy wörtlich, Design-Code, Format, Fassungen) +
   `01-referenzen/`. Run ≥ 2: zuerst Feedback konsolidieren.
2. **VISUAL**: Referenz = Referenzbild aus dem Brief (sonst eine REFERENZ-AD), Copy 1:1.
   3 Kandidaten je Brief.
3. **JURY**: Brief-Treue (Text zeichengenau, Design-Code) + Blocker + 1-Sekunden-Test.
4. **Leitung, nach Go des Owners:** Bilder an den Task oder Ordner, Kommentar als reiner
   Text, Status gemäss `brand/BRAND.md`. Finals heissen
   `<PROD>_B<n>_s<k>_FINAL[-<WÄHRUNG>]_<id>.png`. Die Engine setzt nie einen
   Launch-Status.
