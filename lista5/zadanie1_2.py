import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = [0, 3, 6]
y = [1.225, 0.905, 0.652]
f = interpolate.interp1d(x, y, kind="quadratic") # Dopasowywanie funkcji do punktów
xnew = np.arange(0, 6, 0.1)
ynew = f(xnew)
plt.plot(x, y, "o", xnew, ynew, '-')
plt.grid()
plt.show()