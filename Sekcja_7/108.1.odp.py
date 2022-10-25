'''
Oto nieco okrojona wersja klasy Cake.
 Na zewnątrz klasy została zdefiniowana inna funkcja, która będzie wykorzystywana w internetowym systemie zamówień wypieków. Oto ona:
       def add_extra_additives(cake, additives):
           cake.add_additives(additives)

Problem polega na tym, że podczas składania zamówienia klient może dobierać dodatki do wypieku. 
Niektóre z wypieków już te dodatki posiadają, więc można doprowadzić do tego, że wśród składników 
jedna pozycja znajdzie się kilka razy. Zobacz, jak aktualnie zachowuje się funkcja, która dodaje czekoladę i orzechy:
add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()
 
add_extra_additives(cake01, ['strawberries', 'sugar-flowers','chocolade', 'nuts'])
cake01.show_info()
Rozwiążesz ten problem definiując dekorator, który również będzie klasą, a następnie oznaczysz tym dekoratorem funkcję add_extra_additives
'''

# Zdefiniuj klasę NoDuplicates
class NoDuplicates:
# metoda __init__ przyjmuje argument funct, który zapisuje w lokalnych zmiennych instancji 
    def __init__(self, funct):
        self.funct = funct
# metoda __call__ ma oprócz argumentu self przyjąć te same argumenty co funkcja add_extra_additives.  
    def __call__(self, cake, additives):
# zdefiniuj pustą listę no_duplicate_list, która będzie zawierać tylko te dodatki, które są unikalne (nie ma ich jeszcze na liście additives w obiekcie cake
        no_duplicate_list = []
# przejdź przez wszystkie dodatki, które mają być dodane do ciasta
        for a in additives:
            if not a in cake.additives:
                no_duplicate_list.append(a) # jeśli taki dodatek nie znajduje się jeszcze na liście additives w wypieku, to dodaj go do listy no_duplicate_list
        self.funct(cake, no_duplicate_list) # na koniec wywołaj funkcję funct przekazując do niej obiekt cake oraz nową listę z unikalnymi dodatkami
        
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
 
    def add_additives(self, additives):
        self.additives.extend(additives)
 
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')

# Oznacz funkcję add_extra_additives dekoratorem wskazującym na klasę NoDuplicates
@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)

# Przetestuj działanie funkcji. Dodatki, które dany obiekt cake już posiadał, nie powinny być teraz dodawane drugi raz   
add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()
 
add_extra_additives(cake01, ['strawberries', 'sugar-flowers','chocolade', 'nuts'])
cake01.show_info()

'''
Jeśli temat Cię zainteresował zajrzyj na stronę
https://www.codementor.io/sheena/advanced-use-python-decorators-class-function-du107nxsv
gdzie pokazano, w jaki sposób korzystając z dekoratorów zaimplementowanych jako klasa zbudować system uprawnień do uruchamiania funkcji
'''
