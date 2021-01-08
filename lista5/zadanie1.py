import numpy as np
import matplotlib.pyplot as plt


def polynomial(x, y):
    n = np.shape(x)[0]  # "wysokość" piramidy
    piramida = np.zeros([n, n])  # stworzenie pola do piramidy

    # wpisanie w piramidę wartości y w 1 kolumnie
    for i in range(np.shape(piramida)[1]):
        piramida[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            licznik = (piramida[i + 1][j - 1] - piramida[i][j - 1])
            mianownik = (x[i + j] - x[i])
            piramida[i][j] = licznik / mianownik
    return piramida[0]  # zwróć tylko 1 wiersz, w którym sa wyniki


def plot_function(x_list, function):    # Funkcja do rysowania funkcji
    y_list = []

    for j in range(len(x_list)):
        y_list.append(0)

        for i in range(len(function)):
            y_list[j] += function[i] * x_list[j] ** i

    plt.plot(x_list, y_list)
    plt.grid()


def print_values(result):

    m = len(result)
    result = result[::-1]
    print("y = ", end='')

    for i in range(m):

        if result[i] < 0 or i == 0:
            if i == m-1:
                print(f"{result[i]} ", end='')
            else:
                print(f"{result[i]}x^{m-i-1} ", end='')
        else:
            if i == m-1:
                print(f"+{result[i]} ", end='')
            else:
                print(f"+{result[i]}x^{m-i-1} ", end='')


x = np.array([0, 3, 6])
y = np.array([1.225, 0.905, 0.652])
x_range = np.arange(-10, 11)

wynik = polynomial(x, y)
print_values(wynik)
plot_function(x_range, wynik)
plt.scatter(x, y)

plt.show()


