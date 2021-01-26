from scipy.special import roots_legendre
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return (np.log(x)) / (x**2 - 2*x + 2)


#  Result from wolframalpha
Iex1 = 0.584942806931287737492018615016497857523136308159081622007882778547741573548617412988719475526195276
a = 1
b = np.pi
s = 2

knots = [2, 4]

for n in knots:
    xi, ai = roots_legendre(n)
    I_n = 0
    for i in range(len(ai)):
        I_n += (b-a)/2*ai[i]*f((b+a)/2+(b-a)/2*xi[i])
    print("%4d  %18.15f  %12.5e" % (n, I_n, np.abs(Iex1-I_n)))


x_range = np.linspace(1, np.pi, 1000, endpoint=True)
y_range = f(x_range)
plt.fill_between(x_range, f(x_range), 0)
plt.plot(x_range, y_range, '-k')
plt.axhline(color='black')
plt.show()