from scipy.integrate import dblquad
import numpy as np


def fxy(x, y):
    return np.sin(np.pi * x) * np.sin(np.pi * (y - x))
# argument - calkowanie wewnetrzne


# dolna granica calki wewnetrznej
def gfxy(x):
    return 0


# gorna granica calki wewnetrznej
def hfxy(x):
    return x


# Result from Wolframalpha
Iex1 = -0.2026423672846755428877589264194552778087175493444930976912180637883462419244708823824185478512436752
wdxy = dblquad(fxy, 1, 0, gfxy, hfxy)

print("%18.15f  %12.5e" % (wdxy[0], np.abs(Iex1-wdxy[0])))
