'''
https://pl.wikipedia.org/wiki/Liczba_doskona%C5%82a

Liczba doskonała – liczba naturalna, która jest sumą wszystkich swych dzielników właściwych (to znaczy od niej mniejszych).
No to poszukajmy liczb doskonałych w przedziale od 1 - 10000. Oto funkcja wyznaczająca dzielniki liczby:
'''
import itertools as it
 
 
def get_factors(x):
 
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list
 
# Przetestuj funkcję wyznaczając dzielniki liczby 20
print(get_factors(20))
 
# W zmiennej candidate_list zapisz liczby od 1 do 10000 (przetwarzanie będzie trochę trwało, więc możesz zacząć od mniejszej wartości np. 100) 
candidate_list = list(range(1, 10001))
'''
W zmiennej filtered_list zapisz tylko te liczby z candidate_list, które są doskonałe
skorzystaj z funkcji filterfalse z modułu itertools
na każdym liczbie z listy candidate_list
sprawdzaj, czy suma liczb z listy zwróconej przez get_factors dla tej liczby jest różna od tej liczby
wynik skonwertuj do listy
'''
filtered_list = list(it.filterfalse(lambda x: x != sum(get_factors(x)),candidate_list))

# Dla każdego elementu z listy filtered_list wyświetl tą liczbę oraz listę jej dzielników (ponownie wywołaj get_factors)
for p in filtered_list:
    print(p, get_factors(p))

