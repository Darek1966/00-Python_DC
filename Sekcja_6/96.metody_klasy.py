
class Car:     


    def __init__(self, marka, model, isPoduszkaOk, isLakierOk, isMechOk, isOnSale):
        self.marka = marka         
        self.model = model
        self.isPoduszkaOk = isPoduszkaOk
        self.isLakierOk = isLakierOk
        self.isMechOk = isMechOk
        self.__isOnSale = isOnSale  
           
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

    IsOnSale = property(GetIsOnSale, SetIsOnSale, None, 'jesli ustawione na true, samochod jest dostepny w promocji/wyprzedazy')

# metoda na poziomie klasy
    @classmethod
    def ReadFromText(cls, aText):       # cls - skrót od class
        aNewCar = cls(*aText.split(':'))
        return aNewCar

lineOfText = 'renault:Megane:True:True:False:False'
car_3 = Car.ReadFromText(lineOfText)
car_3.GetInfo()
