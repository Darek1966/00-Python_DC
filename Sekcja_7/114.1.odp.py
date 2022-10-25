
class Cake:
 
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)
 
    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)
'''
Ciastkarnia będzie się specjalizować w produkcji tortów na różne okazje. 
Ponieważ klasa Cake nie ma aż tylu specyficznych atrybutów pozwalających na opisanie nowych tortów, 
decydujesz się utworzyć nową klasę SpecialCake, która odziedziczy z klasy Cake
Nowa klasa ma dodatkowo przyjąć i zapamiętać następujące atrybuty:
occasion - okazja z jakiej jest zamawiany wypiek
shape - kształt tortu, np kwadratowy, piramida, jeż, standardowy
ornaments - dodatkowe ozdoby, np kwiatki, serduszka, listki
text - tekst jaki ma być wypisany na torcie
'''  
class SpecialCake(Cake):
 
    def __init__(self, name, kind, taste, additives, filling,
                 occasion, shape, ornaments, text):
 
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text
# Korzystając z mechanizmów dziedziczenia dodaj do metody show_info instrukcje wyświetlające specyficzne dla nowej klasy
    def show_info(self):
        super().show_info()
        print("Ocassion:    {}".format(self.occasion))
        print("Shape:       {}".format(self.shape))
        print("Ornaments:   {}".format(self.ornaments))
        print("Text:        {}".format(self.text))
        print('-'*20)

# Utwórz dwa obiekty klasy SpecialCake: birthday i wedding        
birthday = SpecialCake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream',
                       'birthday', 'standard', 'hearts', '15')
wedding  = SpecialCake('Vanilla Cake','cake', 'vanilla', ['whipped cream', 'coconut shirms'], 'strawberries cream',
                       'wedding', 'pyramid', 'pigeons', 'Patricia & Tom')
 
# Wyświetl informacje o obu obiektach korzystając z metody show_info()
birthday.show_info()
wedding.show_info()

# Dla każdego obiektu z listy SpecialCake.bakery_offer
# wyświetl pełną nazwę - właściwość full_name
# wywołaj metodę show_info() 
for cake in SpecialCake.bakery_offer:
    print(cake.full_name)
    cake.show_info()
 