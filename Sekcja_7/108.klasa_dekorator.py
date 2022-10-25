
import random  # losowanie

class MemoryClass: # tworzymy, żeby w losowaniach nie powtarzały się samochody
    list_of_already_selected_items = []  # lista już wylosowanych samochodów

    def __init__(self, funct):   # funct - poniższe funkcje
        print('>> this is init of MemoryClass')
        self.funct = funct

    def __call__(self, list):
        print('>> this is call of MemoryClass instance')
# lista już wylosowanych samochodów
        items_not_selected = [i for i in list if i not in MemoryClass.list_of_already_selected_items]
        print('+-- selecting only from a list of', items_not_selected) # jakie samochody podlegają losowaniu
        item = self.funct(items_not_selected)  # przekazana już okrojona lista
        MemoryClass.list_of_already_selected_items.append(item) # dodamy do lusty wylosowanych samochodów
        return item  # zwróć informację o wylosowanej marce samochodów
        
        
cars = ["opel", 'Toyota', 'Fiat', 'Ford', 'Renault', 'Mercedes', 'BMW', 'Peugeot', 'Porsche', 'Audi', 'VW', 'Mazda']

@MemoryClass
def SelectTodayPromotion(list_of_cars): # argument - lista samochodów
    return random.choice(list_of_cars)  # losowanie jednej marki

@MemoryClass
def SelectTodayShow(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)

print('Promotion:', SelectTodayPromotion(cars))
print('Show:', SelectTodayShow(cars),)
print('Free accessories', SelectFreeAccessories(cars))
