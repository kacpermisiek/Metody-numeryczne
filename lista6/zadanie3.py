from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

x = np.array([-2.2, -0.3, 0.8, 1.9])
y = np.array([-15.18, 10.962, 1.92, -2.04])
x_0 = 0.0


cs = CubicSpline(x, y)
print(f"f'(0) = {cs(x_0, 1)}")
print(f"f''(0) = {cs(x_0, 2)}")

x_range = np.linspace(-2.2, 1.9, 1000, endpoint=True)
y_range = cs(x_range)
y_range_1prim = cs(x_range, 1)
y_range_2prim = cs(x_range, 2)

plt.plot(x_range, y_range, label='f(x)')
plt.scatter(x, y)

plt.plot(x_range, y_range_1prim, label="f'(x)")
plt.plot(x_range, y_range_2prim, label="f''(x)")

plt.plot(0, cs(x_0, 1), 'o', label="f'(0)")
plt.plot(0, cs(x_0, 2), 'o', label="f''(0)")

plt.grid()
plt.legend()
plt.show()

