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
Repräsentanten auf, Die Gesamtmenge der Punkte ist dann eine Ebene, und die
ist unabhängig von der Wahl der Repräsentaten. Diese Menge von Klassen ist im
projektiven Raum die Gerade durch zwei Punkte.

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

Erst mal ein paar prototypische Beispiele. Genauer gesagt sind dies
elliptische Kurven in der affinen rellen Ebene. Drei Beispiele mit Formeln und
Bild dazu, einmal fischartig, einmal Insel und Hügel, einmal nur Hügel und
einmal Hügel mit Hochebene, am Schluss sich selbst kreuzende Kurve (keine
elliptische Kurve)

Was haben die mit (mathematischen) Ellipsen zu tun?

- Die Berechnung der Bogenlänge einer Ellipse, genauer: Das Problem aus dem
  Winkel die Länge des Bogens bis dorthin zu berechnen, führt auf Integrale
  die sich nicht in geschlossener Form lösen lassen. Besonders frustrierend,
  da das ganze beim Kreis so gut funktioniert, und die Verallgemeinerung von
  Kreis auf Ellipse bei der Flächenberechnung kein Problem darstellt.
- Die Umkehrfunktion davon kann man in die komplexen Zahlen hinein
  fortsetzen. Nennt man elliptische Funktionen.
- Mit so einer Funktion und ihrer Ableitung kann man eine 1-1 Abbildung
  von den Punkten einer elliptischen Kurve auf ein Parallelogramm der
  komplexen Ebene konstruieren.
- ... also eher entfernte Verwandschaft.


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

  $$ y^2 = x^3 + ax + b     (2)


zu betrachten, wobei:

  $$ \Delta_E = -4a^3 - 27b^2 != 0 $$

Dies wird die `Weierstraßsche Normalform` genannt.

Die letzte Bedingung brauchen wir, um solche Sachen auszuschließen, die wir im
letzten Beispiel gesehen haben.

Footnote:

Stimmt für die reellen Zahlen, die wir gerade betrachten. Nur für Körper mit
Charakteristik 2 oder 3 muss man etwas mehr Koeffizienten auf der rechten
Seite hinzunehmen.


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

- Fun fact negative Zahlen: Diophant kannte bereits negative Zahlen,
  und wusste wie man mit ihnen rechnen musste, hat sie aber nur als
  Hilfsgrößen die bei Zwischenrechnungen auftreten betrachtet und
  nicht als Lösungen von Gleichungen akzeptiert. Bis
  ins 18. Jahrhundert waren Mathematikern negative Zahlen
  suspekt. Zitat Francis Maseres, 1758: "[negative numbers] darken the
  very whole doctrines of the equations and make dark of things which
  are in their nature excessively obvious and simple.
  Erst im 19. Jahrhundert durch Mathematike wie Hamilton und Gauß
  etablierten sich negative Zahlen wie wir sie heute kennen.


Nehmen wir einfach mal an, wir haben eine elliptische Kurve, gegeben in der
Weierstraßschen Normalform und mit rationalen
Koeffizenten. Nehmen wir weiter an, wir kennen schon zwei Punkte (x_1, y_1)
und (x_2, y_2) auf
der Kurve. Dann können wir eine Gerade durch diese legen und bekommen häufig
einen dritten Schnittpunkt.

Bemerkung 1: Wir bekommen auf keinen Fall einen vierten Schnittpunkt, das
liegt daran, dass wir uns auf Kurve vom Grad 3 beschränkt haben. Warum
können Polynome vom Grad n höchstens n Nullstellen besitzen? Übungsaufgabe:

Tip: Polynomdivision, Nullstelle ist linearer Teiler.

Antwort: Polynomdivision, spalte bei Nullstelle x_0 (x - x_0) ab, dass
geht genau wenn x_0 Nullstelle. Bei n Nullstellen komplett zerlegt,
weitere Nullstelle->Widerspruch.
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
  y_r = - y_p + s (x_p - x_r)


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

Image ec5-m1-p1-points.png [TODO: Start with P,Q, add line and 3rd
intersection, then arrow to sum. Now add R to the box and remove the line and
the arrow. Repeat until end, Finally make an animated png from it.]


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

Was haben wir bis jetzt?

- Eine Kurve, genauer eine Menge von Punkten (x, y), die Gleichung in
  Weierstraß-Form erfüllen.
- Eine Operation \oplus auf der Kurve, also eine Formel, die aus zwei Punkten
  P_1 = (x_1, y_1), und P_2 = (x_2, y_2) einen dritten Punkt
  P_3 = (x_3, y_3) = P_1 \oplus P_2 macht.


Endliche Körper
===============

