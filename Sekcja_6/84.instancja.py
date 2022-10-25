
class Car:      # klasa (szablon)

    def __init__(self, marka, model, isPoduszkaOk, isLakierOk, isMechOk):
        self.marka = marka
        self.model = model
        self.isPoduszkaOk = isPoduszkaOk
        self.isLakierOk = isLakierOk
        self.isMechOk = isMechOk

    def JestUszkodzony(self):         # funkcja wewnątrz klasy
        return not (self.isPoduszkaOk and self.isLakierOk and self.isMechOk)

    def GetInfo(self):                 # funkcja wewnątrz klasy
        print('{}   {}'.format(self.marka, self.model).upper())
        print('Poduszka - ok -     {}'.format(self.isPoduszkaOk))
        print('Lakier   - ok -     {}'.format(self.isLakierOk))
        print('Mechanik - ok -     {}'.format(self.isMechOk))
        print('-------------------------------------------')


car_1 = Car('Opel', 'Corsa', True, True, True)
car_2 = Car('Seat', 'Ibiza', True, False, True)

car_1.GetInfo()
car_2.GetInfo()


print('Czy samochód jest uszkodzony:')
print(car_1.marka, car_1.model, car_1.JestUszkodzony())
print(car_2.marka, car_2.model, car_2.JestUszkodzony())

print('x' * 30)
print(car_1.marka, car_1.model, car_1.isPoduszkaOk, car_1.isLakierOk, car_1.isMechOk)
print(car_2.marka, car_2.model, car_2.isPoduszkaOk, car_2.isLakierOk, car_2.isMechOk)
