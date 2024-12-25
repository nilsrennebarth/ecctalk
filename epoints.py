#!/usr/bin/env python3
import matplotlib.pyplot as plt
from ecurve import Ecurve


def main():
    E = Ecurve(a=-1, b=1, xrange=(-2, 6), yrange=(-12, 12), size=20.0)
    E.plotCoord()
    E.plotGraph()
    E.plotTitle()
    Points = [
        (1, 1), (-1, 1), (0, -1), (3, -5), (5, 11),
        (1/4, 7/8), (-11/9, -34/54)
    ]
    Names = ["P", "Q", "R", "S", "T", "U", "V"]
    Values = [
        "(1, 1)", "(-1, 1)", "(0, -1)", "(3, -5)", "(5, 11)",
        "(1/4, 7/8)", "(-11/9, -34/54)"
    ]

    P = Points[0]
    plt.text(P[0] - 0.15, P[1] + 0.25, "P", fontsize=20)
    P = Points[1]
    plt.text(P[0] - 0.15, P[1] + 0.25, "Q", fontsize=20)
    for i in range(1, 6):
        E.plotsum(Points[0], Points[i], Points[i+1], Names[i+1])
    plt.text(
        -2, 10,
        "\n".join(f"${n} = {v}$" for n, v in zip(Names, Values)),
        fontsize=20, va='top', bbox=dict(boxstyle='round', facecolor='wheat')
    )
    plt.savefig('ec6-m1-p1-points.png', bbox_inches='tight')
    plt.close(E.fig)


main()
