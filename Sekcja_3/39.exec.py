
from unittest import result

from numpy import source

var_x = 10

# source = 'var_x = 4'

source = '''
for i in range(var_x):
    print('-' * i)
'''                     # w wynikach pół choinki


source = '''
new_var = 1
for i in range(var_x):
    print('-' * i)
    new_var += 1
''' 
result = exec(source)
print(result)   # None

print(var_x)  # 4
# print(new_var) # wyświetla błąd - new_var niezdefiniowana

source = input('Wprowadź wartość: ')
print(eval(source)) # może wykonywać niebezpieczne kawałki kodu
