
markaOnSale = 'Opel' # będzie można modyfikować tylko dla Opel

class Car:     

    numerOfCars = 0   
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

    def GetIsOnSale(self):
        return self.__isOnSale

    def SetIsOnSale(self, newIsOnSaleStatus):
        if self.marka ==markaOnSale:
            self.__isOnSale == newIsOnSaleStatus
            print('Zmiana statusu IsOnSale na {}  dla  {}'.format(newIsOnSaleStatus, self.marka))
        else:
            print('Nie mozna zmienic statusu IsOnSale, Wyprzedaz wazna tylko dla {}'.format(markaOnSale))
# nowe właściwości dla klasy
    IsOnSale = property(GetIsOnSale, SetIsOnSale, None, 'jesli ustawione na true, samochod jest dostepny w promocji/wyprzedazy')    # property - funkcja nowa

car_1 = Car('Opel', 'Corsa', True, True, True, False) 
car_2 = Car('Seat', 'Ibiza', True, False, True, True) 

print('Czy samochody sa na wyprzedazy:', car_1.GetIsOnSale(), car_2.GetIsOnSale())

car_1.SetIsOnSale(True)
car_2.SetIsOnSale(False)
print('Czy samochody sa na wyprzedazy:', car_1.GetIsOnSale(), car_2.GetIsOnSale())

# po dodaniu property
car_1.IsOnSale = True
car_2.IsOnSale = True
print('Czy samochody sa na wyprzedazy:', car_1.IsOnSale, car_2.IsOnSale)
