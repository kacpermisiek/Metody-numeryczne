from scipy.integrate import simps
from matplotlib import pyplot as plt
import numpy as np


def f(x):
    return np.cos(2 * np.arccos(x))


a = -1
b = 1

knots = [3, 5, 7]

for s in knots:
    zx = np.linspace(a, b, num=s, endpoint=True)
    zy = f(zx)
    ws = simps(zy, zx)
    print(f"Dla {s} wezlow funkcja: {ws}")
