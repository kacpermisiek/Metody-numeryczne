import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def rownania(wspolrzedne):
    x = wspolrzedne[0]
    y = wspolrzedne[1]

    return [np.tan(x) - y - 1,
            np.cos(x) - 3 * np.sin(y)]


wynik = []
zasieg = np.arange(0, 1.51, 0.01)


for i in zasieg:
    for j in zasieg:
        f_ij = optimize.root(rownania, np.array([i, j]))

        if f_ij.success:
            if 0 <= round(f_ij.x[0], 4) <= 1.5 and [round(f_ij.x[0], 4), round(f_ij.x[1], 4)] not in wynik:
                wynik.append([round(f_ij.x[0], 4), round(f_ij.x[1], 4)])

print(wynik)

y = np.tan(zasieg) - 1
plt.plot(zasieg, y)

for i in range(0, 3):
    plt.plot(zasieg, ((2 * np.pi * i) + np.arcsin(np.cos(zasieg) / 3)))

for i in range(0, 2):
    plt.plot(zasieg, ((2 * np.pi * i) - np.arcsin(np.cos(zasieg) / 3) + np.pi))

for i in range(0, 5):
    plt.scatter(wynik[i][0], wynik[i][1])

plt.show()




