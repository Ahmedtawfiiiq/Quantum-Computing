import numpy as np

s = 4
N = 128
theta = np.arcsin(np.sqrt(s / N))
t = int(np.floor(np.pi / (4 * theta)))
print(t)
