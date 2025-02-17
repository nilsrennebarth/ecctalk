============================
 Vortrag Elliptische Kurven
============================




Verlauf des Vortrages:

- Was sind sie, wie sehen sie anschaulich aus?
- Addition geometrisch gesehen -> Formeln
- Übergang zur projektiven Ebene
- Um mit Computern zu rechnen ohne Rundungsfehler -> Restklassen
- Wie zur Kryptographie nutzen (Diffie-Hellmann für elliptische Kurven)

- Fun fact: Ursprünglich erforscht um RSA zu attackieren
- Fun fact: Elliptische Kurven können als zweidimensionale
  Verallgemeinerung zum eindimensionalen Kreis angesehen werden.


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


Kurven von Grad 2 sind alle bekannt und vollständig beschrieben
(Kegelschnitte). Das nächstkompliziertere wären Kurven vom Grad 3.
Allgemeine Form: Polynom in x,y vom Grad 3, also:

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
  Erst im 19. Jahrhundert durch Mathematiker wie Hamilton und Gauß
  etablierten sich negative Zahlen wie wir sie heute kennen.


Nehmen wir einfach mal an, wir haben eine elliptische Kurve, gegeben in der
Weierstraßschen Normalform und mit rationalen Koeffizenten. Nehmen wir weiter
an, wir kennen schon zwei Punkte P = (x_P, y_P) und Q = (x_Q, y_Q) auf der
Kurve. Dann können wir eine Gerade durch diese legen und bekommen häufig einen
dritten Schnittpunkt.

Bemerkung 1: Wir bekommen auf keinen Fall einen vierten Schnittpunkt, das
liegt daran, dass wir uns auf Kurve vom Grad 3 beschränkt haben. Warum
können Polynome vom Grad n höchstens n Nullstellen besitzen? Übungsaufgabe:

Tip: Polynomdivision, Nullstelle ist linearer Teiler.

Antwort: Polynomdivision, spalte bei Nullstelle x_0 (x - x_0) ab, dass
geht genau wenn x_0 Nullstelle. Bei n Nullstellen komplett zerlegt,
weitere Nullstelle->Widerspruch.

Der Beweis dafür nutzt die Tatsache dass alle x-Werte der Schnittpunkte einer
Geraden mit der Kurve eine Gleichung dritten Gerades erfüllen, und man für
jede Lösung x_0 einen Linearfaktor aus der Gleichung herausziehen kann.

Bemerkung 2: Der dritte Schnittpunkt hat ebenfalls rationale Koordinaten.

Warum? Für den dritten Schnittpunkt gelten zwei Gleichungen: Die
Geradengleichung von der Form $y = s * x + o$ (Die genaue Formel für Konstanten
x und c ausgedrückt durch $x_P, y_P, x_Q, y_Q$ ist vielleicht noch aus der
Schule bekannt) und die Kurvengleichung $y^2 = x^3 + ax + b$. Durch Einsetzen
der ersten Gleichung in die zweite kann man das y wegbekommen und erhält eine
Gleichung nur in x, und zwar vom Grad 3 und mit rationalen Koeffizienten. Sie
hat die Form:

  x^3 + c_2 x^2 + c_1 x + c_0 = 0 (2)

Diese Gleichung hat aber zwei Lösungen, die uns schon bekannt sind: $x_P$ und
$x_Q$. Also kann man die Linearfaktoren $x - x_P$ und $x - x_Q$ aus dem
Polynom auf der linken Seite herausziehen, dann bleibt nur noch ein
Linearfaktor übrig, also lässt sich die linke Seite schreiben als:

  (x - x_P) (x - x_Q) (x - x_3) (3)

mit irgendeinem unbekannten x_3. Es handelt sich aber weiterhin um dasselbe
Polynom, das heißt wenn wir (3) ausmultiplizeren und den Koeffizienten von
$x^2$ betrachten, muss dieser gleich $c_2$ sein:

  - x_P - x_Q - x_3 = c_2

Und wenn $x_P, x_Q$ und $a$ rational sind ist es offenbar auch $x_3$.

Damit ist etwas interessantes passiert: Wir haben aus zwei rationalen Punkten
einen dritten konstruiert.

