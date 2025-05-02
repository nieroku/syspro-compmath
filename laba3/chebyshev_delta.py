import matplotlib.pyplot as plt
from common import *

for n in range(3, 10 + 1):
    nodes = chebyshev(n)
    poly = interpolate(nodes)
    plt.plot(xs, poly(xs) - f(xs))
    plt.pause(1)

plt.show()
