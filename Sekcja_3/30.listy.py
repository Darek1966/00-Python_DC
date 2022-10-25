
from numpy import product

listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []          # zwykły przykład
for a in listA:
    for b in listB:
        product.append((a, b))
print(product)

product = [(a, b) for a in listA for b in listB] # to samo - zagnieżdżone
print(product)

# pierwsza lista - nieparzyste, droga lista - parzyste
product = [(a, b) for a in listA for b in listB if a % 2 == 1 and b % 2== 0]
print(product)

# zapis dla słownika {} - wartości tylko dla klucza się zmieniają
# wartości dla klucza sie podmieniają, pozostaje tylko ostatnia
product = {a : b for a in listA for b in listB if a % 2 == 1 and b % 2== 0}
print(product)
