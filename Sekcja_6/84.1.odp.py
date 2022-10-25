# Do klasy z poprzedniego zadania dodaj 3 metody:
class Cake:
 
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

# show info, która
# -wyświetli wielkimi literami nazwę produktu
# -wyświetli informację o smaku
# -jeśli produkt ma jakieś dodatki to je wyświetli
# -jeśli produkt ma nadzienie to je wyświetli
# (oczywiście przetestuj działanie funkcji po jej zaimplementowaniu)
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:    {}".format(self.kind))
        print("Taste:   {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling: {}".format(self.filling))
        print('-'*20)

# set_filling, która
# -jako argument przyjmie nazwę nadzienia ciasta
# -zapisze ją w atrybucie filling dla ciasta
    def set_filling(self, filling):
        self.filling = filling

# add_additives, która
# -jako argument przyjmie listę dodatków
# -wartości z listy doda do aktualnej listy dodatków
    def add_additives(self, additives):
        self.additives.extend(additives)
 
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')
 
bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)

'''
Następnie dodaj do muffinki nadzienie kremowe, 
a do bezy dodaj kokos i posypkę kakaową. 
Tak zmodyfikowane wypieki wyświetl.
'''
cake02.set_filling('vanilla cream')
cake03.add_additives(['cocoa powder', 'coconuts'])
 
print("Today in our offer:")
for c in bakery_offer:
    c.show_info()
