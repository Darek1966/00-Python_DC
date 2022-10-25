
import time # Zaimportuj moduł time

# Zdefiniuj funkcję wrapper_time przyjmującą jako argument inną funkcję: a_function
# W tej funkcji zdefiniuj nową funkcję a_wrapped_function, która:
# jako argument przyjmuje wszystkie możliwe argumenty
# w zmiennej time_start zapamięta aktualny czas
# w zmiennej v zostanie zapamiętany wynik wywołania funkcji a_function (wywołując ją należy przekazać wszystkie potrzebne parametry)
# w zmiennej time_stop zapamiętaj aktualny czas
# Wyświetl komunikat o treści "Funkcja <tutaj_nazwa_funkcji> wykonana w czasie <tutaj wynik odejmowania time_stop - time_start>"
# zwróć zmienną v
def wrapper_time(a_function):

        def a_wrapped_function(*args, **kwargs):            
            time_start = time.time()
            v = a_function(*args, **kwargs)
            time_stop = time.time()
            print('>>>>>Function {} executed in {}'.format(a_function.__name__, time_stop - time_start))
            return v
# Zwróć funkcję a_wrapped_function   
        return a_wrapped_function

# Oto funkcja, dla której trzeba stworzyć wrapper:  (wrapper stwożony wyżej)
def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

# print(get_sequence(5))
# Do wrapper_get_sequence przypisz wynik funkcji wrapper_time wywołanej z argumentem wskazującym na oryginalną funkcję get_sequence
wrapper_get_sequence = wrapper_time(get_sequence)
# Na moim komputerze wykonanie funkcji z n=18 trwało 3 sekundy, n=19 - 6 sekund, a n=20 - 14 sekund.  
print(wrapper_get_sequence(18))
