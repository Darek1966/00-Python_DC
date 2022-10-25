
class Car:     

    def __init__(self, marka, model, isPoduszkaOk, isLakierOk, isMechOk, accessories):
        self.marka = marka         
        self.model = model
        self.isPoduszkaOk = isPoduszkaOk
        self.isLakierOk = isLakierOk
        self.isMechOk = isMechOk
        self.accessories = accessories 
           
    def GetInfo(self):
        print('{}   {}'.format(self.marka, self.model).upper())
        print('Poduszka - ok -     {}'.format(self.isPoduszkaOk))
        print('Lakier   - ok -     {}'.format(self.isLakierOk))
        print('Mechanik - ok -     {}'.format(self.isMechOk))
        print('Akcesoria           {}'.format(self.accessories))
        print('-------------------------------------------')

    def __iadd__(self, other):          # operator __iadd  (+ =)
        if type(other) is list:         # jeżeli (other) to lista, do dodajemy akcesoria
            accessories = self.accessories
            accessories.extend(other)
            return Car(self.marka, self.model, self.isPoduszkaOk, self.isLakierOk, self.isMechOk, accessories)
        elif type(other) is str:        # jak nie jest to lista, tylko string, to znowu wywołujemy klasę Car
            accessories = self.accessories
            accessories.append(other)
            return Car(self.marka, self.model, self.isPoduszkaOk, self.isLakierOk, self.isMechOk, accessories)
        else:                           # jeśli wpiszemy co innego, to zobaczymy komunikat o błędzie
            raise Exception ('Dodawanie typu {} do samochodu nie jest wdrozony'.format(type(other)))

    def __add__(self, other):
        if type(other) is Car:
            return[self, other]
        else:                               # jeżeli dodany nie jest samochodem, to zobaczymy komunikat o błędzie
            raise Exception ('Dodawanie typu {} do samochodu nie jest wdrozony'.format(type(other)))

    def __str__(self):
        return 'Marka: {}, Model: {}'.format(self.marka, self.model)


car_1 = Car('Seat', 'Ibiza', True, True, True, ['winter tires'])
car_1.GetInfo()

car_1 += ['navigation system', 'roof rack']
car_1.GetInfo()

car_1 += 'loudspeeker system'
car_1.GetInfo()

car_2 = Car('Opel', 'Corsa', True, False, True, [])

car_pack = car_1 + car_2
print('car_1 + car_2=', car_pack[0].marka, car_pack[1].marka)

print(car_1)
