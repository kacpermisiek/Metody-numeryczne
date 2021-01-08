import numpy as np
import math
from scipy import optimize
import matplotlib.pyplot as plt

g = 9.81  # grawitacja
h = 2  # wysokosc koszykarza
s = 10  # odleglosc od kosza
H = 3  # wysokosc kosza
beta = 45  # Kat koncowy


def rownania(dane):
    V_0, alfa = dane

    t = 10 / (V_0 * np.cos(np.deg2rad(alfa)))  # przeksztalcone rownanie 1
    # print(t)
    r2 = float(-1 + V_0 * np.sin(np.deg2rad(alfa)) * t - (g * t * t) / 2)  # Rownanie 2
    r3 = float(V_0 * (np.sin(np.deg2rad(alfa)) + np.cos(np.deg2rad(alfa))) - g * t)  # Rownianie 3
    return [r2, r3]


result = optimize.root(rownania, np.array([10, np.radians(beta)]))

V_p = result.x[0]
alfa = result.x[1]

print(f'Predkosc poczatkowa: {round(V_p, 1)} m/s \nKat poczatkowy: {round(alfa, 1)} stopni')

x, y = [], []

for t in np.arange(0.0, 2.0, 0.001):
    x_t = V_p * np.cos(np.deg2rad(alfa)) * t
    y_t = 2 + V_p * np.sin(np.deg2rad(alfa)) * t - ((g * t ** 2) / 2)
    if x_t <= 10:
        x.append(x_t)
        y.append(y_t)
    else:
        print(f"Czas lotu pilki: {round(t,1)} s")
        break

plt.plot([0, 0], [0, 2])
plt.plot([10, 10], [0, 3])
plt.plot(x, y)
plt.ylabel('y[m]')
plt.xlabel('x[m]')
plt.axis('square')
plt.grid()

plt.show()