Und es kommt noch besser: Nicht nur dass wir einen dritten Punkt gefunden
haben, wir haben falls y_3 != 0 sogar noch einen vierten Punkt, nämlich den
Punkt (x_3, -y_3) schließlich ist die Kurve in Weierstraß-Normalform
spiegelsymmetrisch zur x-Achse.

Bezeichnen wir den so erhaltenen dritten Punkt, also erst dritten Schnittpunkt
nehmen, dann Spiegeln an der x-Achse als $P \oplus Q =: R = (x_R, x_R)$,
können wir indem wir das oben Gesagte konkret durchführen eine Formel für R
bekommen:

Sei s := (y_P - y_Q) / (x_P - x_Q)

Dann ist:

  x_R = s^2 - x_P - x_Q
  y_R = - y_P + s (x_P - x_R)


Und mit diesem Punkt R können wir dieselbe Konstruktion fortsetzen: Gerade
durch (x_P, y_P) und (x_R, y_R) legen, wir erhalten einen dritten
Schnittpunkt, spiegeln ihn an der x-Achse und erhalten (x_S, y_S) und so
weiter.

Example: Kurve $y^2 = x^3 - x + 1$

Anfangs sind P = (1,1) und Q = (-1, 1) (eigentlich == 2P), dann kommen die
Punkte nP + Q (0, -1), (3, -5), (5, 11), (1/4, 7/8), (-11/9, 34/54)

Images ec7-addpt-xxx.png


