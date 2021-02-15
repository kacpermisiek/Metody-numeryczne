import matplotlib.pyplot as plt
from scipy import linalg
import numpy as np

R_range = np.linspace(0, 10, 100, endpoint=True)
b = np.array([0, 120, 120])
I2_list = []


for R_x in R_range:
    a = np.array([[1, -1, -1],
                  [3.5, R_x, 0],
                  [3.5, 0, 6.6]])

    x = linalg.solve(a, b)
    I2_list.append(x[1])


Power_list = [I2_list[i]**2 * R_range[i] for i in range(len(I2_list))]
P_max_idx = Power_list.index(max(Power_list))
print(f"Maksymalna moc wydzialana na oporniku: {round(Power_list[P_max_idx], 2)} W")
print(f"Wartosc oporu R_x, przy ktorej moc wydzielana jest najwieksza: {round(R_range[P_max_idx], 2)} Ω")

plt.plot(R_range, Power_list, 'ro-', label=r"P($R_x$)")
plt.scatter(R_range[P_max_idx], Power_list[P_max_idx], label=r'$P_{max}$', linewidths=7)
plt.grid()
plt.xlabel("R [Ω]", fontsize=20)
plt.ylabel("P [W]", fontsize=20)
plt.title(r'Wykres mocy wydzielanej przez opornik $R_x$ w zaleznosci od wartosci rezystancji opornika $R_x$', fontsize = 30)
plt.legend(fontsize=40)

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
