

class Car:      # klasa (szablon)

    def __init__(self, marka, model, isPoduszkaOk, isLakierOk, isMechOk):
        self.marka = marka          # atrybuty instancji
        self.model = model
        self.isPoduszkaOk = isPoduszkaOk
        self.isLakierOk = isLakierOk
        self.isMechOk = isMechOk

    def JestUszkodzony(self):         # funkcja wewnątrz klasy - metoda
        return not (self.isPoduszkaOk and self.isLakierOk and self.isMechOk)

    def GetInfo(self):                 # funkcja wewnątrz klasy - metoda
        print('{}   {}'.format(self.marka, self.model).upper())
        print('Poduszka - ok -     {}'.format(self.isPoduszkaOk))
        print('Lakier   - ok -     {}'.format(self.isLakierOk))
        print('Mechanik - ok -     {}'.format(self.isMechOk))
        print('-------------------------------------------')


car_1 = Car('Opel', 'Corsa', True, True, True) # instancja klasy
car_2 = Car('Seat', 'Ibiza', True, False, True) # instancja klasy

print('Identyfikator klasy to:', id(Car))       # Id of class is: 2973455777456
print('Identyfikator instancji to:', id(car_1), id(car_2)) # Id of instance are: 2973462084624 2973462084528

print("Sprawdz, czy obiekt nalezy do klasy:", isinstance(car_1, Car)) # Sprawdz, czy obiekt nalezy do klasy: True
print("Sprawdz, czy obiekt nalezy do klasy za pomocą typu:", type(car_1) is Car) # Sprawdz, czy obiekt nalezy do klasy za pomocą typu: True

print("Sprawdz klase obiektu za pomocą__class__:", car_1.__class__) # Sprawdz klase obiektu za pomocą__class__: <class '__main__.Car'>
print("Lista atrybutow instancji z wartosciami:", vars(car_1)) # Lista atrybutow instancji z wartosciami: {'marka': 'Opel', 'model': 'Corsa', 'isPoduszkaOk': True, 'isLakierOk': True, 'isMechOk': True}

print("Lista atrybutow klas z wartosciami:", vars(Car))
# Lista atrybutow klas z wartosciami: {'__module__': '__main__', '__init__': <function Car.__init__ at 0x0000019DC7FC2DD0>, 'JestUszkodzony': <function Car.JestUszkodzony at 0x0000019DC7FC2E60>, 'GetInfo': <function Car.GetInfo at 
# 0x0000019DC7FC2EF0>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
