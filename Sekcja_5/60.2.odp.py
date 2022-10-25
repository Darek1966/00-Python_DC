'''
A teraz drugi wariant z wykorzystaniem dekorowania funkcji. 
Skopiuj poprzednie rozwiązanie i  dokonaj w nim modyfikacji:
'''
import time
import functools   # Zaimportuj moduł functools
 
def wrapper_time(a_function):
    
    def a_wrapped_function(*args, **kwargs):
        
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print(">>>>>Function {} executed in {}".format(a_function.__name__, time_stop - time_start))
        
        return v
    
    return a_wrapped_function

# Oznacz funkcję get_sequence dekoratorem wskazującym na wrapper_time
@wrapper_time
def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v
# Wywołaj funkcję get_sequence np. tak:
print(get_sequence(3))
# Wywołanie funkcji rekurencyjnej powoduje teraz wielokrotne uruchomienie wrappera wielokrotnie (!!)
