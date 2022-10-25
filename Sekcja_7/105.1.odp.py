'''
Trzeba zdefiniować klasę NoDuplicates, która będzie miała tylko jeden atrybut - list. 
Ten atrybut to lista, która ma przechowywać tylko wartości unikalne.
'''
# Zdefiniuj klasę NoDuplicates
class NoDuplicates:

# W metodzie __init__ utwórz atrybut klasy list, który będzie pustą listą 
    def __init__(self):
 
        self.list = []
# Dodaj metodę __call__
# metoda ma przyjąć argument self i listę z nowymi obiektami, jakie mają być przechowywane w liście new_items 
    def __call__(self, new_items):
        
# dla każdego elementu z new_items, jeśli ten element nie występuje jeszcze na liście list, dodaj go do tej listy        
        for a in new_items:
            if not a in self.list:
                self.list.append(a)
 
# Utwórz obiekt my_no_dup_list, który będzie instancją klasy NoDuplicates. Wyświetl ten obiekt.
my_no_dup_list = NoDuplicates()
print(my_no_dup_list.list)

# Wywołując instancję dodaj do listy elementy z listy ['keyboard','mouse']. Wyświetl ten obiekt. Oba napisy powinny zostać dodane do listy
my_no_dup_list(['keyboard','mouse'])
print(my_no_dup_list.list)

# Wywołując instancję dodaj do listy elementy z listy ['keyboard','mouse','pendrive']. Wyświetl ten obiekt.  Tylko pendrive powinien zostać dodany 
my_no_dup_list(['keyboard','mouse','pendrive'])
print(my_no_dup_list.list)

# Wywołując instancję dodaj do listy elementy z listy ['charger','pendrive'].Wyświetl ten obiekt.  Tylko charger powinien zostać dodany 
my_no_dup_list(['charger','pendrive'])
print(my_no_dup_list.list)
