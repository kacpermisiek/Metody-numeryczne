from scipy import optimize as o
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return (2 * x ** 4) + (24 * x ** 3) + (61 * x ** 2) - (16 * x) + 1


def show_plot(a, b, d):
    y = []
    x = np.arange(a, b, d)
    for i in x:
        y.append(f(i))

    plt.style.use('seaborn')
    plt.plot(x, y)




show_plot(-100, 100, 0.1)  # 1 wykres, podglad jak wygladac bedzie funkcja
show_plot(-10, 2.5, 0.0001)  # 2 wykres, przyblizenie na miejsca zerowe
show_plot(0.12, 0.125, 0.0000001)   # 3 wykres, przyblizenie na 2 miejsca zerowe bardzo blisko siebie



root_list = [o.ridder(f, -9, -8), o.ridder(f, -5, -4), o.ridder(f, 0.121, 0.122), o.ridder(f, 0.123, 0.124)]

y_list = np.zeros(4)

plt.scatter(root_list, y_list)

print(root_list)

plt.show()

