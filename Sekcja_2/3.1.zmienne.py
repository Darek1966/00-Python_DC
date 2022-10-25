'''
a = 10
b = 10
c = 10

print(a, b, c)
print(id(a), id(b), id(c))

a = 10 + 20 # id a zmieni się

print(a, b, c)
print(id(a), id(b), id(c))
'''


a = [1, 2, 3]
b = a
c = a

a.append (4)

 # inna wersja
# a += [4]  # id a taki sam jak b, c

print(id(a), id(b), id(c)) # id taki sam
print(a, b, c)


'''
x = 10
# y = 10

# y = 10 +1 -1 # id taki sam

y = 10 + 1234567890123453451234567890 - 1234567890123453451234567890 # taki sam id

print (id(x), id(y))
'''