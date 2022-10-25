'''
Oto otrzymałeś specjalne zadanie. Trzeba napisać klasę, która będzie odpowiedzialna za:
- pobranie pliku zip z Internetu
- zapisanie go we wskazanej lokalizacji
Twoja nowa klasa ma być wykorzystywana jako Context Manager. 
Aktualnie istnieje plan pobrania pliku zip i rozpakowywania jego zawartości, 
ale to ma się już zadziać w Context Managerze poza klasą. Jeśli wiesz jak to zrobić, 
to do dzieła, a jak chcesz dokładniejszych instrukcji to patrz:
'''

# zaimportuj moduły os, zipfile i requests
import os
import zipfile
import requests

'''
- zdefinuj klasę FileFromWeb
- w metodzie __init__ przyjmij i zapamiętaj parametry
- url - zawierający adres pliku do pobrania
- tmp_file - wskazujący gdzie ten plik ma być zapisany
'''
class FileFromWeb:
 
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file
    '''
    w metodzie __enter__
    - do zmiennej response zapisz wynik wywołania requests.get(self.url)
    - otwórz do zapisu w trybie binarnym plik wskazywany ścieżką self.tmp_file
    - zapisz w tym pliku response.content
    - zwróć obiekt self
    '''
    def __enter__(self):
        #download
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
# w metodzie __exit__ nic nie rób
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

'''
wykorzystaj klasę pisząc wyrażenie with:
- utwórz instancje klasy FileFromWeb korzystając z argumentów (gdyby adres web nie odpowiadał, to zmień go na dowolny inny plik zip):
- https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip
- c:/temp/euroxref.zip
- nadaj instancji alias f
- w bloku with utwórz następne wyrażenie with - utwórz instancję klasy zipfile.ZipFile - przekaż jako argumenty:
- f.tmp_file - czyli ścieżkę do lokalnie zapisanego pliku zip
- "r" - czyli informację, że plik będzie otwierany na odczyt
- nadaj obiektowi alias z
- w bloku with:
- pobierz nazwę pierwszego pliku znajdującego się w archiwum zip korzystając z metody z.namelist()[0]. Zapisz wynik w zmiennej a_file
- wyświetl zmienną a_file (tylko w celu kontroli)
- zmień bieżący katalog na wybrany np. c:/temp - skorzystaj z metody chdir modułu os
- wypakuj plik korzystając z metody obiektu z o nazwie extract. Argumenty to:
- nazwa pliku do wypakowania - tutaj a_file
- nazwa katalogu do jakiego plik ma być wypakowany - przekaż kropkę
- hasło do otwarcia archiwum - przekaż None
'''
with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'E:/Python/00 Python_DC/temp/euroxref.zip') as f:
 
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('E:/Python/00 Python_DC/temp')
        z.extract(a_file, '.', None)
 