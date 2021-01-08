import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve


# Dane poczatkowe
u = 2510    # Predkosc spalin wzgledem rakiety
M_0 = 2.8e6  # masa rakiety w momencie oderwania od Ziemi
m = 13.3e3  # szybkosc zuzycia paliwa
g = 9.81    # przyspieszenie ziemskie


# Funkcja do wykresu
def f(t):
    return u * np.log(M_0/(M_0 - m*t)) - g*t


# Funkcja do obliczen
def fun2(t):
    return u * np.log(M_0 / (M_0 - m * t)) - g * t - 335


x = np.linspace(0, 100, 1000)
y = []

for i in x:
    y.append(f(i))

# Znajdowanie miejsca zerowych funkcji fun2
solve = fsolve(fun2, np.array([70]))
print(f'Czas do osiegniecia predkosci dzwieku: {solve[0]:.3}s')


# Tworzenie wykresu
plt.plot(x, y, color='black')
plt.scatter(solve, f(solve), color='red')
plt.grid()
plt.xlabel('t[s]')
plt.ylabel('V[m/s]')
plt.show()
