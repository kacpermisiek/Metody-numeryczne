from numpy.linalg import cond, norm
from scipy.linalg import hilbert

n = [5, 10, 20]

for i in n:
    print(f"Macierz Hilberta n = {i}")
    print(f"Norma macierzy: {norm(hilbert(i))}")
    print(f"Wskaznik uwarunkowania: {cond(hilbert(i))}\n")

"""
Macierz Hilberta jest przykladem macierzy zle uwarunkowanekj (ma wysoki wskaznik uwarunkowania)
Numeryczne rozwiazywanie nawet niewielkich ukladow rownan z ta macierza jest praktycznie niemozliwe,
Poniewaz sam blad wynikajacy z numerycznej prezentacji liczb wprowadza nieproporcjonalnie duzy blad w odpowiedzi
"""