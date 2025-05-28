import numpy as np
import matplotlib.pyplot as plt

A, B = -np.pi / 2, np.pi / 2


def thomas_algorithm(a, b, c, d):
    n = len(b)

    alpha, beta = [-c[0] / b[0]], [d[0] / b[0]]
    for i in range(1, n):
        divisor = a[i] * alpha[-1] + b[i]
        alpha.append(-c[i]/divisor)
        beta.append((d[i] - a[i] * beta[i - 1])/divisor)

    x = [beta[-1]]
    for i in range(n-2, -1, -1):
        x.append(alpha[i] * x[-1] + beta[i])
    x.reverse()
    return np.array(x)


def solve(num_nodes, boundary_condition):
    assert num_nodes >= 2

    h = (B - A) / (num_nodes - 1)
    h_sqr = h ** 2

    a1, b1, c1, a2, b2, c2 = boundary_condition

    a = np.repeat(1 / h_sqr, num_nodes)
    b = np.repeat(-2 / h_sqr, num_nodes)
    c = np.repeat(1 / h_sqr, num_nodes)
    a[0], c[-1] = 0, 0
    b[0], c[0] = a1 - (b1 / h), b1 / h
    a[-1], b[-1] = -b2 / h, a2 + (b2 / h)

    d = np.cos(np.linspace(A, B, num_nodes))
    d[0], d[-1] = c1, c2

    return thomas_algorithm(a, b, c, d)


def show_example(boundary_conditions, expected):
    num_nodes = 100
    xs = np.linspace(-np.pi / 2, np.pi / 2, num_nodes)
    ys = solve(num_nodes, boundary_conditions)
    plt.plot(xs, ys, 'bo')
    plt.plot(xs, expected(xs))
    a1, b1, c1, a2, b2, c2 = boundary_conditions
    plt.title(
        f"{a1} * y(-π/2) + {b1} * y'(-π/2) = {c1};"
        + f" {a2} * y(π/2) + {b2} * y'(π/2) = {c2}",
    )
    plt.show()
