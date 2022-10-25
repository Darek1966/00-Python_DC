
def Funkcja (what):
    print('Give me', what)

Funkcja('a new car')

NazwaZmiennej = Funkcja
print(type(NazwaZmiennej)) # <class 'function'>

NazwaZmiennej('a new car') # zmienną <NazwaZmiennej> można wywołać funkcję
