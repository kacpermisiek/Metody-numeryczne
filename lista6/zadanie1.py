import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np


def f(x):
    return np.log(np.tanh(x / (x**2 + 1)))


""""
def f_1prim(x):
    return derivative(f, x, 1e-6, 1)


def f_2prim(x):
    return derivative(f, x, 1e-6, 2)


def f_3prim(x):
    return derivative(f, x_0, 1e-4, 3, order=7)
"""

x_0 = 0.2


f_prim = derivative(f, x_0, 1e-6, 1)
f_2prim = derivative(f, x_0, 1e-6, 2)
f_3prim = derivative(f, x_0, 1e-4, 3, order=7)



print(f"f'(0.2) = {f_prim}")    # 4.50353 wg Wolframalpha
print(f"f''(0.2) = {f_2prim}")   # -27.1412 wg Wolframalpha
print(f"f'''(0.2) = {f_3prim}")  # 254.61 wg Wolframalpha
""""

x_range = np.linspace(0, 1, 1000)
y_range_1prim, y_range_2prim, y_range_3prim = [], [], []

for i in x_range:
    try:
        y_range_1prim.append(f_1prim(i))
        y_range_2prim.append(f_2prim(i))
        y_range_3prim.append(f_3prim(i))
    except RuntimeWarning:
        print('xd')


plt.plot(x_range, y_range_1prim)
plt.scatter(x_0, f_1prim(x_0))
plt.show()
"""