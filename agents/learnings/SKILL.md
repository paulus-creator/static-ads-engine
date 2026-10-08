# LEARNINGS — was im Konto gewinnt (wöchentlich, ausserhalb der Runs)

Rein lesend über die Meta Marketing API (`.env`: `META_ACCESS_TOKEN`,
`META_AD_ACCOUNT_ID`, `META_API_VERSION`), `level=ad`, Fenster `last_7d` und `last_28d`,
Kennzahlen nach Ad-Name aufsummiert (Meta liefert je Ad-Set eine Zeile). Ohne Token:
Export aus dem Ads Manager als CSV in `workspace/learnings/` ablegen und von dort lesen.

## Drei Fragen

1. **Welche Statics laufen, mit welchem Ergebnis?** Tabelle: Ad-Name · Spend · ROAS · CPA ·
   CTR · Käufe; Engine-Statics (Dateinamen aus `workspace/*/uebergabe/`) markieren.
   Belastbarkeits-Schwelle aus `brand/BRAND.md` (Default: ab 1'000 Spend und 25 Käufen in
   28 Tagen), darunter «Tendenz».
2. **Was gewinnt, und wie sieht es aus?** Zu jedem belastbaren Static-Winner das Bild
   holen (`workspace/` oder Meta-Creative) und in `brand/REFERENZ-ADS.md` Teil C
   eintragen: Pfad, Kennzahlen, drei Zeilen Layout-Muster. Eigene Winner sind die beste
   Referenz für den nächsten Run (Iteration: gleiches Layout, neuer Hook oder neues
   Produkt; Leiter in `knowledge/frameworks/testing-und-iteration.md`).
3. **Was ist nie live gegangen?** Liste der Übergabe-Pakete ohne Zeile im Konto → an den
   Owner, nicht an die Engine.

## Output

`workspace/learnings/LEARNINGS.md` — Eintrag oben anfügen (Datum per `date`, die drei
Antworten, je ≤ 15 Zeilen). Archiv-Prinzip: nichts löschen. Keine Kampagnen anfassen.
