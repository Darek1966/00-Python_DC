
from numpy import product

listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []         
for a in listA:
    for b in listB:
        product.append((a, b))
print(product)

product = [(a, b) for a in listA for b in listB]
print(product)

product = [(a, b) for a in listA for b in listB if a % 2 == 1 and b % 2== 0]
print(product)


product = {a : b for a in listA for b in listB if a % 2 == 1 and b % 2== 0}
print(product)

# generator (bardzo dużo obiektów)
gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2== 0)
print(gen)    # <generator object <genexpr> at 0x000001AF97312180>

print(next(gen)) # (1, 0)
print(next(gen)) # (1, 2)
print(next(gen)) # (1, 4)

print('-' *30)

for x in gen:
    print(x)
'''  
(1, 0)
(1, 2)
(1, 4)
(3, 0)
(3, 2)
(3, 4)
(5, 0)
(5, 2)
(5, 4)
'''
print('-' *30)

for x in gen:
    print(x)

print('*'*30)
# nowy generator
gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2== 0)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print('koniec generowania')
        break
