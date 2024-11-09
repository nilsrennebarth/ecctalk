#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import sys
from math import sqrt


class Ecurve(object):
    """
    Elliptic curve for plotting
    """
    def __init__(self, a=1, b=0, xrange=(-5, 5), yrange=(-5, 5)):
        self.a = a
        self.b = b
        self.xrange = xrange
        self.yrange = yrange
        self.fig, self.axes = plt.subplots(1, figsize=(10.0, 10.0))

    def potential(self, x, y):
        """
        Difference to zero for the contour plot trick
        """
        return y**2 - (x**3 + x * self.a + self.b)

    def yup(self, x):
        """
        Get positive y coordinate of a point on the curve, given x
        """
        y = x**3 + x * self.a + self.b
        return sqrt(y) if y >= 0 else sqrt(-y)

    def plotCoord(self):
        """
        plot coordintate system in cartesian form
        """
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['left'].set_position('zero')
        self.axes.spines['bottom'].set_position('zero')
        # add labels 'x' and 'y'
        self.axes.set_xlabel('x', size=16, loc='right')
        self.axes.set_ylabel('y', size=16, loc='top', rotation=0)
        # add the arrows
        arrfmt = dict(markersize=5, color='black', clip_on=False)
        self.axes.plot(
            (1), (0), marker='>', transform=self.axes.get_yaxis_transform(),
            **arrfmt
        )
        self.axes.plot(
            (0), (1), marker='^', transform=self.axes.get_xaxis_transform(),
            **arrfmt
        )

    def plotGraph(self):
        """
        main plotting of elliptic curve
        """
        y, x = np.ogrid[
            self.yrange[0]:self.yrange[1]:100j,
            self.xrange[0]:self.xrange[1]:100j
        ]  # range grid  [from : to : how_many_points]
        xlist = x.ravel()
        ylist = y.ravel()
        plt.contour(
            xlist, ylist, self.potential(x, y), [0],
            colors="r", linewidths=3
        )

    def plotTitle(self):
        def sig(x):
            return '+' if x > 0 else '-'

        title = "$y^{{2}} = x^{{3}}"
        if self.a != 0:
            title += f" {sig(self.a)}"
            if abs(self.a) != 1:
                title += f"  {abs(self.a):}"
            title += "x"
        if self.b != 0:
            title += f" {sig(self.b)} {abs(self.b)}"
        title += "$"
        plt.title(title, fontsize=20, color='b', pad=40)

    def plotAll(self, outname):
        self.plotCoord()
        self.plotGraph()
        self.plotTitle()
        plt.savefig(outname)
        plt.close(self.fig)


def numval(s):
    try:
        return int(s)
    except ValueError:
        pass
    return float(s)


def main():
    args = {}
    outfile = 'plot.png'
    for a in sys.argv[1:]:
        name, _, value = a.partition('=')
        if _ != '=':
            outfile = a
        elif name == 'a' or name == 'b':
            args[name] = numval(value)
        elif name == 'xrange' or name == 'yrange':
            mi, _, ma = value.partition(',')
            args[name] = (numval(mi), numval(ma))
    Ecurve(**args).plotAll(outfile)


if __name__ == '__main__':
    main()
