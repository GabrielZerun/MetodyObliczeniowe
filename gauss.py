

#Zaimportowanie biblioteki numpy i sys - numpy jest używany do wykonywania operacji na macierzach, a sys jest używany do wyjścia z programu w przypadku wystąpienia błędu.
#Pobranie od użytkownika liczby zmiennych i przypisanie jej do zmiennej "n".
#Utworzenie macierzy "a" o rozmiarze "n x n+1" za pomocą funkcji "np.zeros()".
#Utworzenie macierzy "x" o rozmiarze "n" za pomocą funkcji "np.zeros()".
#Wprowadzenie współczynników macierzy z uzupełnieniami za pomocą pętli for i przypisanie ich do macierzy "a".
#Rozpoczęcie eliminacji Gaussa poprzez wykonanie pętli for od 0 do "n-1" dla każdego elementu na głównej przekątnej macierzy "a".
# Jeśli wartość elementu na przekątnej jest równa 0, program kończy się z wyjściem błędu. Następnie dla każdego elementu poniżej elementu na przekątnej, obliczany jest stosunek między tym elementem a elementem na przekątnej i odejmowany od wiersza na przekątnej, aby uzyskać wartość 0 dla tego elementu.
# Ten proces powtarza się dla każdej kolumny macierzy "a".
#Rozpoczęcie podstawiania wstecznego za pomocą pętli for od "n-1" do 0. Pierwszy element "x[n-1]" jest obliczany jako wartość na prawo od równości dla ostatniego wiersza macierzy "a" podzielona przez wartość elementu na przekątnej. Następnie dla każdego elementu powyżej "x[n-1]", jego wartość jest obliczana jako wartość na prawo od równości minus sumy iloczynów elementów na poziomych pozostałych elementów na przekątnej i ich odpowiadających "x". W końcu, ta suma jest dzielona przez wartość elementu na przekątnej.
#Wyświetlenie wyników za pomocą pętli for, która wyświetla wartości każdej zmiennej "x" wraz z jej numerem indeksu.

import numpy as np
import sys

#liczba zmiennych
n = int(input('Podaj ilosc zmiennych: '))

# macierz rozmiaru: n x n+1

a = np.zeros((n,n+1))

# macierz rozmiaru: n
x = np.zeros(n)

# wspolczynniki macierzy uzupelnien
print('Podaj wspolczynniki macierzy uzupelnien:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Metoda eliminacji Gaussa
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Dzielenie przez 0!')

    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]

        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]

    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]

    x[i] = x[i]/a[i][i]

print('\n Wynik to: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]))