from scipy.misc import derivative
import numpy as np


def f(x):
    return np.log(np.tanh(x / (x**2 + 1)))


x_0 = 0.2

f_prim = derivative(f, x_0, 1e-6, 1)
f_2prim = derivative(f, x_0, 1e-6, 2)
f_3prim = derivative(f, x_0, 1e-6, 3, order = 7)

print(f"f'(0.2) = {f_prim}")
print(f"f''(0.2) = {f_2prim}")
print(f"f'''(0.2) = {f_3prim}")

