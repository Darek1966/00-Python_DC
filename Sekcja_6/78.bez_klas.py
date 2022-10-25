

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
