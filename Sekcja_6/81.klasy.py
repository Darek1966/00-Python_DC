
class Car:      # klasa (szablon)

    def __init__(self, marka, model, isPoduszkaOk, isLakierOk, isMechOk):
        self.marka = marka
        self.model = model
        self.isPoduszkaOk = isPoduszkaOk
        self.isLakierOk = isLakierOk
        self.isMechOk = isMechOk

car_1 = Car('Opel', 'Corsa', True, True, True)
car_2 = Car('Seat', 'Ibiza', True, False, True)

print(car_1.marka, car_1.model, car_1.isPoduszkaOk, car_1.isLakierOk, car_1.isMechOk)
print(car_2.marka, car_2.model, car_2.isPoduszkaOk, car_2.isLakierOk, car_2.isMechOk)

# # to było w przykładzie bez klas
'''
car_1 ={                
'carMarka' : "Opel",
'carModel' : 'Corsa',
'carPoduszkaOk' : True,
'carLakierOk' : True,
'carMechOk' : True
}

car_2 ={
'carMarka' : "Seat",
'carModel' : 'Ibiza',
'carPoduszkaOk' : True,
'carLakierOk' : False,
'carMechOk' : True
}

def czyUszkodzony (aCar):
    return not (aCar['carPoduszkaOk'] and aCar['carLakierOk'] and aCar['carMechOk'])

print(czyUszkodzony(car_1))
print(czyUszkodzony(car_2))

cars = [car_1, car_2]
for c in cars:
    print('{} {} uszkodzony = {}'.format(c['carMarka'], c['carModel'], czyUszkodzony(c)))
'''