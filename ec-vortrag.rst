============================
 Vortrag Elliptische Kurven
============================

Konzept 1
=========
Vorstellung des generellen mathematischen Konzeptes neue Objekte zu bilden
indem schon vorhandene in Äquivalenzklassen aufgeteilt werden:

1) Punkte im 3-dimensionaln Raum ohne Nullpunkt. Alle Punkte die auf derselben
   Geraden durch den Ursprung liegen sind äquivalent zueinander.

2) Ganze Zahlen, und eine Primzahl p gegeben. Alle Zahlen, die denselben Rest
   beim Teilen durch p besitzen sind äquivalent.

Können beidesmal eine Untermenge wählen die die Repräsentanten für die Klassen
bilden:

1) Punkte {(x, y, 1) x, y \in \R} {(x, 1, 0), x \in \R}, {(1, 0, 0)}
2) Zahlen 0 ... (p-1)

Dann kann man die in der Gesamtmenge definierten Operationen auf die neuen
Objekte übertragen, indem man sie auf den Repräsentanten wie gewohnt
durchführt, und dann als Ergebnis die Äquivalenzklasse nimmt, in der das
Ergebnis liegt.

Beispiele: In 1) Gerade durch zwei Punkte, nimm zwei beliebige Repräsentanten,
zeichne eine Gerade durch beide, fasse alle Punkte auf der Geraden als
Repräsentanten auf, diese Menge von Klassen ist im projektiven Raum die Gerade
durch zwei Punkte.

In 2) nimm zwei beliebige Repräsentanten, bilde die Summe, definiere das
Ergebnis als die Summe der Äquivalenzklassen. Dasselbe mit dem Produkt:

    2 + 6 = 8 = 1 (mod 7)
    2 * 6 = 12 = 5 (mod 7)


Die neuen Objekte können auch ganz neue Eigenschaften haben - das macht sie ja
gerade so interessant:

1) Geraden werden in der projektiven Ebene zu Großkreisen auf der
   Kugeloberfläche. Damit
   schneiden sich zwei Geraden genau in zwei Punkten, die liegen aber genau
   gegenüber (Antipoden) sind also äquivalent. Mit anderen Worten: Zwei
   Geraden in der projektiven Ebene schneiden sich genau in einem
   Punkt (nicht-euklidische Geometrie).
2) Modulo 13 gilt:

   5 * 5 = 25 = 12 = -1 (mod 13)

   Es gibt also in den Zahlen mod 13 eine `Wurzel aus -1`

Aber Vorsicht: Wir müssen darauf achten, dass das Endergebnis `wohldefiniert`
ist: Wenn man zwei andere Repräsentanten nimmt mus dasselbe herauskommen,
wobei dasselbe heißt: die beiden verschiedenen Ergebnisse liegen in derselben
Klasse. Bei Multiplikation und Addition funktioniert das. Beim Wurzelziehen
beispielsweise geht es schief:

   sqrt(9) = 3
   sqrt(16) = 4

aber 9 (mod 7) == 2 (mod 7) == 16 (mod 7), wohingegen 3 != 4 (mod 7)


Konzept 2
=========
Zwischen geometrischer Anschauung (Geraden, Kurven, Schnittpunkte) und den
zugehörigen arithmetischen Eigenschaften immer wieder hin- und herwechseln.


Verlauf des Vortrages:

- Was sind sie, wie sehen sie anschaulich aus?
- Addition geometrisch gesehen -> Formeln
- Übergang zur projektiven Ebene
- Um mit Computern zu rechnen ohne Rundungsfehler -> Restklassen
- Wie zur Kryptographie nutzen (Diffie-Hellmann für elliptische Kurven)

- Fun fact: Ursprünglich erforscht um RSA zu attackieren
- Fun fact: Elliptische Kurven können als zweidimensionale
  Verallgemeinerung zum eindimensionalen Kreis angesehen werden.

[Nachsehen: Wer waren Diffie und Hellman? -> Fußnote]

Vorweg: Was haben die mit (mathematischen) Ellipsen zu tun?

Das braucht zuviel Mathematik, und führt zu weit vom Thema aber für
die, die es wissen wollen:

Die Berechnung der Bogenlänge einer Ellipse

[Bild Ellipse mit Teil des Bogens]

ergibt Integrale die sich nicht in geschlossener Form lösen
lassen. Die Umkehrfunktionen davon nennt man elliptische Funktionen.
Die kann man ins Komplexe fortsetzen und mit denen erhält man eine
1-1 Abbildung einer elliptischen Kurve über den komplexen Zahlen auf
ein Parallelogramm in der komplexen Ebene. Also eher die entferntere
Verwandschaft...


