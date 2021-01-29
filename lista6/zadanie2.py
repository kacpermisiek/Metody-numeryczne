from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
y = np.array([0.0, 0.078348, 0.13891, 0.192916, 0.244981])
x_0 = 0.2

# Do wykresu
f1 = interpolate.interp1d(x, y, kind='quadratic')
x_range = np.arange(0, 0.4, 0.001)
y_range = f1(x_range)


p1 = interpolate.lagrange(x, y)
derivative = np.polyder(p1)

y_range_prim = derivative(x_range)

print(f"f'(0.2) = {derivative(x_0)}")


plt.scatter(x, y)
plt.plot(x_range, y_range, label='f(x)')
plt.plot(x_range, y_range_prim, label='f\'(x)')
plt.scatter(x_0, derivative(x_0))


plt.legend()
plt.grid()
plt.show()
