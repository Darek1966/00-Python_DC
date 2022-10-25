'''
Administrator systemu chciałby wiedzieć, ile plików i katalogów znajduje się w określonym katalogu. 
Słyszał, że da się to zrobić w Pythonie i w sumie ma racje...
'''

# Zaimportuj moduł os i itertools
import os
import itertools
 
# Napisz generator scantree, który:
# jako argument przyjmie ścieżkę do początkowego katalogu path
def scantree(path):

    '''
następnie dla każdego obiektu zwracanego przez os.scandir:
(zobacz dokumentację - https://docs.python.org/3/library/os.html#os.scandir 
- obiekty zwracane przez os.scandir to obiekty klasy os.DirEntry - https://docs.python.org/3/library/os.html#os.DirEntry)

jeżeli obiekt ten jest katalogiem, czyli metoda obiektu is_dir() zwraca True
zwraca ten obiekt korzystając z yield
wywołuje rekurencyjnie scantree dla tego katalogu
jeżeli obiekt jest plikiem, czyli metoda obiektu is_dir() zwraca False
zwraca ten obiekt korzystając z yield
    '''
    for entry in os.scandir(path):
        if entry.is_dir():
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry

'''
Przetestuj działanie tej funkcji na wybranym przez siebie nie za dużym katalogu:
do zmiennej listing zapisz wynik wywołania scantree wskazując argumentem na wybrany katalog
następnie przejdź przez listing pętlą for i dla każdego obiektu wyświetl informację o tym 
czy jest to plik czy katalog oraz pełną ścieżkę do tego pliku/katalogu
'''
listing = scantree('E:/Python/00 Python_DC/temp')
for l in listing:
    print('DIR ' if l.is_dir() else 'FILE', l.path)
 
 
listing = scantree('E:/Python/00 Python_DC/temp')
listing = sorted(listing, key=lambda e: e.is_dir())

''' 
Korzystając z funkcji groupby z modułu itertools wyświetl informację o ilości katalogów
 i plików w wybranym przez ciebie katalogu bazowym. 
 Pamiętaj o ponownym utworzeniu zmiennej listing posortowaniu obiektu listing
'''
for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))
