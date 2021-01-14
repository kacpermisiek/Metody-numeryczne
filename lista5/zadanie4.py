import matplotlib.pyplot as plt
import numpy as np

xs = np.array([0.2, 2.0, 20.0, 200.0, 2000.0, 20000.0])
ys = np.array([103.0, 13.9, 2.72, 0.8, 0.401, 0.433])

plt.scatter(xs, ys)

f = np.polyfit(xs, ys, 1)
f1 = np.poly1d(f)

print(f1)

Re_x = [5.5, 5000]
Re_y = [f1(Re_x[0]), f1(Re_x[1])]


x_range = np.arange(0.2, 20000, 0.001)

print(f"f(5.5) = {Re_y[0]}\nf(5000) = {Re_y[1]}")

plt.scatter(Re_x, Re_y)
plt.plot(x_range, f1(x_range))
plt.xscale('log', base=2)
plt.yscale('log', base=2)
plt.grid()
plt.show()