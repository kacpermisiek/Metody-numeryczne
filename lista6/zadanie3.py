from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

x = np.array([-2.2, -0.3, 0.8, 1.9])
y = np.array([-15.18, 10.962, 1.92, -2.04])
x_0 = 0.0


cs = CubicSpline(x, y)
print(f"f'(0) = {cs(x_0, 1)}")
print(f"f'(0) = {cs(x_0, 2)}")