Jetzt möchten wir aber konkrete Berechnungen vornehmen und zwar auf Computern,
die nicht beliebig genau rechnen können. Am besten wäre, wenn wir auf
endlichen Mengen rechnen könnten, da gibt es mit der Genauigkeit keine
Probleme. Wenn wir uns unsere bisherigen Formeln ansehen, stellen wir fest,
das wir eigentlich nur Addition, Subtraktion, Multiplikation und Division
verwendet haben, und davon ausgegangen sind, dass die üblichen Rechengesetze
gelten. Eine solches Objekt nennen Mathematiker `Körper` (engl. `field`).

Na toll, sowas gibt es doch gar nicht! Oder ...? Doch, die gibt es, und sie
sind allen fast schon aus der Grundschule bekannt, wo jeder schon mal Division
mit Rest gemacht hat. Wir setzen eine beliebige Zahl N fest, und teilen dann
alle ganzen Zahlen in Äquivalenzklassen ein: zwei ganze Zahlen a und b gelten
als äquivalent, wenn sie beim Teilen durch N denselben Rest ergeben. Oder
anders gesagt: wenn $ (a - b) = m N$ 

Offenbar gibt es dann nur endlich viele Äquivalenzklassen, denn wir können die
Zahlen 0..N-1 als Repräsentanten nehmen. Man kann sich leicht überlegen, dass
Addition, Subtraktion und Multiplikation einfach durch die normale Operation
auf den Repräsentanten durchgeführt werden können, und wohldefiniert sind. Nur
bei der Division gibt es ein Problem: Wenn N sich zerlegen lässt:
$N = n_1 \dot n_2$ und weder n_1 noch n_2 sind 1 oder N, dann hätten wir
$n_1 n_2 = 0$ 

N darf sich also nicht zerlegen lassen, mit anderen Worten, N muss eine
Primzahl sein. Und für diese funktionert es auch tatsächlich. Wir legen also
eine Primzahl p fest, und rechnen einfach normal mit den Zahlen 0..p-1, und
sobald wir aus dem Bereich 0..p-1 herauskommen reduzieren wir wieder wieder,
indem wir mit Rest durch p teilen. Nur: wie geht die Division?

Nehmen wir ein Beispiel: p=37, und wir wollen $9 \div 10$ berechnen, oder
anders gesagt, wird suchen die Zahl x, so dass x * 10 = 9 (mod 37). 
Es würde schon ausreichen eine Zahl x zu finden mit x * 10 = 1 (mod 37), denn
dann können wir x einfach mit 9 multiplizieren (und ggf. mod 37 reduzieren),
oder noch mal anders formuliert: Wir suchen eine Zahl r, so dass es eine ganze
Zahl s gibt mit r * 10 = s * 37 + 1 bzw. 1 = 10 r - 37 s

Wir teilen dazu unser festgelegte Primzahl 37 mit Rest durch die Zahl deren
Inverses wir berechnen wollen, also 10:

  $$ 37 = 3 * 10 + 7     7 = 37 - 3 * 10 $$

Der bleibende Rest ist 7. Nun dasselbe Verfahren mit 10 und 7:

  $$ 10 = 1 * 7 + 3     3 = 10 - 1 * 7 $$

7 mit Rest durch 3:

  $$ 7 = 2 * 3 + 1    1 = 7 - 2 * 3 $$

Wir sehen: die Zahlen werden immer kleiner, in der Tat kann man beweisen
(Übungsaufgabe) dass sie sich bei jedem Schritt in etwa halbieren. (Stimmt
auch nicht ganz: wir müssem um effizienter zu werden mit Resten im Bereich
[-(p-1)/2 .. (p-1)/2] rechnen.) Irgenwann kommen wir mal zu einer Division die
Rest 1 liefert.

In der letzten Zeile sehen wir die 1 als Summe von Produkten von 7 und 3.
Mit der vorletzten Zeile können wir die 3 als Summe von Produkten von 7 und 10
schreiben, damit bekommen wir die 1 als Summe von Produkten von 7 und 10.
Die 7 wiederum können wir mit der obersten Zeile als Summe von Produkten aus
37 und 10 ausdrücken und erhalten so am Schluss 1 als Summe von Produkten 10
und 37:

$$ 1 = 1 * 7 - 2 * 3 = 1 * 7 - 2 * (10 - 1 * 7) =
     = 3 * 7 - 2 * 10 = 3 * (37 - 3 * 10) - 2 * 10 =
     = 3 * 37 - 11 * 10 $$

Jetzt haben wir noch ein kleines Vorzeichenproblem schließlich wollten wir
(s.o.) bei der 10 einen positiven Faktor. Das haben wir aber gleich:


         -11 * 10 + 3 * 37 =
       = (26 - 37) * 10 + 3 * 37 =
       = 26 * 10 - 7 * 37

Und erhalten damit 26 als Inverses von 10 (mod 37).

Über endlichen Körpern sehen unsere elliptischen Kurven nun wenig intuitiv
aus. Beispiel: [finplot.png]

