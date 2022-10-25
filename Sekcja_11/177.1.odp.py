
# Jak widać ta klasa nie jest context managerem, ale my to zmienimy:
# zaimportuj moduł contextlib
import os
import zipfile
import requests
import contextlib
 
 
class FileFromWeb:
 
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file
 
    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
# A teraz trochę popsujemy... :
# 1/. w metodzie close zakomentuj wyrażenie if. Niech instrukcja usuwająca plik wykonuje się bezwarunkowo
# 2/. uruchom kod - powinien działać poprawnie
    def close(self):
        #if os.path.isfile(self.tmp_file):
        os.remove(self.tmp_file)

# Naprawmy to:
# 5/. Dodany w poprzednich krokach blok with umieść w kolejnym bloku with, który "ukryje" wyjątek FileNotFoundError
with contextlib.suppress(FileNotFoundError):
 
    with contextlib.closing(FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'E:/Python/00 Python_DC/temp/euroxref1.zip')) as f:

# zmień linijkę tworzącą instancję (f = FileFromWeb...) na instrukcję with tak, 
# że do utworzenia context managera wykorzystasz metodę closing z modułu contextlib 
        f.download_file()
 
        with zipfile.ZipFile(f.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir('E:/Python/00 Python_DC/temp')
            z.extract(a_file, '.', None)

# 3/. odkomentuj ostatnią linijkę usuwającą plik. 
# 4/. Uruchom ponownie skrypt, który tym razem powinien się kończyć błędem.
        os.remove(f.tmp_file)
