from scipy.integrate import quad
import numpy as np


def f(x):
    return (np.log(x)) / (x**2 - 2*x + 2)


qq = quad(f, 1, np.pi)

print(qq)