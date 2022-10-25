'''
Szef cukierni w której pracujesz poprosił Cię o napisanie programu, który koniecznie ma działać obiektowo!
Zaczynamy od zdefiniowania klasy Cake, która ma posiadać atrybuty:
-name opisujące nazwę produktu
-kind opisujący rodzaj wypieku np. torty, ciastka, muffinki, bezy
-taste z głównym smakiem
-additives - zawierający listę dodatków do danego ciasta, np. owoce, posypki, polewy itp, jeżeli ciasto nie ma dodatków, to będzie to pusta lista
-filling - opis nadzienia, jeżeli dane ciasto nie ma nadzienia, to ma to być pusty napis
'''
class Cake:
 
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
''' 
Po zdefiniowaniu klasy utwórz kilka instancji tej klasy, 
to dobry moment na wzbogacenie słownictwa w zakresie słodkośc
i w języku angielskim, ale jak wolisz - możesz to robić po polsku
'''
 
cake01 = Cake('Ciasto waniliowe','ciasto', 'wanilia', ['czekolada', 'orzechy'], 'smietana')
cake02 = Cake('Czekolada Muffin','muffin', 'czekolada', ['czekolada'], 'krem')
cake03 = Cake('Super Slodka Markiza','beza', 'bardzo słodka', ['lukier'], 'masa toffi')

# Utwórz listę bakery_offer i dodaj do niej instancje wcześniej utworzonych obiektów klasy Cake

bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)
 
print("Dzis w naszej ofercie:")

# Napisz pętlę przechodzącą przez wszystkie instance klasy znajdujące się na liście bakery_offer
for c in bakery_offer:
    print("{} - ({}) glowny smak: {} z dodatkami {}, wypelnione {}".format(
        c.name, c.kind, c.taste, c.additives, c.filling))
