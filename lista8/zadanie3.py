from scipy.linalg import eigh_tridiagonal
import numpy as np

n_array = [10, 100]

for n in n_array:
    print(f"\n n = {n}\n\n")
    d = 2 * np.ones(n)
    nd = -1 * np.ones(n-1)
    w3, v3 = eigh_tridiagonal(d, nd)

    print("Wartosci wlasne: ")
    for i in range(3):
        print(w3[i])

    print("Wektory wlasne: ")
    for i in range(3):
        print(v3[i])


