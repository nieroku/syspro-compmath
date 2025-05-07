import matplotlib.pyplot as plt
from common import *

upto = 33

naive_max_delta = []
chebyshev_max_delta = []
for n in range(3, upto):
    nodes = evenlySpaced(n)
    poly = interpolate(nodes)
    naive_max_delta.append(max(poly(x) - f(x) for x in xs))

    nodes = chebyshev(n)
    poly = interpolate(nodes)
    chebyshev_max_delta.append(max(poly(x) - f(x) for x in xs))

plt.semilogy(range(3, upto), naive_max_delta, label="Равномерные узлы")
plt.semilogy(range(3, upto), chebyshev_max_delta, label="Узлы Чебышева")
plt.semilogy(range(4, upto, 2), chebyshev_max_delta[1::2], label="Узлы Чебышева (нечётное число узлов)")
plt.legend()

plt.show()
