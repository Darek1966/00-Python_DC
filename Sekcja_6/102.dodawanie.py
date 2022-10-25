import csv
import types


def exportToFile_static(path, header, data):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
        print('>>>To jest funkcja exportToFile - metoda statyczna')

def exportToFile_Class(cls, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['marka', 'model', 'IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.marka, c.model, c.IsOnSale])
        print('>>>To jest funkcja exportToFile - metoda klasy')

def exportToFile_Instance(self, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['marka', 'model', 'IsOnSale'])
        writer.writerow([self.marka, self.model, self.IsOnSale])
        print('>>>To jest funkcja exportToFile - metoda instancji')

markaOnSale = 'Opel' 

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

   
    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.marka ==markaOnSale:
            self.__isOnSale == newIsOnSaleStatus
            print('Zmiana statusu IsOnSale na {}  dla  {}'.format(newIsOnSaleStatus, self.marka))
        else:
            print('Nie mozna zmienic statusu IsOnSale, Wyprzedaz wazna tylko dla {}'.format(markaOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'jesli ustawione na true, samochod jest dostepny w promocji/wyprzedazy')    # property - funkcja nowa

car_1 = Car('Opel', 'Corsa', True, True, True, False) 
car_2 = Car('Seat', 'Ibiza', True, False, True, True) 

print('Statyczny-------------' * 10)
Car.ExportToFile_Static = exportToFile_static    # funkcja statyczna
# exportToFile_static(r'E:\Python\00 Python_DC\temp\export_static.csv', ['Marka', 'Model', 'IsOnSale'], [car_1.marka, car_1.model, car_1.IsOnSale])
Car.ExportToFile_Static(r'E:\Python\00 Python_DC\temp\export_static.csv', ['Marka', 'Model', 'IsOnSale'], [car_1.marka, car_1.model, car_1.IsOnSale])
print(dir(Car))

print('Klasa-----------------' * 10)
# Car.ExportToFile_Class = exportToFile_Class   # błąd
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.ExportToFile_Class(path = r'E:\Python\00 Python_DC\temp\export_Class.csv')
print(dir(Car))

print('Instancja-------------' * 10)
# car_1.ExportToFile_Instance = exportToFile_Instance  # błąd
car_1.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_1)
car_1.ExportToFile_Instance(path = r'E:\Python\00 Python_DC\temp\export_instance.csv')
print(dir(car_1))

print('-' * 50)
if hasattr(car_1, 'ExportToFile_Static') and callable(car_1.ExportToFile_Static):
    print('Obiekt ma metode ExportToFile_Static')
if hasattr(car_1, 'ExportToFile_Class') and callable(car_1.ExportToFile_Class):
    print('Obiekt ma metode ExportToFile_Class')
if hasattr(car_1, 'ExportToFile_Instance') and callable(car_1.ExportToFile_Instance):
    print('Obiekt ma metode ExportToFile_Instance')
    