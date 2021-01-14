from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import numpy as np


h = np.array([0.0, 3.0, 6.0])
ro = np.array([1.225, 0.905, 0.652])

result = lagrange(h, ro)

print(result)

x_data = np.arange(0, 6, 0.01)
y_data = []

for i in x_data:
    y_data.append(result[0] + i*result[1] + i**2 * result[2])

plt.scatter(h, ro)
plt.plot(x_data, y_data)
plt.grid()
plt.show()