Praktisch werden in standardisierten Verfahren im Wesentlichen vier Kurven
benutzt, jeweils mit verschiedenen endlichen Köpern. Die Primzahlen haben
dabei 76, 117 und 156 Dezimalstellen.

Funktioniert der Übergang zu endlichen Körpern nun überhaupt? Will heißen:
Gibt es überhaupt genügend Punkte auf diesen Kurven? Die Antwort hat Helmut
Hasse (* 25.8.1898  + 26.12.1979) 1933 gegeben:

Satz (Hasse-Schranke): Sei E eine elliptische Kurve über \F_q Sein N die
Anzahl der Punkte auf E. Dann ist

$$ \| N - q - 1 \| \le 2 \sqrt{q} $$

Die Anzahl von Punkten überhaupt ist $2q + 1$, da \F_q q Elemente hat (Das + 1
ist für den Punkt im Unendlichen).
Für große q (und solche interessieren uns ja für die Kryptographie) ist die
Wurzel im Vergleich zu q eher klein, und damit besagt der Satz, das etwa die
Hälfte der Punkte des gesamten Raumes auf der Kurve liegt.

EC Diffie-Hellman
=================


Erste Anmerkung: Diffie-Hellman ist kein Verschlüsselungsverfahren,
und auch kein Signaturverfahren, sondern es erlaubt es zwei Leuten
Alice und Bob über einen öffentlichen Kanal mit Lauscher E sich auf
ein gemeinsames Geheimnis zu einigen, das E nicht herausbekommen kann.

Eine Möglichkeit, so ein gemeinsames Geheimnis zu nutzen wäre zum
Beispiel es als Key für ein konventionellles symmetrisches
Verschlüsselungsverfahen zu nutzen (AES).

Zurück zu EC-Diffie-Hellmann:

Vorher haben A und B eine elliptische Kurve E zusammen mit einem
endlichen Körper K festgelegt, und zusätzlich noch einen Punkt P. P
ist dabei so gewählt, dass die Sequenz P, P+P, P+P+P ... `lange`
braucht um sich zu wiederholen. (Anmerkung: Wir wollen zusätzlich, dass die
Anzahl der Additionen bis sich das Ergebnis wiederholt eine Primzahl ist.) Mit
lang meinen wir eine Zahl die in etwa so viele Stellen wie die Primzahl
unseres endlichen Körpers. Diese Informationen sind öffentlich
und insbesondere auch E bekannt.

Alice wählt nun ihr Geheims n_a, eine lange Dezimalzahl. Sie berechnet
daraus P + ... + P, n_a - mal.

(Aufmerksame Leute werden sich fragen wie das mit so großen Zahlen
gehen soll. Antwort: Wiederholtes Verdoppeln und Addieren statt immer wieder
eins drauf zu addieren)

Dann übermittelt Alice das Ergebnis P_a - ein Punkt auf der Kurve - an
Bob.

Bob macht auf seiner Seite währenddessen dasselbe, er wählt sein
eigenes Geheimnis n_b, und berechnet P + ... + P, n_b mal. Dann
übermittelt er das Ergebnis P_b an Alice.

[TODO: Image, A -> B, over arrow is P_a = P + ...^{n-times} + P ]

Nun kennt Alice n_a und P_b, Bob dagegen kennt n_b und P_a.

Alice berechnet nun P_b + ... + P_b (n_a mal) und erhält S (ein
Punkt auf der Kurve).

Bob berechnet P_a + ... + P_a (n_b mal) und erhält S'

Aber nun ist

       S = P_b + ... + P_b =
           (P + ...^n_b + P) + ...^n_a + (P + ... +P)
         = P + ...^ n_a n_b P =
	 = P + ...^ n_b n_a P =
	 = P + ...^n_a P + ...^n_b
	 = P_a + ...^n_b + P_a =
	 = S'

Damit sind S und S' derselbe Punkt und somit ein gemeinsames
Geheimnis. Eve dagegen kennt nur P_a und P_b, bekommt damit aber weder
n_a noch n_b heraus. (Außer sie hat einen funktionierenden
Quantencomputer, aber das ist eine andere Geschichte).

Was hatten wir:

- Ein paar Kurven so in Fisch oder Knubbelform
- Eine geometrische Operation \oplus darauf, die aus zwei Punkten einen
  dritten macht
- Ein Ausflug in die dritte Dimension, der zu den Kurven einen
  schwurbelfreien Punkt im Unendlichen hinzufügt. Nun ist \oplus eine
  Addition
- Ein Ausflug in endliche Körper, danach kann ein Computer mit den
  Kurven rechnen, und zwar ohne zu ungenau zu werden oder zuviel
  Speicher zu brauchen.
- Eine Methode wie man sich mit diesen Punkten auf der Kurve auf ein
  gemeinsames Geheimnis einigt das kein anderer kennt.