Erst mal ein paar prototypische Beispiele. Genauer gesagt sind dies
elliptische Kurven in der affinen rellen Ebene. Drei Beispiele mit Formeln und
Bild dazu, einmal durchgehend mit Beule, einmal fischartig, einmal als zwei
getrennte Teile.

Allgemeine Form: Polynom in x,y vom Grad 3. Heißt:

$$ a y^3 + b y^2 x + c y x^2 + d x^3 + e y^2 + f x y + g x^2 + $$
$$ + h x + i y + j = 0   (1) $$

Das sind 10 verschiedene Parameter, ziemlich viele, sehr
unübersichtlich. Wir wollen eigentlich zwei Kurven die durch Drehung
ineinander übergehen nicht wirklich als unterschiedlich betrachten. Auch etwas
schräg ansehen oder Stauchen und Strecken soll als `dieselbe` Kurve betrachtet
werden. Arithmetisch gesehen heißt das: Es gibt eine Abbildung

   x, y -> f(x, y), g(x, y)

die jeden Punkt (x, y) auf der einen Kurve in einen Punkt (x', y') auf der
anderen Kurve umrechnet, und umgekehrt. Damit lässt sich (kompliziert, braucht
viel Mathematik) zeigen:

Es reicht Kurven der Form:

  $$ y^2 = x^3 + ax + b     (2) $$


zu betrachten. Dies wird die `Weierstraßsche Normalform` genannt.
Zusatzbedingung [TODO] um solche Sachen auszuschließen
(Bild mit sich selbst schneidender Kurve).

Der aufmerksame Zuhörerin wird sich fragen, warum die Koeffizenten der
Beispiele eigentlich alles ganze Zahlen sind, wenn hier doch ständig von
reellen Zahlen die Rede ist. Mit rationalen Zahlen (vulgo: Brüche ganzer
Zahlen) kann man alle reellen Zahlen genügend genau annähern.
Beliebige relle Zahlen hingegen bestehen aus unendlich vielen unregelmäßigen
Nachkommastellen, mit denen kann man nur ungefähr rechnen, es gibt immer
Rundungsfehler. Wir wollen - kommt gleich - aber eine einzige Operation immer
wieder wiederholen und zwar so richtig oft, da müssen wir ohne sich
akkumulierende Rundungsfehler auskommen, also rechnen wir mit Brüchen ganzer
Zahlen. Die haben das nächste Problem, die werden potentiell - und auch in der
Praxis immer länger, und unendlich viel Speicherplatz und Rechenkapazität
haben wir leider nicht zur Verfügung. Lösung kommt später.

Vorerst mal bleiben wir bei rationalen Zahlen.

- Fun fact: Die Griechen oder genauer Diophant von Alexandria, betrachtete
  überhaupt nur Zahlen, die sich als ganzzahlige Verhältnisse darstellen
  lassen, also in heutiger Sprache: rationale Zahlen. Er kam dabei auf die
  ersten Probleme die sich in der heutigen mathematischen Sprache formuliert
  damit befassten Punkte auf elliptischen Kurven zu finden, bei denen beide
  Koordinaten rational sind.

Nehmen wir einfach mal an, wir haben eine elliptische Kurve, gegeben in der
Weierstraßschen Normalform und mit rationalen
Koeffizenten. Nehmen wir weiter an, wir kennen schon zwei Punkte (x_1, y_1)
und (x_2, y_2) auf
der Kurve. Dann können wir eine Gerade durch diese legen und bekommen häufig
einen dritten Schnittpunkt.

Bemerkung 1: Wir bekommen auf keinen Fall einen vierten Schnittpunkt, das
liegt daran, dass wir uns auf Kurve vom Grad 3 beschränkt haben.

Der Beweise dafür nutzt die Tatsache dass alle x-Werte der Schnittpunkte einer
Geraden mit der Kurve eine Gleichung dritten Gerades erfüllen, und man für
jede Lösung x_0 einen Linearfaktor aus der Gleichung herausziehen kann.

Bemerkung 2: Der dritte Schnittpunkt hat ebenfalls rationale Koordinaten.

Der Beweis benutzt wieder die in Bemerkung 1 erwähnte Zerlegung der Gleichung
für die x-Koordinaten in Linearfaktoren:

   x^3 + a x^2 + b x + d = (x - x_1) (x - x_2) (x - x_3) =

Ausmultiplizieren der rechten Seite gibt für den Koeffizenten a bei x^2:

  a = - (x_1 + x_2 + x_3)

Sowohl x1, x2 und a sind nach unseren Annahmen rational, dann muss es auch x_3
sein. y_3 liegt auf der Geraden, ist also von der Form y = mx + g mit m und g
beides rational, ist also ebenfalls rational.

