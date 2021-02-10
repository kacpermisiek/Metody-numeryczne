from scipy.integrate import quad
import numpy as np


def fun(x, x0):#x-theta x0-parametr
    return 1/np.sqrt(1-np.sin(x0/2)**2*np.sin(x)**2)


x0 = [np.pi/12, np.pi/6, np.pi/4] #kąty w radianach


for x in x0:
    cal = quad(fun, 0, np.pi/2, args=x)
    print('%8.2f %18.12f %18.12f' % (x*180/np.pi, cal[0], (np.pi/2.0)-cal[0]))
