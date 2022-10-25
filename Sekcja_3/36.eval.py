
from unittest import result
from numpy import source

var_x = 10
password = 'moje super tajne hasło'

# source = 'var_x + 2'
# source = 'var_x + 3'
source = '33 + 3'
# source = '__import__("os").getcwd()' # obejście hasła
# source = 'password'   # moje super tajne hasło

# result = eval(source)
# print(result)         # 12   # 13

# globals = globals().copy()
# del globals ['password']  # usuwamy zmienną wskazującą na hasło

globals = {}   # puste środowisko - wyświetli tylko to, co wprowadzimy

result = eval(source, globals)
print(result)         # 13

# print(globals())

