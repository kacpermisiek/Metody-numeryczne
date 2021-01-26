import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np


def f(x):
    return np.log(np.tanh(x / (x**2 + 1)))


x_0 = 0.2


f_prim = derivative(f, x_0, 1e-6, 1)
f_2prim = derivative(f, x_0, 1e-6, 2)
f_3prim = derivative(f, x_0, 1e-4, 3, order=7)


print(f"f'(0.2) = {f_prim}")    # 4.50353 wg Wolframalpha
print(f"f''(0.2) = {f_2prim}")   # -27.1412 wg Wolframalpha
print(f"f'''(0.2) = {f_3prim}")  # 254.61 wg Wolframalpha

x_range = np.linspace(0.1, 1, 1000, endpoint=True)
x_range2 = np.linspace(0.2, 1, 100, endpoint=True)


y_1prim = derivative(f, x_range, 1e-6, 1)
y_2prim = derivative(f, x_range, 1e-6, 2)
y_3prim = derivative(f, x_range2, 1e-4, 3, order=7)

plt.scatter([x_0 for i in range(3)], [f_prim, f_2prim, f_3prim])
plt.plot(x_range, y_1prim, label="f'(x)")
plt.plot(x_range, y_2prim, label="f''(x)")
plt.plot(x_range2, y_3prim, label="f'''(x)")
plt.grid()
plt.legend()
plt.show()