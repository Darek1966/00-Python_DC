
import math

# Utwórz pustą listę argument_list
argument_list = []

'''
Napisz pętlę, która do listy argument_list doda
100 wartości zaczynając od zera
gdzie każda kolejna jest o 0.1 większa od poprzedniej
'''
for i in range (100):
    argument_list.append(i/10)

'''
Poproś użytkownika o wprowadzenie wzoru. Wzór zapisz w zmiennej formula. 
Użytkownik wprowadzając ten wzór powinien skorzystać ze zmiennej x do tego aby oznaczyć argument funkcji
'''
formula = input("Wprowadź formułę, użyj „x” jako argumentu: ")

'''
 Dla każdego elementu x z listy argument_list oblicz wartość funkcji wprowadzonej przez użytkownika i wyświetl jej wynik
'''
for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))
    