Damit ist etwas interessantes passiert: Wir haben aus zwei rationalen Punkten
einen dritten konstruiert: Wir können sogar eine Formel für den dritten Punkt
angeben:

Seien P=(x_p, y_p) und Q=(x_q, y_q), P + Q = R = (x_r, y_r), wobei 

sei s := (y_p - y_q) / (x_p - x_q)

Dann ist:

  x_r = s^2 - x_p - x_q
  y_r = - y_p + s (x_p - x_r


Und es kommt noch besser: Nicht nur dass wir einen dritten Punkt gefunden
haben, wir haben falls y_3 != 0 sogar noch einen vierten Punkt, nämlich den
Punkt (x_4, y_4) = (x_3, -y_3) schließlich ist die Kurve in Weierstraß-Normalform
spiegelsymmetrisch zur x-Achse. Und mit diesem vierten Punkt können wir
dieselbe Konstruktion fortsetzen: Gerade durch (x_1, y_1) und (x_4, y_4)
legen, wir erhalten einen dritten Schnittpunkt, (x_5, y_5), spiegeln ihn an
der x-Achse und erhalten (x_6, y_6), und so weiter.

Example: Kurve $y^2 = x^3 - x + 1$

Anfangs sind P = (1,1) und Q = (-1, 1) (eigentlich == 2P), dann kommen die
Punkte nP + Q (0, -1), (3, -5), (5, 11), (1/4, 7/8), (-11/9, 34/54)
[TODO: Bild]


Damit haben wir eine Operation \x, die aus Punkt P = (x_1, y_1) und Q = (x_2,
y_2) den Punkt P \mult Q = (x_4, y_4) macht. Warum haben wir den Punkt (x_3,
y_3) dabei unter den Tisch fallen lassen? Weil wir die gleiche Operation immer wieder
anwenden wollen, dabei aber nicht immer bei den drei Anfangspunkten bleiben
wollen.

Es stellt sich heraus, dass die Operation \x folgende Eigenschaften hat
(Großbuchstaben bezeichnen in den folgenden Formeln Punkte auf der Kurve, also
Koordinatenpaare (x, y):

  P \x Q = Q \x P                (1)

  (P \x Q) \x R = P \x (Q \x R)   (2)

Das ist den Eigenschaften der Addition schon sehr ähnlich, es fehlen eigentlich
nur noch folgende:

Es gibt einen Punkt O mit der Eigenschaft:

  P \x O = P

für alle P, und für alle P gibt es einen Punkt P', so dass:

  P \x P' = O

Dieser neutrale Punkt ist der von dem es bei vielen Beschreibungen einfach
heißt, er liege `im Unendlichen`. Wir wollen das aber präzise fassen, und dazu
machen wir etwas, was auch sonst nützlich ist: Wir treten aus der Ebene heraus
und sehen uns die Kurve etwas aus der Entfernung an. Zunächst mal geometrisch
anschaulich gesehen: Wir fassen die Kurve als ein Gebilde auf, das sich eigentlich
auf einer Kugel befindet. In der Mitte der Kugel ist eine punktförmige
Lichtquelle. Die Leinwand ist eine Ebene oberhalb der Kugel, das auf die
Leinwand projizierte Bild ist die Kurve, wie wir sie kennen.

Mathematisch heißt das: Wir nehmen statt zwei Koordinaten x und y nun drei: x,
y, z, sagen aber dafür, dass Punkte, die auf demselben Strahl liegen alle
äquivalent sind, also (x, y, z) ~ (x', y', z') wenn es eine Konstante \lambda
aus \R gibt mit (x', y', z') = (\lambda x, \lambda y, \lambda z)

Statt Punkte betrachten wir nun Äquivalenzklassen von Punkten. Die
Kurvengleichung

$$ y^2 = x^3 + ax + b $$

wird zu:

$$ y^2 z = x^3 + ax z^2 + b z^3 $$

Wenn z != 0 ist, können wir beide Seiten durch z^3 teilen und erhalten:

$$ \frac{y^2}{z^2} = \frac{x^3}{z^3} + a \frac{x}{z} + b $$

das entspricht genau dem Punkt $(\frac{x}{z}, \frac{y}{z}$. Wenn dagegen
$z = 0$, dann wird die Gleichung zu $0 = x^3$, also muss auch $x = 0$, und da
mindestens eine der drei Koordinaten != 0 sein muss, muss $y != 0$, und da es
bis auf einen Faktor egal ist können wir y = 1 wählen, somit ist der Punkt (0,
1, 0) der Punkt auf der Kurve im `Unendlichen`. image: ell-curve-projective.png
