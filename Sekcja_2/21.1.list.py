
# list = range(10)
# print('Lista:', list, type(list)) # nie jest jeszcze listą, jest range - Lista: range(0, 10) <class 'range'>

list = list (range(10))
print('Lista:', list, type(list)) # Lista: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'> - jest ok

