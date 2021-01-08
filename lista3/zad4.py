import numpy as np


def Gauss(A,b):
    #tworzenie wektora do ktorego zapisywac bedziemy wyniki
    n = len(b)
    x = np.zeros(n,float)

    for k in range(n-1):
        if A[k,k] == 0:#Sprawdzanie czy element diagonali jest zerowy, jesli jest: trzeba wykonac zamiane miejscami wierszy
            for i in range(k+1,n):
                if A[i,k] !=0: #Jesli ten element nie jest rowny zero, zamien wiersze miejscami
                    A[[k,i]] = A[[i,k]]
                    b[[k,i]] = b[[i,k]]
                    break #Przerwanie petli zamiany miejsc wierszy
        #Eliminacja
        for i in range (k+1,n):
            if A[i,k] == 0: continue #Jesli element pod diagonala jest rowny 0, pozostaw go bez zmian
            wspolczynnik = A[k,k] / A[i,k] #Obliczanie wspolczynnika
            for j in range(k,n):
                A[i,j] = A[k,j] - A[i,j] * wspolczynnik #Zerowanie elementu #np. a(2,1) = a(1,1) - a(2,1)*(a(1,1)/a(2,1))
                
            b[i] = b[k] - b[i] * wspolczynnik #Zmiana wartosci elementu b
        
    #Rozwiazywanie ukladu rownan

    x[n-1] = b[n-1] / A[n-1,n-1] #obliczenie wartosci ostatniej zmiennej wektora x

    for i in range(n-2,-1,-1): #Petla dzieki ktorej poznajemy wartosci zmiennych zaczynajac od przedostatniej i konczac na  pierwszej
        tmp = 0 
        for j in range(i+1,n):
            tmp += A[i,j] * x[j]
        x[i] = (b[i] - tmp) / A[i,i]

    return x
    



#Zadanie 1
A = np.array([[-1,1,-4],[2,2,0],[3,3,2]],float)
b = np.array([[0],[1],[0.5]],float)
print(f"Wynik z zadania 1:\n{np.vstack(Gauss(A,b))}\n")

#Zadanie 2
L = np.array([[1,0,0],[3/2,1,0],[1/2,11/13,1]],float)
U = np.array([[2,-3,-1],[0,13/2,(-7)/2],[0,0,32/13]],float)
b = np.array([[1],[-1],[2]],float)
y = Gauss(L,b)
print(f"Zadanie 2 \n Ly=b\ny=\n{np.vstack(y)}\n")
x = Gauss(U,y)
print(f"Ux=y\n x = \n{np.vstack(x)}\n\n")

#Zadanie 3
A = np.array([[0,0,2,1,2],[0,1,0,2,-1],[1,2,0,-2,0],[0,0,0,-1,1],[0,1,-1,1,-1]],float)
b = np.array([[1],[1],[-4],[-2],[-1]],float)
x = Gauss(A,b)
print(f"Wynik z zadania 3:\nx=\n{np.vstack(Gauss(A,b))}\n")
