
class Door:                     # door - drzwi
    def __init__(self, where):
        self.where = where

    def open(self):
        print('Openig door to the {}'.format(self.where))

    def close(self):
        print('Closing door to the {}'.format(self.where))
'''
door1 = Door('hell')        # hell - piekło
door2 = Door('future')      # future - przyszłość

door1.open()
door1.close()
door2.open()
door2.close()
'''
from contextlib import contextmanager

# @contextmanager

#def OpenAndClose(obj):
#   obj.open()
#   yield obj
#   obj.close()

#with OpenAndClose(Door('next room')) as door:
#   print('the dore is to the {}'.format(door.where))


#def OnlyClose(obj):
#    yield obj
#   obj.close()

#with OnlyClose(Door('next room')) as door:
#    door.open()
#    print('the dore is to the {}'.format(door.where))

'''
from urllib.request import urlopen
from contextlib import closing

with closing(urlopen('http://www.kursyonline24.eu')) as page:
    for line in page:
        print(line)
'''

'''
import os

# os.remove(r'E:\Python\00 Python_DC\temp\myk.ini')   # usuwanie pliku

from contextlib import suppress
with suppress(FileNotFoundError):   # nie wyświetli błędu, że nie ma pliku do usunięcia
    os.remove(r'E:\Python\00 Python_DC\temp\myk.ini')
'''

from contextlib import redirect_stdout      # plik gromadzi komunikaty
f = open(r'E:\Python\00 Python_DC\temp\log.txt', 'w')
with redirect_stdout(f):
    print('Hello')
    d = Door('Exit')
    d.open()
    d.close()
