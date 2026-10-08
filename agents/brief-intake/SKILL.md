# BRIEF-INTAKE — den Brief des Art Directors in eine Datei

Du übersetzt einen Brief in `workspace/DATUM/brief-<id>/01-brief.md`. Du challengst
nicht: keine Claim-Flags, keine Nachfragen, keine Ziel-URLs. Was im Brief steht, wird
gebaut (Regel 6).

Quelle des Briefs steht in `brand/BRAND.md`, Abschnitt «Briefings». Drei Fälle:

| Quelle | Lesen mit |
|---|---|
| ClickUp-Task | `clickup_get_task` (Listen-ID aus BRAND.md) → Titel, Beschreibung, Custom Fields, Anhänge; PDF per `clickup_download_task_attachment` laden und lesen |
| Markdown-Datei im Ordner | Datei lesen; Referenzbilder liegen daneben |
| Notion, Slack, E-Mail | mit dem jeweiligen Connector lesen; sonst bittet die Leitung den Owner, den Brief als Datei abzulegen |

## Run 1

1. Brief lesen (siehe Tabelle). `<id>` = Task-ID oder Dateiname ohne Endung.
2. Referenzbilder aus Brief/PDF nach `01-referenzen/` (eine Datei je Referenz, Herkunft
   in `01-referenzen/INDEX.md`).
3. `01-brief.md` schreiben:

```markdown
# Brief — <id> · <Produkt> · <Titel>  (Zeit per date)
- Anzahl Briefs/Fassungen: … · Format: … (Standard aus brand/BRAND.md) · Märkte: …
- Design-Code: [Farben, Typo, Logo-Position, Elemente — wörtlich aus dem Brief]
- Referenzbild je Brief: `01-referenzen/<datei>` — was davon als Struktur übernommen wird

## Brief 1
| Element | Text im Bild (wörtlich) | Hierarchie |
|---|---|---|
| Headline | … | gross |
| Zeile | … | mittel |
| CTA/Preis | … | … |
- Produkt-Referenz: `brand/assets/products/<…>` · Preis je Währung … (falls Preis-Brief)
- Besonderes: …
```

4. Zeile im Register (`workspace/BRIEF-REGISTER.md`: id, Produkt, Briefs, Status, Pfad).

## Run ≥ 2 (Feedback)

Kommentare lesen (`clickup_get_task_comments` oder Feedback-Datei) → `FEEDBACK-R<n-1>.md`:
je Datei Rein / Raus / ändern mit Wortlaut. Daraus:

- **Fall A** (Auswahl ohne Auflage) → Währungs-Zwillinge, FINAL-Dateien.
- **Fall B** (eine Änderung je Bild) → VISUAL deterministisch per Pillow (Diff ausserhalb
  der Zone 0, 0 Credits) oder Neu-Render, wenn die Änderung das Motiv betrifft.
- **Fall C** (alles raus) → neuer Run 1.

Den Fall benennen, mehr nicht.

Naming der Lieferbilder: `<PROD>_B<n>_s<k>_v<run>_<id>.png`, Finals
`<PROD>_B<n>_s<k>_FINAL[-<WÄHRUNG>]_<id>.png`.
