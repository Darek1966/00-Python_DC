'''
Twoja firma będzie wykonywała analizę sprzedażową dla klienta. Jeden z algorytmów określa że:
dla każdego produktu (a jest ich 500)
należy zasymulować każdy rodzaj promocji (a jest ich 50)
i przewidzieć wyniki sprzedaży dla próbki klientów (a jest ich 500)

Widać więc, że będzie 500x50x500 przypadków do przeanalizowania. 
Poniższy kod generuje listę produktów, promocji i klientów, a następnie przechodzi przez listę wszystkich kombinacji. 
Dodatkowo po przejściu przez wszystkie kombinacje, program zatrzymuje się na 10 sekund:

Uruchom powyższy kod i zaobserwuj ilość konsumowanej pamięci. U mnie było to ponad 1 GB. 
Aby wygodnie obserwować zajęcie pamięci program zatrzymuje się na końcu na 10 sekund. 
Zmień ten parametr jeżeli potrzebujesz więcej czasu na sprawdzenie pamięci. 
Gdyby ta wartość powodowała u Ciebie błędy zmniejsz ilość produktów, promocji lub klientów.
'''
import time

# Zdefiniuj klasę Combinations 
class Combinations:

# W metodzie __init__
# przyjmij parametry products, promotions, customers i zapisz je jako atrybuty klasy. 
# Ponadto zdefiniuj trzy atrybuty: current_product, current_promotion, current_customer i przypisz im wartość 0. 
# Podczas zwracania kombinacji produkt-promocja-klient te liczby będą wskazywały na w danej chwili zwracany element z list products, promotions, customers 
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
 
        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

# Zdefiniuj metodę __next__, która:
# Sprawdzi czy current_customer jest >= od długości listy customers. 
# Jeśli tak, to wartość current_customer należy ustawić na 0, a wartość current_promotion zwiększyć o 1 
    def __next__(self):
 
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

# Sprawdzi czy current_promotion jest >= od długości listy promotions. 
# Jeśli tak, to wartość current_promotion należy ustawić na 0, a wartość current_product zwiększyć o 1
        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

# Sprawdzić, czy current_product jest >-= od długości listy products. 
# Jeśli tak, to należy  wartość current_product ustawić na -0 i zgłosić wyjątek StopIteration
        if self.current_product >= len(self.products):
            self.current_product =0
            raise StopIteration()

# do lokalnej zmiennej item_to_return zapisze kombinację utworzoną  jako element z listy products wskazywany przez liczbę current_product, 
# element z listy promotions wskazywany przez liczbę current_promotion i element z listy customers wskazywany przez liczbę current_customer 
        item_to_return = "{} - {} -{}".format(self.products[self.current_product],
                                              self.promotions[self.current_promotion],
                                              self.customers[self.current_customer])
# liczbę current_customer zwiększy o 1
        self.current_customer += 1

# zwróci zmienną item_to_return
        return  item_to_return

# Zdefiniuj metodę __iter__ zwracającą obiekt self 
    def __iter__(self):
        return  self
 
 
products = ["Product {}".format(i) for i in range(1, 500)]
promotions = ["Promotion {}".format(i) for i in range(1, 50)]
customers = ['Customer {}'.format(i) for i in range(1, 500)]

# Utwórz instancję klasy Combinations i zapisz ją w zmiennej combinations 
combinations = Combinations(products, promotions, customers)

# Dla każdego elementu zmiennej combinations wykonaj  pass
for c in combinations:
    pass
# Uruchom program i zmierz ilość wykorzystywanej pamięci przez ten program. Powinno to być o wieeeele mniej :) 
time.sleep(10)

# 726 MB