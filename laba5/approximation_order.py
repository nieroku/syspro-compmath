import numpy as np
from common import *


def exact(x):
    return -np.cos(x)


num_nodes = 200
boundary_conditions = 1, 0, 0, 0, 1, 1
for i in range(1, 3 + 1):
    xs = np.linspace(-np.pi / 2, np.pi / 2, num_nodes)
    xs2 = np.linspace(-np.pi / 2, np.pi / 2, 2 * num_nodes)
    solution = solve(num_nodes, boundary_conditions)
    solution2 = solve(2 * num_nodes, boundary_conditions)
    numerator = np.abs(exact(xs) - solution).max()
    denominator = np.abs(exact(xs2) - solution2).max()
    print(f"p_{i} = {np.log2(numerator / denominator)}")
    num_nodes *= 2
