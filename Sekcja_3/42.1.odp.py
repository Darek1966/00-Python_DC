
import math
import time

# Utwórz listę ze wzorami:
formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
 
 # Przygotuj listę argumentów (jeżeli pętla trwa zbyt długo zmniejsz ilość elementów na tej liście):
argument_list = []
for i in range (1000000):
    argument_list.append(i/10)

# Dla każdej formuły z listy formuł:
for formula in formulas_list:
# Utwórz pustą listę results_list = []
    results_list = []
# Wyświetl formułę nad jaką teraz pracuje pętla
    print("Formula {}".format(formula))
# W zmiennej start zapisz czas bieżący
    start = time.time()
# Dla każdego argumentu z listy argument_list wylicz wartość formuły i dodaj go do listy wyników results_list
    for x in argument_list:
        results_list.append(eval(formula))
# Wyświetl informację o minimalnej i maksymalnej wyliczonej wartości znajdującej się w liście results list
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
# W zmiennej stop zapisz czas bieżący
    stop = time.time()
# Wyświetl informacje o czasie trwania obliczeń
    print("Calculation time: {}".format(stop - start))
 
# Przetestuj skrypt

# Skopiuj pętlę z punktu (3) i dokonaj modyfikacji:   
for formula in formulas_list:
 
    results_list = []
    print("Formula {}".format(formula))
    start = time.time()

# Przed pętlą liczącą wartość formuły wstaw instrukcję zapamiętującą w zmiennej compiled_formula skompilowany kod
    compiled_formula = compile(formula, formula, 'eval')

# W pętli liczącej wartość formuły skorzystaj z prekompilowanego kodu ze zmiennej compiled_formula
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
# Uruchom program i porównaj czasy przed i po optymalizacji
    print("Calculation time: {}".format(stop - start))
