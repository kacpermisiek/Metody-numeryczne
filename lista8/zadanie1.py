from scipy.linalg import eig
import numpy as np

A = np.array([[-1, -4, 1],
              [-1, -2, -5],
              [5, 4, 3]], dtype=float)
# A - nie jest macierzą hermitowską


w, v = eig(A)

print("Wartości własne: ", w, sep="\n")
print("Wektory własne: ", v, sep="\n")