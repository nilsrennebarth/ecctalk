#!/usr/bin/env python3
"""
Plot a curve over a finite field

This is a very simple minded program and only works for small
primes.
"""
import matplotlib.pyplot as plt
import numpy as np

P = 37


def efunc(x):
    return (x**3 - x + 1) % P


def main():
    fig, axes = plt.subplots(1, figsize=(10.0, 10.0))
    # Calculate square roots as a dict
    sqrt = {(x*x) % P: x for x in range(1, (P+1)//2)}
    sqrt[0] = 0
    # Initialize list of points
    points = []
    for x in range(P):
        ysquare = efunc(x)
        if ysquare not in sqrt:
            continue
        points += [
            (x, sqrt[ysquare]),
            (x, P - sqrt[ysquare])
        ]
    plist = np.transpose(np.array(points))
    plt.plot(plist[0], plist[1], "ok")
    plt.title(
        r'$y^{2} = x^{3} - x + 1$ über $\mathbb{F}_{37}$',
        fontsize=24, color='b', pad=20
    )
    plt.savefig('finplot.png')


main()
