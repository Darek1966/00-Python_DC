
markaOnSale = 'Opel'

class Car:     

    def __init__(self, marka, model, isPoduszkaOk, isLakierOk, isMechOk, isOnSale):
        self.marka = marka         
        self.model = model
        self.isPoduszkaOk = isPoduszkaOk
        self.isLakierOk = isLakierOk
        self.isMechOk = isMechOk
        self.__isOnSale = isOnSale  
        
    @property
    def IsOnSale(self):
        return self.__isOnSale

    @IsOnSale.setter
    def IsOnSale(self, newIsOnSaleStatus):
        if self.marka == markaOnSale:
            self.__isOnSale == newIsOnSaleStatus
            print('Zmiana statusu IsOnSale na {}  dla  {}'.format(newIsOnSaleStatus, self.marka))
        else:
            print('Nie mozna zmienic statusu IsOnSale, Wyprzedaz wazna tylko dla {}'.format(markaOnSale))

    @IsOnSale.deleter   # będzie można stosować del
    def IsOnSale(self):
        self.__isOnSale = None

    @property
    def CarTitle(self):
        return "Marka:  {}, Model:  {}".format(self.marka, self.model).title()

car_1 = Car('Seat', 'Ibiza', True, True, True, False) 

print(car_1.IsOnSale)
car_1.IsOnSale = True   # można dodawać
del car_1.IsOnSale   # nie można usunąć - error (bez deleter)
print(car_1.IsOnSale)
print(car_1.CarTitle)
