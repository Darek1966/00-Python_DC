
# def Funkcja(prefix='Please buy me', what='something nice', *args):
from keyword import kwlist

from numpy import product


def Funkcja(prefix='Please buy me', what='something nice', *args, **kwargs):

    print(prefix, what)
    print(args)     # utworzy tuplet ( )
    print(kwargs)   # utworzy słownik { }

# Funkcja('Plaese buy me', 'a new car', 'a cat', 'a dog', 'a dragon') # można dopisywać - dla args

Funkcja('Plaese buy me', 'a new car', 'a cat', 'a dog', 'a dragon', shop='market', color='any') # dla kwargs

product = ['milk', 'bread', 'flekes']
parameters = {'price':'low', 'time':'now' }

Funkcja ('Buy me', 'newspaper', *product, **parameters)
