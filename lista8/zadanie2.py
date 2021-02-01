from scipy.linalg import hilbert
# Poniewaz macierz Hilberta jest rowniez macierza hermitowska, uzywam eigh zamiast eig
from scipy.linalg import eigh
import numpy as np


A = np.array(hilbert(6))

w, v = eigh(A)

print("Wartości własne: ", w, sep="\n")
print("Wektory własne: ", v, sep="\n")