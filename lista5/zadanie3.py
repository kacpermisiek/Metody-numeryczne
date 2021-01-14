from scipy.interpolate import PchipInterpolator
import matplotlib.pyplot as plt
import numpy as np


xs = np.array([0.2, 2.0, 20.0, 200.0, 2000.0, 20000.0])
ys = np.array([103.0, 13.9, 2.72, 0.8, 0.401, 0.433])


pch = PchipInterpolator(xs, ys)

results = [pch(5.5), pch(5000)]
print(f"f(5.5) = {results[0]}\nf(5000) = {results[1]}")

plt.scatter(xs, ys)
x_range = np.arange(0.2, 20000, 0.001)

plt.scatter([5.5, 5000], results)
plt.plot(x_range, pch(x_range))
plt.xscale('log', base=2)
plt.yscale('log', base=2)
plt.grid()
plt.show()