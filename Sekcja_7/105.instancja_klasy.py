
class MemoryClass:
    def __init__(seff, list):       # klasa i obiekty klasy
        seff.list_of_items = list   # metoda klasy

    def __call__(self, item):       # żeby obiekt klasy (list) uruchamiać jako metodę trzeba __call__
        self.list_of_items.append(item)
        
mem = MemoryClass([])               # zmienna mem - pusta lista
print('List of items in memory', mem.list_of_items)

mem.list_of_items.append('by sugar')    # metoda - dodajemy przy użyciu metody
print('List of items in memory', mem.list_of_items)

mem('buy milk')     # obiekt klasy (list) uruchamiany jako metoda
print('List of items in memory', mem.list_of_items)

mem('buy coffee')   # obiekt klasy (list) uruchamiany jako metoda
print('List of items in memory', mem.list_of_items)

print('This class is callable:', callable(MemoryClass))
print('This class is callable:', callable(mem))
