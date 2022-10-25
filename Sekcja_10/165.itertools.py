
from calendar import month
import itertools
import operator
from unittest import result

data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul)   # operator.mul - mnożenie
for each in result:
    print(each)

print('-' * 20)

data = [1, 2, 13, 4, 5]
result = itertools.accumulate(data, max)    # wartość maksymalna
for each in result:
    print(each)

print('-' * 20)

for i in itertools.count(10, 3):    # od 10 do 22 co 3        
    print(i)
    if i > 20:
        break

print('-' * 20)
'''
months =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for m in itertools.cycle(months):   # przechodzi przez listę miesięcy w nieskończoność
    print(m)
'''
print('-' * 20)

colors_basic = ['read', 'yellow', 'blue']
colors_mix = ['green', 'orange', 'violet']
result = itertools.chain(colors_basic, colors_mix)  # łączy listy
for each in result:
    print(each)

print('-' * 20)

cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
selections = [True, False, True, False]
result = itertools.compress(cars, selections)   # zwraca tam gdzie True
for each in result:
    print(each)

print('-' * 20)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.dropwhile(lambda x: x<5, data)   # wyświetla od 5 z listy 
for each in result:
    print(each)

print('-' * 20)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.filterfalse(lambda x: x<5, data)   # opuszcza elementy mniejsze od 5
for each in result:
    print(each)

print('-' * 20)

months =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
result = itertools.islice(months, 6, 8)     # wybiera z listy 6 i 8 pozycję
for each in result:   
    print(each)

print('-' * 20)

spades = ['Hearts', 'Tiles', 'Clovers', 'Pikes']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
result = itertools.product(spades, figures) # łączy elementy z pierwszego zbioru z elementami drugiego zbioru
for each in result:
    print(each)

print('-' * 20)

for i in itertools.repeat('tell me more', 5):   # generuje napis 5 razy
    print(i)

print('-' * 20)

data = [(1, 2), (3, 4), (5, 6)]
result = itertools.starmap(operator.add, data)  # dodaje elementy w nawiasach ( )
for each in result:
    print(each)

print('-' * 20)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.takewhile(lambda x: x<5, data)   # pobiera elementy mniejsze od 5
for each in result:
    print(each)

print('-' * 20)

cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
cars1, cars2 = itertools.tee(cars)      # tworzymy dwa iteretory: cars1 i cars2

for each in cars1:
    print(each)
print('-----------------')
for each in cars2:
    print(each)

print('-' * 20)

months =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plan = ['busy', 'busy', 'busy', 'busy', 'busy', 'busy', 'free', 'free']
result = itertools.zip_longest(months, plan, fillvalue='unknow')     # łączy elementy z listy - problem miesięcy nieokreślonych
for each in result:   
    print(each)
