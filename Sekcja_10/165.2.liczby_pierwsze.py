'''
A teraz coś, czego nie było na lekcji VIDEO: islice
Obiekt islice jest stworzony w oparciu o generator.  
Wiesz, że generatory często przypominają listy, a w listach można się odwoływać do podzbiorów za pomocą operacji cięcia (slice). 
Idea korzystania z operatora islice jest taka, że gerator wygeneruje liczby dopiero w momencie kiedy je wytniesz (operacja slice). 
Załóżmy, że poszukujemy liczb pierwszych do 10000. Do sprawdzenia czy liczba ma dzielniki można by użyć:
'''

import itertools as it
import operator
from unittest import result

def check_if_has_dividers(x):
 
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False
# Zakładając, że chcesz wyświetlić WSZYSTKIE liczby pierwsze do 10000 możesz to zrobić tak:

# not optimal:
prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
print(prime_numbers)

# Zauważ, że komputer przez chwilę musiał to liczyć... Jeśli zechcesz wyświetlić tylko 10 początkowych wartości zrobisz to tak:

print(prime_numbers[:10])

# Mimo tego,  że wyświetlamy tylko 10 początkowych liczb pierwszych i tak najpierw musiały być wyliczone wszystkie. A to trwa.... i tu z pomocą przychodzi islice:

prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
print(list(prime_numbers))

#Zobacz, że inincjując ten obiekt robimy to aż do 10000000. Mimo tego wyniki dostajemy bardzo szybko. 
# Dlaczego? Bo islice skończy generować kolejne liczby kiedy uda mu się zwrócić owe 10. Sprytne! W formie ćwiczenia przepisz/skopiuj ten kod do siebie i zobacz jak to działa.
