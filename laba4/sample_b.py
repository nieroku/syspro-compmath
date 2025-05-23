import numpy as np
from simpson import integrate


# NIntegrate[E^(-Sqrt[x] + Sin[x/10]), {x, 0, Infinity}, WorkingPrecision -> 200]
EXACT = 2.98100345255833825
PRECISION = 1e-8


def f(t):
    if t+PRECISION >= 1:
        return 0
    x = t / (1 - t)
    divisor = (1 - t) ** 2
    dividend = np.exp(np.sin(x / 10) - np.sqrt(x))
    return dividend / divisor


def integrate_f(n):
    ts = np.linspace(0, 1, n + 1, endpoint=True)
    ys = np.vectorize(f)(ts)
    h = ts[1] - ts[0]
    return integrate(h, ys)


n = 2
while True:
    value = integrate_f(n)
    if abs(value - EXACT) < PRECISION:
        print("value:", value)
        print("number of splits:", n)
        break
    n *= 2
