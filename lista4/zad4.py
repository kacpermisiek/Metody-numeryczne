import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def funkcja12(dane):
    x = dane[0]
    y = dane[1]
    return [x + np.exp(-x) + y ** 3,
            x ** 2 + 2 * x * y - y ** 2 + np.tan(x)]


def funkcja1(x):
    return np.cbrt(-np.exp(-x) - x)  # Przeksztalcenie funkcji do postaci y = ...


def funkcja2(x):
    return [x - np.sqrt(2 * x**2 + np.tan(x)),
            x + np.sqrt(2 * x**2 + np.tan(x))]  # Funkcje 2 trzeba rozbic na 2 przypadki, poniewaz bylo y^2


zasieg = np.arange(-2, 2, 0.000001)

#Rysowanie okregu
circle = plt.Circle((0, 0), 2, color='b', fill=False)
ax = plt.gca().add_artist(circle)

# Rysowanie funkcji
plt.plot(zasieg, funkcja1(zasieg), color='black')
plt.plot(zasieg, funkcja2(zasieg)[0], color='green')
plt.plot(zasieg, funkcja2(zasieg)[1], color='green')

# Z wykresu odczytujemy 3 miejsca gdzie przecinaja sie obydwie funkcje (kolor zielony oraz czarny
solves = [[-1.2, -1.3], [-0.7, -1.1], [1.2, -1.1]]

wynik = []

for x in solves:
    x_i = optimize.root(funkcja12, x)
    if x_i.success:
        if np.sqrt(x_i.x[0]**2 + x_i.x[1]**2) <= 4:
            wynik.append([x_i.x[0], x_i.x[1]])

print("Pierwiastki ukladu rownan:\n X       Y")
for x in wynik:
    plt.plot(x[0], x[1], 'o')
    print(f'{x[0]:.6}   {x[1]:.6}')


plt.axis((-5, 5, -5, 5))
plt.grid()
plt.show()
