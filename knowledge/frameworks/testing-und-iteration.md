# Testing und Iteration — übergeordnete Prinzipien

Die operative Test-Durchführung (Budgets, Kill-Regeln, Ads Manager) liegt beim
Media-Buyer. Diese Datei steuert, wie die Engine produziert und aus Ergebnissen lernt.

## 1. Ein Test ist eine Frage
Schlecht: «Wir testen 6 Statics.» Gut: «Wir testen, ob der Root-Cause-Angle mehr
qualifizierte Käufe erzeugt als der Convenience-Angle.» Jeder Run sollte eine benennbare
Frage beantworten; KONZEPT formuliert sie in der «Lage in 3 Sätzen».

## 2. Concepts statt Klone
Standard: **5 strategisch verschiedene Angles × je eine Layout-Familie = 5 echte
Concepts.** Zehn fast identische Varianten sind ein Concept, nicht zehn. Innerhalb eines
Concepts sind die drei Kandidaten Neu-Renders derselben Umsetzung, keine Varianten.

## 3. CTR ist ein Diagnosewert, kein Geschäftsmodell
Drei Mess-Ebenen: (1) Auction/Attention (CPM, Outbound CTR, Cost per Click, LPV) →
(2) Message Match/Intent (Klick→LPV, Product Views, ATC, Checkout) → (3) Business
Outcome (CPA, Neukunden-CPA, ROAS, Stabilität über Tage). Bewertet wird auf Ebene 3.

## 4. Diagnose vor Neuproduktion

| Beobachtung | Wahrscheinliche Ursache | Nächster Schritt |
|---|---|---|
| Hoher CPM, schwache CTR | Bild/Hook/zu enger Appeal | neue Layout-Familie + Hook |
| Gute CTR, wenige LPVs | Ladezeit, falscher Klickreiz | Speed/Link/Erwartung prüfen |
| Gute LPVs, schwache ATCs | Message Match, Argument, Offer | Seite + Produkt-Transition |
| Gute ATCs, schwache Käufe | Preis, Trust, Checkout | Offer-/Checkout-Diagnose |
| Gute Conversion, wenig Spend | zu enger Angle | Angle verbreitern, neue Bilder |
| Viele Klicks, kaum Käufe | Curiosity ohne Buying Intent | Hook näher an Problem + Produkt |

## 5. Iteration vor dem Launch ist normal
Einzelne Statics durchlaufen mehrere Versionen, bis sie sitzen. Feedback des Art
Directors fliesst in die nächste Fassung. Das ist kein Scheitern, sondern Teil des
Prozesses (RUNBOOK: Feedback-Runde).

## 6. Ein Winner ist Research, kein Endpunkt
Nach jedem Winner zuerst identifizieren, **was** vermutlich gewonnen hat (Bild, Hook,
Mechanismus, Proof, Destination, Offer), dann kontrolliert iterieren:

**Iteration Ladder:** 1. Winner-Layout × 3 neue Hooks → 2. Winner-Hook × 3 neue Layouts
→ 3. Winner-Mechanismus in anderer Story → 4. Winner-Argument in anderer Grammatik →
5. Winner-Angle für benachbarte Awareness-Stufe → 6. Winner mit neuem Proof/Offer.

**Format-Regel: ein Format im Test, zwei beim Winner.** Test-Phase: 4:5. Winner bekommen
das 9:16-Derivat (neu layoutet, nicht gecroppt).

LEARNINGS trägt eigene Winner in `brand/REFERENZ-ADS.md` Teil C ein; KONZEPT nimmt sie
im nächsten Run als Referenz für die Leiter.
