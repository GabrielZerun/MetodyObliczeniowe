
import numpy as np

def iteracje_proste(wspolczynniki, w_wolne, epsilon):
    n = len(wspolczynniki)
    x = np.zeros(n)
    x_prev = np.zeros(n)
    liczba_iteracji = 0

    while(True):
        for i in range(n):
            # Obliczanie sumy zawierającej wszystkie składniki oprócz tego z indeksem i
            suma = np.dot(wspolczynniki[i][:i], x[:i]) + np.dot(wspolczynniki[i][i + 1:], x_prev[i + 1:])

            # Obliczanie wartości xi
            x[i] = (w_wolne[i] - suma) / wspolczynniki[i][i]

        # warunek zakończenia iteracji
        if np.max(np.abs(x - x_prev)) < epsilon:
            break

        x_prev = np.copy(x)
        liczba_iteracji += 1

    return x, liczba_iteracji



wspolczynniki = np.array([[3,1,2], [1,-4,1],[1,2,3] ])
w_wolne = np.array([5, -7, 2])
epsilon = 0.001


wynik, liczba_iteracji = iteracje_proste(wspolczynniki, w_wolne, epsilon)

print("Rozwiązanie:")
print(wynik)
print("Liczba wykonanych iteracji:", liczba_iteracji)



