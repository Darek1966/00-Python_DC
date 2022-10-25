'''
Zaczynamy od klasy, która jest rozwiązaniem poprzedniego zadania. 
Ponieważ obecnie skupiamy się bardziej na pobieraniu kolejnych elementów, 
zrezygnujemy z funkcji opóźniającej program oraz skorzystamy ze zdecydowanie krótszych list produktów, promocji i klientów:

Naszym celem jest eliminacja metody __next__ i jej zamiana na __getitem__, 
co pozwoli na odwoływanie się do i-tego generowanego elementu. 
Jednocześnie jednak chcemy nadal móc wykorzystywać obiekt w pętli for, a wiesz, 
że domyślnie do tego jest potrzebna metoda __next__. Obejdziesz ten problem wykorzystując sztuczkę z funkcją iter()
'''
class Combinations:

# Usuń definicję metody __next__
# Zmienne current_product, current_promotion i current_customer inicjowane w __init__ też nie będą już potrzebne
 
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

# Dodaj do klasy definicję metody __getitem__
    def __getitem__(self, item):

# Jeżeli item jest większe od ilości elementów, które może generować obiekt klasy, to zgłoś wyjątek StopIteration
# wskazówka - maksymalna ilość generowanych kombinacji to ilość produktów razy ilość promocji razy ilość klientów
# W przeciwnym razie musisz wyliczyć jaką kombinację należy zwrócić i w tym celu 
        if item >= len(self.products)*len(self.promotions)*len(self.customers):
            raise  StopIteration()
# w zmiennej pos_products zapisz wynik dzielenia całkowitego wartości item przez ilość promocji razy ilość klientów
        else:
            pos_products = item // (len(self.promotions)*len(self.customers))
            # print(item, (len(self.promotions) * len(self.customers)), pos_products)

# zaktualizuj zmienną item zapisując w niej wynik dzielenia modulo wartości item przez ilość promocji razy ilość klientów
            item = item % (len(self.promotions)*len(self.customers))

# w zmiennej pos_promotions zapisz wynik dzielenia całkowitego wartości item przez ilość klientów
            pos_promotions = item // len(self.customers)

# zaktualizuj zmienną item zapisując w niej wynik dzielenia modulo wartości item przez ilość klientów
            item = item % len(self.customers)

# w zmiennej pos_customers zapisz wartość item
            pos_customers = item

# teraz zmienne pos_products, pos_promotions i pos_customers wskazują na poprawny elementy list products, promotions i customers, które należy zwrócić
 
            return "{} - {} -{}".format(self.products[pos_products],
                                        self.promotions[pos_promotions],
                                        self.customers[pos_customers])
 
# Zwróć napis składający się z elementu listy products znajdującego  się na pozycji pos_products 
# oraz z elementu listy promotions znajdującego się na pozycji pos_promotions 
# oraz z elementu listy customers znajdującego się na pozycji pos_customers
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]
 
combinations = Combinations(products, promotions, customers)

# W głównej części skryptu napisz pętlę for, która:
# zmiennej sterującej i przypisze wartości od 1  do 30 (tyle mamy obecnie możliwych kombinacji - 3 produkty * 2 promocje * 5 klientów)
# w każdym wykonaniu pętli wyświetli  i-ty element z obiektu combinations. 
# Dzięki temu, że klasa Combinations ma teraz metodę __getitem__ zobaczysz wszystkie możliwe kombinacje produktów, promocji i klientów
# Po zakończonych testach zakomentuj tę pętlę
# for i in range(0, 31):
#    print(i, combinations[i])

# Sprawdź czy z obiektu combinations można pobierać kolejne elementy korzystając z funkcji next (nie powinno się dać) 
# Zrób coś żeby się dało! :)
# Wskazówka: Pamiętaj o funkcji iter()
# Przetestuj pobieranie kolejnych elementów metodą next()
combinations_iterator = iter(combinations)
print(next(combinations_iterator))

# Napisz pętlę for, która przejdzie przez wszystkie możliwe kombinacje zwracane przez obiekt combinations, ale nie korzystaj ze zmiennej sterującej! 
for c in combinations_iterator:
    print(c)
