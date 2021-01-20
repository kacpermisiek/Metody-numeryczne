import matplotlib.pyplot as plt
import numpy as np

h = np.array([0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150])
ro = np.array([1.0, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741])

z = np.polyfit(h, ro, 2)
p = np.poly1d(z)
x_range = np.linspace(0, 10, 1000)

plt.plot(x_range, p(x_range), label='wykres funkcji')

print(f'p(10.5km) = {p(10.5)}')


xp = np.linspace(0, 10, 100)
plt.plot(h, ro, '.', xp, p(xp))
plt.grid()
plt.show()


