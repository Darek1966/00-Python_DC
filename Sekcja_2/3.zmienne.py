
nap = 'Hallo Word'

nap2 = nap + "!!"

print(nap2)
print(nap + nap2)
print(type(nap), type(nap2))
print(id(nap), id(nap2))

nap2 = nap2[:-2]

print(nap2)
print(nap + nap2)
print(type(nap), type(nap2))
print(nap is nap2)
print(id(nap), id(nap2))
