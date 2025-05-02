import numpy as np
import math


def f(x):
    return 1 / ((25 * x * x) + 1)


class HornerPolynomial:
    def __init__(self, nodes, coefs):
        self.nodes = nodes
        self.coefs = coefs

    def __call__(self, x, i=0):
        if i + 1 == len(self.coefs):
            return self.coefs[-1]
        return self.coefs[i] + (x - self.nodes[i]) * self(x, i+1)


def interpolate(nodes):
    n = len(nodes)-1
    divided_diffs = [f(nodes)]
    for i in range(n):
        next_divs = []
        for j in range(n - i):
            next_divs.append(
                (divided_diffs[-1][j] - divided_diffs[-1][j + 1])
                /
                (nodes[j] - nodes[j + i + 1])
            )
        divided_diffs.append(next_divs)
    return HornerPolynomial(
        nodes,
        list(map(lambda it: it[0], divided_diffs))
    )


def evenlySpaced(n):
    return np.array([(2 * i / n) - 1 for i in range(n + 1)])


def chebyshev(n):
    return np.array(
        [2 * math.cos(((2 * k + 1) * math.pi)/(2 * (n + 1)))
         for k in range(n + 1)]
    )


xs = np.linspace(-1.0, 1.0, 1000)
