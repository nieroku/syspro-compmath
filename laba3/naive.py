import matplotlib.pyplot as plt
from common import *


plt.plot(xs, f(xs))

for n in range(3, 10 + 1):
    nodes = evenlySpaced(n)
    poly = interpolate(nodes)
    plt.plot(xs, poly(xs))
    plt.pause(1)

plt.show()
