import numpy as np

X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
S = np.sqrt(Z)
T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
V = np.sqrt(X)
Rz = lambda theta: np.array([[np.exp(-1j * theta / 2), 0], [0, np.exp(1j * theta / 2)]], dtype=complex)

print(X)
print(np.allclose(np.power(V, 2), X))
