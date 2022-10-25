'''
W tym zadaniu dodasz do klasy Cake obsługę operatora:
__iadd__ 
__str__
'''
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

# dodaj metodę pozwalającą na wygodne formatowanie obiektów klasy Cake do postaci tekstu. 
# Niech zwracany będzie napis składający się z atrybutów kind, name oraz additives 
    def __str__(self):
        return "{} - {} with {}".format(self.kind, self.name, self.additives)

# dodaj metodę pozwalającą na dodawanie do klasy napisu. 
# Ten napis ma być dołączany jako kolejny element na liście additives 
    def __iadd__(self, other):
 
        if type(other) is str:
            self.additives.append(other)
            return self
# zmodyfikuj powyższą metodę tak, aby możliwe było przekazanie na raz większej ilości  dodatków. 
# Wszystkie one mają być dołączone do listy additives.
        elif type(other) is list:
            self.additives.extend(other)
            return self
# zmodyfikuje powyższą metodę tak, że jeśli zostanie ona wykorzystana do dodania zmiennych innych typów, to wygenerowany zostanie błąd.
        else:
            raise Exception('Sorry - operation not implemented')
 
        
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

# przetestuj w/w metody
cake01 += 'cherry'
print(cake01)
 
cake01 += ['whipped cream', 'raspberry']
print(cake01)
 
# skończy się to błędem
# cake01 += 3
# print(cake01)