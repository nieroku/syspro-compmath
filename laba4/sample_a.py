import numpy as np
from simpson import integrate

# NIntegrate[Sin[Pi x^5]/((1 - x) x^5), {x, 0, 1}]
EXACT = 8.03491067542
PRECISION = 1e-8


def f(x):
    return np.sin(x ** 5 * np.pi) / ((1-x) * x ** 5)


def integrate_f(n):
    xs = np.linspace(0, 1, n + 1, endpoint=True)
    ys = np.concatenate(([np.pi], f(xs[1:-1]), [5 * np.pi]))
    h = xs[1] - xs[0]
    return integrate(h, ys)


n = 2
while True:
    value = integrate_f(n)
    if abs(value - EXACT) < PRECISION:
        h_over_2 = integrate_f(n * 2)
        h_over_4 = integrate_f(n * 4)
        p = np.log2(abs(value - h_over_2) / abs(h_over_2 - h_over_4))
        print("value:", value)
        print("order of approximation:", p)
        print("number of splits:", n)
        break
    n *= 2
