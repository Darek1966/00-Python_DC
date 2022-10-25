
markaOnSale = 'Opel'

class Car(object):     

    numerOfCars = 0   
    listOfCars = []


    def __init__(self, marka, model, isPoduszkaOk, isLakierOk, isMechOk, isOnSale):
        print('>>To jest __init__ klasy rodzicielskiej:', self.__class__.__name__)
        self.marka = marka         
        self.model = model
        self.isPoduszkaOk = isPoduszkaOk
        self.isLakierOk = isLakierOk
        self.isMechOk = isMechOk
        self.__isOnSale = isOnSale  
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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.marka == markaOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Zmiana statusu IsOnSale na {}  dla  {}'.format(newIsOnSaleStatus, self.marka))
        else:
            print('Nie mozna zmienic statusu IsOnSale, Wyprzedaz wazna tylko dla {}'.format(markaOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'jesli ustawione na true, samochod jest dostepny w promocji/wyprzedazy')

class Truck(Car):

    def __init__(self, marka, model, isPoduszkaOk, isLakierOk, isMechOk, isOnSale, capacityKg):
        print('>>To jest __init__ klasy dziecięcej:', self.__class__.__name__)
        super().__init__(marka, model, isPoduszkaOk, isLakierOk, isMechOk, isOnSale) # wszystko z klasy Car - dziedziczenie
        self.capacityKg = capacityKg

    def GetInfo(self):
        super().GetInfo()
        print('CapacityKg -     {}'.format(self.capacityKg))


truck_1 = Truck('Ford', 'Transit', True, False, True, False, 1600)
truck_2 = Truck('Renault', 'Trafic', True, True, True, True, 1200)

print('Wywoływanie właściwości:')
print(truck_1.marka, truck_1.capacityKg, truck_1.IsOnSale, truck_2.marka, truck_2.capacityKg, truck_2.IsOnSale)

truck_1.GetInfo()
truck_2.GetInfo()


