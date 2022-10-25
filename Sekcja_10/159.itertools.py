
import itertools as it
from unittest import result

# myList = ['a', 'b', 'c', 'd']
'''
for combination in it.combinations(myList, 3):
    print(combination)
'''
'''
for combination in it.permutations(myList, 3):
    print(combination)   
'''
'''
for combination in it.combinations_with_replacement(myList, 3):
    print(combination)   
'''
'''
money = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

results = []

for i in range(1, 101):
    for combination in it.combinations(money, i):
        if sum(combination) == 100:
            results.append(combination)

results = set(results)

for result in results:
    print(result)
'''

money = [50, 20, 10]

for i in range(1, 101):
    for combination in it.combinations_with_replacement(money, i):
        if sum(combination) == 100:
            print(combination)
            
