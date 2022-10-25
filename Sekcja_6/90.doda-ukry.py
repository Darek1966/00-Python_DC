
class Car:     

    numerOfCars = 0   # zmienne na poziomie klasy
    listOfCars = []


    def __init__(self, marka, model, isPoduszkaOk, isLakierOk, isMechOk, isOnSale):
        self.marka = marka         
        self.model = model
        self.isPoduszkaOk = isPoduszkaOk
        self.isLakierOk = isLakierOk
        self.isMechOk = isMechOk
        self.__isOnSale = isOnSale   # __ ukrywa zmienną, nie można jej zmodyfikować
        Car.numerOfCars +=1             
        Car.listOfCars.append(self)     


    def JestUszkodzony(self):      
        return not (self.isPoduszkaOk and self.isLakierOk and self.isMechOk)

    def GetInfo(self):
        print('{}   {}'.format(self.marka, self.model).upper())
        print('Poduszka - ok -     {}'.format(self.isPoduszkaOk))
        print('Lakier   - ok -     {}'.format(self.isLakierOk))
        print('Mechanik - ok -     {}'.format(self.isMechOk))
        print('Jest w wyprzedazy   {}'.format(self.__isOnSale))
        print('-------------------------------------------')

car_1 = Car('Opel', 'Corsa', True, True, True, False) 
car_2 = Car('Seat', 'Ibiza', True, False, True, True) 

car_1.GetInfo()
car_2.GetInfo()

car_2.__isOnSale = False # nie da rady zmienić __isOnSale przez __
car_2.RokProd = 2005     # można tak modyfikować (to wada klas Pythona)
del car_2.RokProd        # del - usunięcie

setattr(car_2, 'TAXI', False)    # setsttr - dodawanie i modyfikowanie właściwości
delattr(car_2, 'TAXI')           # delattr - usuwa artybut
print(hasattr(car_2, 'TAXI'))    # hassttr - czy posiada taki atrybut

print(vars(car_2))
