from scipy.integrate import simps
from matplotlib import pyplot as plt
import numpy as np


def f(x):
    return np.cos(2 * np.arccos(x))


a = -1
b = 1

print("nr wezla  wartosc")

knots = [3, 5, 7]

for i in knots:
    zx = np.linspace(a, b, num=i, endpoint=True)
    zy = f(zx)
    ws = simps(zy, zx)
    print("%6d  %18.15f" % (i, ws))

