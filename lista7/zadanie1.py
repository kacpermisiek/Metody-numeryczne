from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


def f1(t, y):
    return np.sin(t*y)


y0 = [2, 2.5, 3, 3.5]

for el in y0:
    wynik = solve_ivp(f1, [0, 6], [el], atol=1e-12, rtol=1e-9)
    print('\nWyniki dla y0 równego', el)
    # print('t=', wynik.t)
    # print('y=', wynik.y[0])
    plt.plot(wynik.t, wynik.y[0])

plt.legend(['y0=2', 'y0=2.5', 'y0=3', 'y0=3.5'])
plt.grid()
plt.show()
