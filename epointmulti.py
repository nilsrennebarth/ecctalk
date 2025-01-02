#!/usr/bin/env python3
import matplotlib.pyplot as plt
from ecurve import Ecurve


class Ecpoints:
    Points = [
        (1, 1), (-1, 1), (0, -1), (3, -5), (5, 11),
        (1/4, 7/8), (-11/9, -34/54)
    ]
    Names = ["P", "Q", "R", "S", "T", "U", "V"]
    Values = [
        "(1, 1)", "(-1, 1)", "(0, -1)", "(3, -5)", "(5, 11)",
        "(1/4, 7/8)", "(-11/9, -34/54)"
    ]

    def __init__(self):
        self.img = 0

    def plotdot(self, P, name):
        plt.plot(P[0], P[1], "ok")
        plt.text(P[0] - 0.15, P[1] + 0.25, name, fontsize=20)

    def plotline(self, Q, R):
        def line(x):
            return (x - vect[0][0]) * s + vect[0][1]

        vect = [self.Points[0], Q, [R[0], -R[1]]]
        vect.sort(key=lambda x: x[0])
        # slope of line
        s = (vect[2][1] - vect[0][1]) / (vect[2][0] - vect[0][0])
        plt.plot([-1.7, 5.2], [line(-1.7), line(5.2)], color="c", linewidth=1)

    def plotbox(self, i: int):
        text = "\n".join(
            f'{self.Names[j]} = {self.Values[j]}'
            for j in range(i+1)
        )
        plt.text(
            -2, 10, text, fontsize=20, va='top',
            bbox=dict(boxstyle='round', facecolor='wheat')
        )

    def bg(self, i: int):
        self.E = Ecurve(
            a=-1, b=1, xrange=(-2, 6), yrange=(-12, 12), size=20.0
        )
        self.E.plotCoord()
        self.E.plotGraph()
        self.E.plotTitle()
        for j in range(i+1):
            self.plotdot(self.Points[j], self.Names[j])

    def saveimg(self):
        plt.savefig(f'ec7-addpt-{self.img:03d}', bbox_inches='tight')
        plt.close(self.E.fig)
        self.img += 1

    def plotseq(self, i):
        self.bg(i)
        self.plotbox(i)
        self.saveimg()
        self.bg(i)
        self.plotbox(i)
        self.plotline(self.Points[i], self.Points[i+1])
        self.saveimg()
        self.bg(i)
        self.plotbox(i)
        self.plotline(self.Points[i], self.Points[i+1])
        plt.plot(self.Points[i+1][0], -self.Points[i+1][1], "xk")
        self.saveimg()
        self.bg(i)
        self.plotbox(i)
        self.plotline(self.Points[i], self.Points[i+1])
        plt.plot(self.Points[i+1][0], -self.Points[i+1][1], "xk")
        R = self.Points[i+1]
        self.E.axes.arrow(
            R[0], -R[1], 0, 2 * R[1],
            head_width=0.1, head_length=0.2, length_includes_head=True,
            linestyle='dashed', color='y'
        )
        self.saveimg()
        if i == len(self.Points)-2:
            self.bg(i+1)
            self.plotbox(i + 1)
            self.saveimg()


def main():
    E = Ecpoints()
    for i in range(1, 6):
        E.plotseq(i)


main()
