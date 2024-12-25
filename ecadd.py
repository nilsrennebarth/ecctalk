#!/usr/bin/env python3
import matplotlib.pyplot as plt
from ecurve import Ecurve


def main():
    E = Ecurve(a=-1, b=1, xrange=(-2, 2.1), yrange=(-4.1, 4.1), size=20.0)
    E.plotCoord()
    E.plotGraph()
    E.plotTitle()
    Points = [(1, 1), (-1, 1), (0, -1)]

    P = Points[0]
    plt.text(P[0] - 0.15, P[1] + 0.25, "P", fontsize=20)
    P = Points[1]
    plt.text(P[0] - 0.15, P[1] + 0.25, "Q", fontsize=20)
    P = Points[2]
    E.plotsum(Points[0], Points[1], Points[2], "R")
    plt.plot(
        [-1.5, 1.5], [1, 1], color="c", linewidth=1
    )
    plt.savefig('ec5-m1-p1-add.png', bbox_inches='tight')
    plt.close(E.fig)


main()
