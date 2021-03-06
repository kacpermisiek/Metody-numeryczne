from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import numpy as np

R_e = np.array([0.2, 2.0, 20.0, 200.0, 2000.0, 20000.0])
C_d = np.array([103.0, 13.9, 2.72, 0.8, 0.401, 0.433])

lag = lagrange(np.log(R_e), np.log(C_d))

x_range = np.arange(0.1, 25000, 0.1)

R_e_list = [5, 50, 5000]
C_d_list = np.exp(lag(np.log(R_e_list)))

plt.scatter(R_e, C_d, label='Punkty z danych')
plt.scatter(R_e_list, C_d_list, label='Obliczone punkty')
plt.plot(x_range, np.exp(lag(np.log(x_range))))

for i in range(len(R_e_list)):
    print(f"Wartosc Cd dla Re = {R_e_list[i]}  :  {C_d_list[i]}")

plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()
