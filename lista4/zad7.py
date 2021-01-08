from sympy import Symbol, solve
import numpy as np
import matplotlib.pyplot as plt

#   Obliczenie rowniania

x = Symbol('x')
eq1 = x**4 + (5 + 1j) * x**3 - (8 - 5j) * x**2 + (30 - 14j) * x - 84
result = solve(eq1, x)
print("Miejsca zerowe funkcji: ")
print(result)

#   Majac miejsca zerowe mozemy przedstawic nasza funkcje jako y = (x + 7) * (x - 2) (x + 3j) * (x - 2j)

def f_real(x):
    return (x + 7) * (x - 2)


def f_imaginary(x):
    return (x + 3) * (x - 2)


x_range = np.arange(-7.5, 4, 0.01)
y_real = []
y_imaginary = []

for x in x_range:
    y_real.append(f_real(x))
    y_imaginary.append(f_imaginary(x))

plt.plot(x_range, y_real, 'g', label='real')
plt.plot(x_range, y_imaginary, 'b', label='imaginary')
plt.legend()

x_roots = [-7, 2, -3, 2]

plt.scatter(x_roots, np.zeros(4), color='red')
plt.grid()
plt.show()
