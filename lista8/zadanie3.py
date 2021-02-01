from scipy.linalg import eigh_tridiagonal
import numpy as np

n_array = [10, 100]

for n in n_array:
    d = 2 * np.ones(n)
    nd = -1 * np.ones(n-1)
    w3, v3 = eigh_tridiagonal(d, nd)

    print("Wartosci wlasne: ", w3)

    print("\nWektory wlasne", v3)