Es stellt sich heraus, dass die Operation \x folgende Eigenschaften hat
(Großbuchstaben bezeichnen in den folgenden Formeln Punkte auf der Kurve, also
Koordinatenpaare (x, y):

  P \x Q = Q \x P                (1)

  (P \x Q) \x R = P \x (Q \x R)   (2)

Das ist den Eigenschaften der Addition schon sehr ähnlich, es bleiben nur zwei
Probleme:

- Was tun wenn wir einen Punkt mit $y_p = 0$ zu sich selbst addieren wollen?
- Was wenn wir zwei Punkte mit derselben x- aber unterschiedlichen y-Werten
  addieren wollen.

Damit eng zusammen hängt die folgende Eigenschaft, die wir für die Addition
gerne hätten, damit sie mehr wie eine normal Addition wirkt. (Mathematisch:
wir wollen, dass die Punkte unter der Addition eine Gruppe bilden).
Es gibt einen Punkt O mit der Eigenschaft:

  P \x O = P

für alle P, und für alle P gibt es einen Punkt P', so dass:

  P \x P' = O

Dieser neutrale Punkt ist der von dem es bei vielen Beschreibungen einfach
heißt, er liege `im Unendlichen`. Wir wollen das aber präzise fassen, und dazu
machen wir etwas, was auch sonst nützlich ist: Wir treten aus der Ebene heraus
und sehen uns die Kurve etwas aus der Entfernung an.



Diesmal beginnen wir mit der arithmetischen Formulierung, da diese im
Vergleich zur geometrischen Betrachtung etwas einfacher zu beschreiben ist:

Wir nehmen zu den Kurvenkoordinaten x und y im zweidimensionalen Raum die
Koordinate z im dreidimensionalen Raum dazu, allerdings mit der
Zusatzbedingung, dass nicht alle drei Werte gleichzeitig Null sein dürfen.
Warum? Kommt später, wenn wir die geometrische Sichtweise ansehen. Erstmal
einfach so hinnehmen.

Die Gleichung der elliptischen Kurve wird nun homogenisiert: Es wird an jeden
Summand eine Potenz von $z$ dranmultipliziert, so dass die Summe der
Exponenten überall drei wird. Die Zahlen $a$ und $b$ gelten weiterhin als
Konstanten, werden also bei der Summe der Exponenten nicht mitgezählt.

Damit haben wir jetzt natürlich viel mehr Lösungen als vorher, das machen wir
(fast, und das ist der eigentliche Trick dabei) wieder rückgängig, indem wir
zwei verschiedene Lösungen als äquivalent betrachten, wenn sie sich nur durch
einen konstanten Faktor unterscheiden.

Das macht natürlich nur Sinn, wenn sich die Eigenschaft `liegt auf der Kurve`
bei zueinander äquivalenten Punkten nicht ändert, und in der Tat gilt::

    & & (x_1, y_1, z_1) \in E \\
    & \Rightarrow &
    y_1^2 z_1 = x_1^3 + a x_1 z_1^2 + b z_1^3 \\
    & \Rightarrow &
    \lambda^3 y_1^2 z_1
    = \lambda^3 x_1^3 + \lambda^3 a x_1 z_1^2 + \lambda^3 b z_1^3 \\
    & \Rightarrow &
    (\lambda y_1)^2 \lambda z_1 = (\lambda x_1)^3
    + a \lambda x_1 (\lambda z_1)^2 + b (\lambda z_1)^3 \\
    & \Rightarrow &
    (y_2)^2 z_2 = (x_2)^3
    + a x_2 (z_2)^2 + b (z_2)^3 \\
    & \Rightarrow & (x_2, y_2, z_2) \in E


Für die Addition (s.o.) fehlten uns noch die Fälle $x_p = x_q$ bzw. $P=Q$ und
$y=0$. Die können wir nun festlegen. Zur praktischen Berechnung spielt der
Punkt im Unendlichen also keine wirkliche Rolle, er ist einfach ein weiterer
Spezialfall der Regeln.

Was haben wir geometrisch gesehen gemacht? Wir haben einen Punkt in der Ebene
durch eine Gerade durch den Nullpunkt ersetzt (Hier kommt die Bedingung dass
mindestens eine Koordinate $!= 0$ sein muss ins Spiel, sonst bekommt man aus
einem Punkt nicht eindeutig eine Gerade durch den Nullpunkt).  Eine Gerade
wird zu einer Ebene durch den Ursprung. Unsere Kurve wird zu einem Bündel von
Geraden, die sich wie ein Vorhang bauscht.

Ein klein wenig einfacher wird das, wenn wir unsere Sicht auf eine Kugel vom
Radius 1 um den Nullpunkt beschränken. Unsere Kurve ist dann tatsächlich eine
Kurve auf der Kugel, nur dass jeweils zwei Antipoden als einziger Punkt
aufgefasst werden müssen. Wenn man nun eine Lichtquelle in den Nullpunkt
stellt, und in die Ebene $z = 1$ eine Leinwand stellt, wird unsere
ursprüngliche ebene Kurve genau die Projektion auf die Leinwand, daher der
Name "projektive Ebene".


Was haben wir bis jetzt?

- Eine Kurve, genauer eine Menge von Punkten (x, y), die Gleichung in
  Weierstraß-Form erfüllen.
- Eine Operation \oplus auf der Kurve, also eine Formel, die aus zwei Punkten
  P_1 = (x_1, y_1), und P_2 = (x_2, y_2) einen dritten Punkt
  P_3 = (x_3, y_3) = P_1 \oplus P_2 macht.

Achtung: Diese Addition von Punkten hat mit der aus der Schule bekannten
Addition von zweidimensionalen Vektoren in der Ebene nichts zu tun,
insbesondere ist ganz offensichtlich
$(x_1, y_1) \oplus (x_2, y_2) \ne (x_1 + x_2, y_1 + y_2)$

Endliche Körper
===============


Jetzt möchten wir konkrete Berechnungen vornehmen und zwar auf Computern,
die nicht beliebig genau rechnen können. Zunächst stellen wir fest, das sowohl
bei der Definition elliptischer Kurven als auch bei den Formeln für die
Addition von Punkten nur die normalen Grundrechenarten Addition, Subtraktion,
Multiplikation und Division eingegangen sind, sowie die bekannten
Rechenregeln. So etwas nennen Mathematiker einen `Körper` (engl. `field`), und
definieren das noch etwas genauer, aber die Definition wäre in diesem Rahmen
etwas zu technisch.

Bekannte Beispiele für Körper wären die Menge der reellen
Zahlen $\R$, die Menge der rationalen Zahlen $\Q$ oder die Menger der
komplexen Zahlen.

Eine Folgerung aus der genauen Definiton benötigen wir aber im Folgenden, das
ist eine weitere `bekannte` Rechenregel:

Sei K ein Körper, seien a, b \in K mit a != 0, b != 0, dann gilt: a * b != 0.

Gibt es noch andere Körper, insbesondere welche, in denen wir ohne
Genauigkeitsverlust rechnen können? Ja, die gibt es, es handelt sich um die
`endlichen` Körper.

Die wichtigste Zutat für diese ist bereits aus der Grundschule bekannt: Die
Division mit Rest. Dazu legen wir eine ganze Zahl $N$ fest und sagen dann,
von einer beliebigen Zahl a interessiert uns eigentlich nur der Rest beim
Teilen durch $N$. Anders, und mathematisch etwas präziser ausgedrückt: Wir
teilen die gesamte Menge der ganzen Zahlen \Z in $N$ Klassen ein: Alle Zahlen
die beim Teilen durch $N$ denselben Rest ergeben, sind in einer Klasse.

Wir definieren dann die Addition bzw. Multiplikation zweier Klassen, indem wir
aus den beiden Klassen jeweils irgendwelche Zahlen wählen, diese addieren
bzw. multiplizieren, und die Klasse als Ergebnis nehmen, in der die Summe
bzw. das Produkt liegt.

Aber halt: "Irgendwelche"? Dann kommt doch beim Addieren bzw. Multiplizieren
immer was anderes aus, je nachdem welche Zahlen aus der Klasse wir
wählen. Stimmt, es kommen je nachdem verschiedene Zahlen heraus, aber die
liegen alle in derselben Klasse. Das ist der Inhalt des Lemmas.

Können wir N beliebig wählen? Nehmen wir an N ist zusammengesetzt, also N =
n_1 n_2 mit n_1, n_2 < N, Dann ist n_1 n_2 \equiv 0, im Widerspruch zur
Körpereigenschaft oben.

Also muss $N$ notwendigerweise prim sein. Diese Bedingung ist jedoch auch
schon hinreichend.

Äquivalenzklassen sind schön für die Theorie, aber Wie rechnen wir nun
praktisch?

Wir beschränken uns auf die Zahlen 0..p-1.
Wenn die Ausgangszahlen nicht in diesem Bereich liegen sollten, wenden wir
Division mit Rest durch $p$ an. Addition, Subtraktion und Multiplikation von
ganzen Zahlen gibt wieder ganze Zahlen, und durch Division mit Rest kommen wir
wieder in das Intervall 0..p-1.

Addition und Multiplikation geht normal, nur dass wir das
Ergebis wieder durch Division mit Rest auf den Bereich 0..p-1 bringen.

Wenn bei der Division eine ganze Zahl rauskommt, können wir die auch normal
rechnen.

Aber was wenn nicht?

Was ist eigentlich $\frac a b (mod p) = q$? Es ist die Zahl $q$ aus $0..p-1$, für
die $q*b = a (mod p)$ oder:  $a - q*b = m p$ für $m \in \Z$. Offenbar reicht
uns ein Verfahren um $\frac 1 b$ zu bestimmen. Am besten lässt sich das mit
einem Beispiel erläutern: Wir legen $p=37 fest, und wollen das multiplikative
Inverse von 10 bestimmen, also zwei Zahlen q und m so dass:

  m * 37 + q * 10 = 1

Das m selbst brauchen wir nicht, aber wenn es bei dem Verfahren mit
herausfällt, ist das zur Kontrolle auch ok. Woran wir eigentlich interessiert
sind, ist das $q$.

Das sieht jetzt ein wenig wie ein Zaubertrick aus. Wir fangen mit etwas völlig
Offensichtlichen an, was uns der Lösung scheinbar keinen Schritt weiterbringt,
Wir schreiben zwei Anfangsgleichungen hin:

  1 * 37 + 0 * 10 = 37  (1)
  0 * 37 + 1 * 10 = 10  (2)

Nun kombinieren wir diese Gleichungen auf die richtige Art und Weise, so dass
die Zahl auf der linken Seite immer kleiner wird. Auf der rechten Seite stehen
37 und 10, wir teilen 37 durch 10 mit Rest und erhalten: $37 = 3*10 + 7$,
bzw. $37 - 3 * 10 = 7$, wir multiplizieren also Gleichung (2) mit -3 und
zählen Gleichung (1) dazu:

  (1*1 + (-3)*0) * 37 + (1*0 - 3*1) * 10 = 1*37-3*10 = 7
  1 *37 + (-3) * 10 = 7 (3)

Jetzt kombinieren wir Gleichung (2) und (3). Die Zahlen auf der rechten Seite
sind 10 und 7. Wir teilen 10 mit Rest durch 7 und bekommen: $10 = 1 * 7 + 3$
also $1 * 10 - 1 * 7 = 3$, heißt wir müssen Gleichung (3) mit -1
multiplizieren und von Gleichung (2) abziehen:

  (1*0 - 1*1) * 37 + (1*1 + (-1)*(-3)) * 10= 1*10-1*7 = 3
  (-1) * 37 + 4 * 10 = 3 (4)

Die Zahlen auf den rechten Seiten sind 7 und 3, wir teilen dann 7 durch 3 mit
Rest und bekommen: $7 = 2*3 - 1$ bzw. $7 - 2*3 = 1$, also nehmen wir Gleichung
4 mit $(-2)$ mal und zählen Gleichung (3) dazu:

  (1 + (-1)*(-2)) * 37 + (1*(-3) + (-2)*4) * 10 = 7-2*3 = 1
  (-3) * 37 + (-11) * 10 = 1 (5)

Damit ist das multiplikative Inverse von 10 mod 37 gleich -11, bzw. $-11 + 37
= 26$

Das gesamte Verfahren ist letztlich der euklidische Algorithmus zum Bestimmen
des kleinsten gemeinsament Teilers der Zahlen 37 und 10, plus ein wenig
Buchhaltung. Weil 10 und 37 teilerfremd sind (sonst wäre 37 nicht prim), muss
die Folge der Zahlen auf der rechten Seite irgendwann mit 1 enden.

Wenn man beim Teilen mit Rest auch negative Rest erlaubt, statt wie oben auf
positiven zu bestehen, kann man sehen, dass die Folge der Zahlen auf der
rechten Seite immer mindestens um den Faktor 2 kleiner wird, das Verfahren ist
also sehr effizient.

Außerdem braucht man sich nie mehr als die Koeffizienten der letzten zwei
Gleichungen zu merken, das Verfahren braucht also konstanten Speicherplatz.

Über endlichen Körpern sehen unsere elliptischen Kurven nun wenig intuitiv
aus. Beispiel: [finplot.png]

Funktioniert der Übergang zu endlichen Körpern nun überhaupt? Will heißen:
Gibt es überhaupt genügend Punkte auf diesen Kurven? Die Antwort hat Helmut
Hasse (* 25.8.1898  + 26.12.1979) 1933 gegeben:

Satz (Hasse-Schranke): Sei E eine elliptische Kurve über \F_p Sei N die
Anzahl der Punkte auf E. Dann ist

$$ \| N - p - 1 \| \le 2 \sqrt{p} $$

Zu jedem x-Wert gibt es entweder keinen oder zwei Punkte auf der Kurve. Die Anzahl
der möglichen x-Werte ist p, der Satz sagt also, dass auf der Kurve etwa halb
so viele Punkte liegen wie maximal möglich wäre.

Für große q (und solche interessieren uns ja für die Kryptographie) ist die
Wurzel im Vergleich zu q eher klein, und damit besagt der Satz, das etwa die
Hälfte der Punkte des gesamten Raumes auf der Kurve liegt.

Für elliptische Kurven über endlichen Körpern gibt es sogar ein effizientes
Verfahren, den Schoof-Algorithmus, benannt nach René Schoof (* 1955-05-08),
die Anzahl der Punkte zu bestimmen.

Praktisch werden in standardisierten Verfahren im Wesentlichen vier Kurven
benutzt, jeweils mit verschiedenen endlichen Köpern. Die Primzahlen haben
dabei 76, 117 und 156 Dezimalstellen.

EC Diffie-Hellman
=================

Jetzt haben wir alle Zutaten beisammen: Wir haben elliptische Kurven, und
Punkte darauf, mit denen wir (bzw. die Computer) effizient rechnen können, wo
kommt jetzt die Kryptographie her?

Diffie-Hellman ist kein Verschlüsselungsverfahren, und auch kein
Signaturverfahren, sondern ein Schlüsselaustauschverfahren.  Damit können sich
zwei Leute - üblicherweise Alice und Bob genannt - auf ein gemeinsames
Geheimnis einigen, obwohl sie dabei nur einen öffentlichen Kanal kommunizieren
auf dem eine Lauscherin Eve lauscht.

Eine Möglichkeit, so ein gemeinsames Geheimnis zu nutzen wäre zum
Beispiel es als Key für ein konventionellles symmetrisches
Verschlüsselungsverfahen zu nutzen (AES).

Benannt nach seinen Erfindern Whitfield Diffie (* 1944-06-05) und Martin
Hellman (*1945-10-02), nach einem generellen Konzept von Ralph Merkle (*
1952-02-02) Das Verfahren wurde 1976 publiziert, basierte damals jedoch nicht
auf elliptischen Kurven.

Vorher haben A und B eine elliptische Kurve E zusammen mit einem
endlichen Körper K festgelegt, und zusätzlich noch einen Punkt P. P
ist dabei so gewählt, dass die Sequenz P, P+P, P+P+P ... `lange`
braucht um sich zu wiederholen. (Anmerkung: Wir wollen zusätzlich, dass die
Anzahl der Additionen bis sich das Ergebnis wiederholt eine Primzahl ist.) Mit
lang meinen wir eine Zahl die in etwa so viele Stellen wie die Primzahl
unseres endlichen Körpers. Diese Informationen sind öffentlich
und insbesondere auch E bekannt.

Alice wählt nun ihr Geheims s_A, eine lange Dezimalzahl. Sie berechnet
daraus P + ... + P, s_A - mal.

(Aufmerksame Leute werden sich fragen wie das mit so großen Zahlen
gehen soll. Antwort: Wiederholtes Verdoppeln und Addieren statt immer wieder
eins drauf zu addieren)

Dann übermittelt Alice das Ergebnis P_A - ein Punkt auf der Kurve - an
Bob.

Bob macht auf seiner Seite währenddessen dasselbe, er wählt sein
eigenes Geheimnis s_B, und berechnet P + ... + P, s_B mal. Dann
übermittelt er das Ergebnis P_B an Alice.

Nun kennt Alice s_A und P_B, Bob dagegen kennt s_B und P_A.

Alice berechnet nun P_B + ... + P_B (s_A mal) und erhält P_S (ein
Punkt auf der Kurve).

Bob berechnet P_A + ... + P_A (s_B mal) und erhält P_S'

Aber nun ist

     P_S = P_B + ... + P_B =
           (P + ...^s_B + P) + ...^s_A + (P + ... +P)
         = P + ...^ s_A s_B P =
	 = P + ...^ s_B s_A P =
	 = P + ...^s_A P + ...^s_B
	 = P_a + ...^s_B + P_a =
	 = P_S'

Damit sind P_S und P_S' derselbe Punkt und somit ein gemeinsames
Geheimnis. Eve dagegen kennt nur P_a und P_b, bekommt damit aber weder
s_A noch s_B heraus. (Außer sie hat einen funktionierenden
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


Allgemeines Konzept: Äquivalenzklassen
======================================
Vorstellung des generellen mathematischen Konzeptes neue Objekte zu bilden
indem schon vorhandene in Äquivalenzklassen aufgeteilt werden:

1) Punkte im 3-dimensionalen Raum ohne Nullpunkt. Alle Punkte die auf derselben
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
ist: Wenn man zwei andere Repräsentanten nimmt, muss dasselbe herauskommen,
wobei dasselbe heißt: die beiden verschiedenen Ergebnisse liegen in derselben
Klasse. Bei Multiplikation und Addition funktioniert das. Beim Wurzelziehen
beispielsweise geht es schief:

   sqrt(9) = 3
   sqrt(16) = 4

aber 9 (mod 7) == 2 (mod 7) == 16 (mod 7), wohingegen 3 != 4 (mod 7)

