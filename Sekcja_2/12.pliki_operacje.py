
import os

path = r'E:\Python\00 Python_DC\Sekcja_2\mydata.txt'  # r - znak ma być traktowany surowo \ to \ a nie co innego

# os.remove(path) # jak odkomentuje remove-usunięcie, to plik zostanie usunięty, a nastepnie ponownie utworzony


if os.path.isfile(path):      # sprawdza czy plik instnieje
    print('Plik już jest',  path)
else:
    print('Pliku nie ma, będzie utworzony',  path)
    open(path, 'x').close()  # plik jest utworzony (pusty), jeżeli jest to wyświetli x
    print('Plik został utworzony', path)


# result = os.path.isfile(path) or open(path, "x").close() # czy plik istnieje - or - lub utwórz
# print(result) # True
