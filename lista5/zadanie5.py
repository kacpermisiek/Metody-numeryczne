import matplotlib.pyplot as plt
import numpy as np

x = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
y = np.array([6.008, 15.772, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828])

x_range = np.arange(1, 4, 0.001)

poly1, tres1, trank1, tsv1, trcond1 = np.polyfit(x, y, 1, full=True)
fun1 = np.poly1d(poly1)
y1 = fun1(x_range)

poly2, tres2, trank2, tsv2, trcond2 = np.polyfit(x, y, 2, full=True)
fun2 = np.poly1d(poly2)
y2 = fun2(x_range)

print(f"suma kwadratow odchylenia od funkcji liniowa: {tres1}")
print(f"suma kwadratow odchylenia od funkcji kwadratowa: {tres2}")

print("\nODP. Lepiej dopasowana jest funkcja kwadratowa ")

plt.scatter(x, y)
plt.plot(x_range, y1, label='linia prosta')
plt.plot(x_range, y2, label='funkcja kwadratowa')
plt.grid()
plt.show()
