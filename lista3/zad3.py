import numpy as np
from scipy import linalg

A = np.array([[0, 0, 2, 1, 2],
              [0, 1, 0, 2, -1],
              [1, 2, 0, -2, 0],
              [0, 0, 0, -1, 1],
              [0, 1, -1, 1, -1]])

B = np.array([[1], [1], [-4], [-2], [-1]])

x = linalg.solve(A, B)

print(x)

# Sprawdzanie czy wynik sie zgadza
print(np.allclose(np.dot(A, x), B))

