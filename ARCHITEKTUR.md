# Architektur — Kern-Engine

## Zielbild

Ein Ablauf, zwei Einstiege, ein Ausgang:

```
Einstieg A  KONZEPT            Referenz wählen · Produkt · Angle · Text im Bild
Einstieg B  BRIEF-INTAKE       Brief des Art Directors 1:1 (Copy, Referenzbild, Design-Code)
                 │
                 ▼
            VISUAL             Referenz + Produktfoto als Bildreferenzen → 3 Kandidaten je Konzept
                 │
                 ▼
            JURY               Referenz neben Ergebnis · Blocker · 1-Sekunden-Test → beste 3
                 │
                 ▼
            LEITUNG            Übergabe-Ordner · Kontaktbogen · optional Figma-Board oder Task-Post
```

Dateien je Run in `workspace/YYYY-MM-DD/` (Brief-Läufe: `workspace/YYYY-MM-DD/brief-<id>/`):

| Schritt | schreibt | liest |
|---|---|---|
| Leitung | `00-leitung.md` | `brand/BRAND.md`, Higgsfield `balance`, optional Umsatz-Tool |
| Konzept | `01-konzepte.md` | `brand/REFERENZ-ADS.md`, `brand/PRODUKTE.md`, `brand/OFFERS.md`, `brand/FUNNELS.md`, Trendtrack, die letzten 3 Runs |
| Brief-Intake | `01-brief.md` + `01-referenzen/` | Brief (Datei, ClickUp-Task, PDF) |
| Visual | `03-visuals/<konzept>/k1…k3.png` + `PROMPTS.md` | `01-konzepte.md` oder `01-brief.md`, `brand/assets/products/`, `brand/PACKAGING.md` |
| Jury | `03b-jury.md` + `03b-kontaktbogen.png` | `03-visuals/`, Referenz-Bilder |
| Leitung | `uebergabe/<konzept>/bild-01…03.png` + `README.md` · `06-kosten.md` | `03b-jury.md` |

## Die fünf Agenten

| Agent | Auftrag in einem Satz | Skill |
|---|---|---|
| **KONZEPT** | Findet je Run 5 Design-Referenzen (Markt mit Reach-Beleg oder Art-Director-Auswahl), bindet jede an ein Produkt, einen Angle und den Text im Bild. | `agents/konzept/SKILL.md` |
| **VISUAL** | Setzt das Konzept mit dem echten Produkt und dem Text um: Layout-Muster der Referenz, Text im Modell, Etikett wahr. | `agents/visual/SKILL.md` |
| **JURY** | Legt Referenz neben Ergebnis, prüft Blocker, urteilt in einer Sekunde, wählt die besten 3. Generiert nie. | `agents/jury/SKILL.md` |
| **BRIEF-INTAKE** | Übersetzt einen Brief (Datei, Task, PDF) in `01-brief.md`, konsolidiert Feedback in Run ≥ 2. | `agents/brief-intake/SKILL.md` |
| **LEARNINGS** | Liest das Werbekonto wöchentlich: welche Statics laufen, was gewinnt; ergänzt REFERENZ-ADS mit eigenen Winnern. | `agents/learnings/SKILL.md` |

Die Session-Leitung (das stärkste Modell, nicht als Subagent) übernimmt alles, was kein
eigener Agent ist: Übergabe-Ordner, Kontaktbogen, Kosten, optionales Board, Preis-Check
gegen die Live-Seite bei Offer-Konzepten.

## Nicht-Ziele

Keine Ad-Copy (Headline, Primary Text — das macht der Copywriter). Kein automatisches
Schalten. Keine Wissens-Sammlung um ihrer selbst willen. Keine neuen Agenten ohne
Bild-Beleg, dass ein Schritt fehlt.

## Warum so schlank

Eine frühere Fassung dieser Engine hatte 14 Agenten, 64 Checklisten-Punkte und
Audit-Protokolle. Sie optimierte Nachvollziehbarkeit, nicht Bildqualität. Die Lehre: Mit
«Referenz + echtes Produkt + Text im Bild» sind Bild-Regie, Copy-Agent und Assembly
trivial oder Sache der Leitung. Was bleibt, sind die drei Schritte, die ein Bild wirklich
besser machen: eine gute Referenz wählen, sie sauber umsetzen, mit frischen Augen prüfen.
