'''
Pracujemy z wynikiem LAB z poprzedniej lekcji.
Dodaj do klasy Cake atrybut na poziomie klasy. 
Nazwij go known_types. Będą w nim przechowywane produkowane w naszej cukierni słodkości. 
Przypisz do zmiennej listę np. w następującej postaci:
'''
class Cake:
 
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = [] # Dodaj do klasy Cake nowy atrybut bakery_offer, który na początku będzie pustą listą.
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
# Zmień __init__ tak, że jeżeli jako parametr kind zostanie przekazana wartość znajdująca się na liście known_kinds, to zostanie zaakceptowana, 
        if kind in self.known_kinds:
            self.kind = kind
# ale jeśli ktoś przekaże wartość spoza tej listy, to do nowo tworzonego obiektu do atrybutu kind zostanie wpisany napis other.
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
# # Zmień __init__ tak, aby po utworzeniu nowego obiektu typu Cake, został on automatycznie dodany do listy bakery_offer
        self.bakery_offer.append(self)
 
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
 
    def set_filling(self, filling):
        self.filling = filling
 
    def add_additives(self, additives):
        self.additives.extend(additives)
 
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')
# Przetestuj działanie nowej funkcji __init__ tworząc obiekt "wafel kakaowy":
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')
 
print("Today in our offer:")
# Zmień pętlę wyświetlającą informację o ofercie cukierni tak, aby korzystała z atrybutu klasy
for c in Cake.bakery_offer:
    c.show_info()
    
# Sprawdź czy obiekty cake01 i inne są instancjami klasy Cake korzystając z funkcji isinstance i type
# Wyświetl informacje o instancji cake01 i o klasie Cake korzystając z funkcji vars i dir
print('Is cake01 of type Cake? (isinstance)', isinstance(cake01, Cake))
print('Is cake01 of type Cake? (type)', type(cake01) is Cake)
print('vars cake01', vars(cake01))
print('vars Cake?', vars(Cake))
print('dir cake01', dir(cake01))
print('dir Cake?', dir(Cake))
