from scipy.interpolate import CubicSpline
import scipy.optimize as o
import matplotlib.pyplot as plt
import numpy as np


def f_prim(x, cs):
    return cs(x, 1)


def f(u):
    return cs(u)


global x
x = np.array([1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3])

global y
y = np.array([-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334])

global cs
cs = CubicSpline(x, y)

plt.scatter(x, y)
x_range = np.arange(1, 3, 0.001)

plt.plot(x_range, cs(x_range), label='f(x)')
plt.plot(x_range, cs(x_range, 1), label="f'(x)")

result = f_prim(2.1, cs)
print(f"y'(2.1)= {result}")

root_list = [o.ridder(f, 1.2, 1.3), o.ridder(f, 2.1, 2.2), o.ridder(f, 2.8, 2.9)]

print(f"Miejsca zerowe funkcji f(x): {root_list}")


plt.scatter(2.1, result, label='f\'(2.1)')
plt.scatter(root_list, np.zeros(len(root_list)), label='f(x)=0')
plt.legend()
plt.grid()
plt.show()
