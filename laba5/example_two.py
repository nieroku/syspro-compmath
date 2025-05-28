import numpy as np
from common import *

show_example((1, 0, 0, 1, 0, 1), lambda x: 1 / 2 + x / np.pi - np.cos(x))
