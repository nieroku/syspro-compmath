import numpy as np


def integrate(h, ys):
    return (2 * ys[2:-1:2].sum() + 4 * ys[1::2].sum() + ys[0] + ys[-1]) * h / 3
