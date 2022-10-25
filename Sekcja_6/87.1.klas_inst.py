
class Car:     

    numerOfCars = 0   # zmienne na poziomie klasy
    listOfCars = []


    def __init__(self, marka, model, isPoduszkaOk, isLakierOk, isMechOk):
        self.marka = marka         
        self.model = model
        self.isPoduszkaOk = isPoduszkaOk
        self.isLakierOk = isLakierOk
        self.isMechOk = isMechOk
        Car.numerOfCars +=1             # nowy samochód - liczba się zwiększa
        Car.listOfCars.append(self)     # obiekt dodany na listę samochodów


    def JestUszkodzony(self):      
        return not (self.isPoduszkaOk and self.isLakierOk and self.isMechOk)
 
        print('{}   {}'.format(self.marka, self.model).upper())
        print('Poduszka - ok -     {}'.format(self.isPoduszkaOk))
        print('Lakier   - ok -     {}'.format(self.isLakierOk))
        print('Mechanik - ok -     {}'.format(self.isMechOk))
        print('-------------------------------------------')

print("Zmienne na poziomie klasy PRZED utworzeniem instancji:", Car.numerOfCars, Car.listOfCars)
# Zmienne na poziomie klasy PRZED utworzeniem instancji: 0 []

car_1 = Car('Opel', 'Corsa', True, True, True) 
car_2 = Car('Seat', 'Ibiza', True, False, True) 

print("Zmienne na poziomie klasy PO utworzeniu instancji:", Car.numerOfCars, Car.listOfCars)
# Zmienne na poziomie klasy PO utworzeniu instancji: 2 [<__main__.Car object at 0x00000168AE577FD0>, <__main__.Car object at 0x00000168AE577F10>]

print('Identyfikator instancji to:', id(car_1), id(car_2))

print("Sprawdz, czy obiekt nalezy do klasy:", isinstance(car_1, Car)) 
print("Sprawdz, czy obiekt nalezy do klasy za pomocą typu:", type(car_1) is Car) 

print("Sprawdz klase obiektu za pomocą__class__:", car_1.__class__) 

print("Lista atrybutow instancji z wartosciami:", vars(car_1))
print("Lista atrybutow klas z wartosciami:", vars(Car))

print("Lista atrybutow instancji z wartosciami:", dir(car_1))
# Lista atrybutow instancji z wartosciami: ['JestUszkodzony', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'isLakierOk', 'isMechOk', 'isPoduszkaOk', 'listOfCars', 'marka', 'model', 'numerOfCars']
print("Lista atrybutow klas z wartosciami:", dir(Car))
# Lista atrybutow klas z wartosciami:      ['JestUszkodzony', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'listOfCars', 'numerOfCars']

print("Wartosc pobrana z instancji:", car_1.numerOfCars, "Wartosc pobrana z klasy", Car.numerOfCars)
# Wartosc pobrana z instancji: 2 Wartosc pobrana z klasy 2

# WADY KLAS jw. - modyfikacja zmiennej zmiekształca wyniki; nie uwzględnia odejmowania samochodów!!!
