# Wichtige Zeichen

- Hochgestellte Zeichen: n^2 = n hoch 2
    - Wird in Markdown mit sup-Tag erstellt: n<sup>2</sup>
- Tiefgestellte Zeichen: n_0 = n null
    - Wird in Markdown mit Sub-Tag erstellt: n<sub>2</sub>
- Element von: $\in$
    - Wird in Markdown mit Inline-Math erstellt: $ \in $
- Kleiner als, grösser als, etc.
    - $<$
    - $>$
    - $\le$
    - $\ge$
- $\subseteq$: Teilmenge. M$\subseteq$N Die Menge M enthält die gleichen Elemente wie die Menge N
- Reelle Zahlen: Alle Zahlen, die auf der Zahlengeraden dargestellt werden können --> Sie umfasst sowohl ratonale Zhalen als auch irrationale Zahlen.

# Was ist log?

Das log steht für Logarithmus und wird jeweils zu einer Basis angegeben. Also log<sub>2</sub> bedeutet Logarithmus zur
Basis 2.
Der Logarithmus gibt an, wie oft man etwas halbieren kann, bis man bei 1 ankommt.

- log<sub>2</sub>8 = 3, denn: 8->4->2->1 --> 3 Schritte
- log<sub>2</sub>16 = 4, denn: 16->4->2->1 --> 4 Schritte

# P und NP

P (Polynomialzeit): Das sind Probleme, die schnell gelöst werden können, also mit einem normalen Algorithmus, der in
polynomieller Zeit läuft. Zum Beispiel n<sup>2</sup>, nlogn, usw. Beispiele: Sortieren von Zahlen - Computer können das
effizient erledigen.

NP (Nichtdeterministische Polynomialzeit): Das sind Probleme, die nicht unbedingt schnell lösbar, aber schnell
überprüfbar sind.
Du könntest dir vorstellen: Wenn jemand eine Lösung präsentiert, kann man schnell prüfen, ob sie korrekt ist.
Beispiel: Ein schwieriges Rätsel - schwer zu lösen, aber leicht zu prüfen, ob die Lösung passt.

P $\subseteq$ NP bedeutet somit, dass jeder Algorithmuss der schnell läuft (P) auch zur Klasse NP gehört.
Denn: Was man schnell berechnen kann, kann man natürlich auch schnell überprüfen.

P ≠ NP: Die grosse Frage der Informatik: Gibt es Probleme, die zwar leicht zu prüfen, aber unmöglich schnell zu lösen
sind?
Das weiss niemand genau! Die meisten Fachleute vermuten, dass es Probleme gibt, die kein Computer effizient lösen kann,
selbst in ferner Zukunft.

# Nichtdeterministisch

Stell dir einen magischen Computer vor, der bei jeder Entscheidung automatisch den besten Weg wählt.
In der echten Welt geht das nicht - aber in der Theorie kann man sich so eine nichtdeterministische Maschine vorstellen.
Man sagt: "Wenn es irgendeinen Weg zur Lösung gibt, findet sie ihn sofort."