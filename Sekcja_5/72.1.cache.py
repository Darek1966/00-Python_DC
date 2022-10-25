
import time
import functools

@functools.lru_cache() # sprawi, że silnia nie będzie liczona za każdym razem od początku, wykorzysta wcześniej obliczony wynik

def Factorial(n):  
    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)
start = time.time()
for i in range(1, 11):     # silnia liczb od 1 do 10
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()
print('Execution time', stop - start)
# szybko liczy - ok. 1 sek.

print(Factorial.cache_info()) # jak działa cache - jak wykorzystuje swoją pamięć
'''
start = time.time()
for i in range(1, 11):     # silnia liczb od 1 do 10
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()
print('Execution time', stop - start)
'''
