from scipy.special import roots_legendre
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return ((np.cos(x) - np.exp(x)) / (np.sin(x)))


#  Result from integral-calculator.com
#  Blad = 2.494217855285153e-14
Iex1 = -2.24659172072861

a = -1
b = 1
s = 2

knots = [c*2 for c in range(1, 10)]


for n in knots:
    xi, ai = roots_legendre(n)
    I_n = 0
    for i in range(len(ai)):
        I_n += (b-a)/2*ai[i] * f((b+a)/2 + (b-a)/2*xi[i])
    print("%4d  %18.15f  %12.5e" % (n, I_n, np.abs(Iex1-I_n)))


x_range = np.linspace(-1, 1, 1000, endpoint=True)
y_range = f(x_range)
plt.fill_between(x_range, f(x_range), 0)
plt.plot(x_range, y_range, '-k')
plt.axhline(color='black')
plt.show()