
import os
import zipfile
import requests
 
class FileFromWeb:
 
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file
 
    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
# Dodaj do tej klasy w __exit__ obsługę błędów:
# jeśli w przedostatniej linijce zmieniasz katalog na nieistniejący, to zostanie wygenerowany błąd: FileNotFoundError
# Należy tylko wyświetlić odpowiedni komunikat o błędzie (ukryć prawdziwą przyczynę)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('>>>>>>>>>>> Error details',exc_type, exc_val, exc_tb)
# jeśli w ostatniej linijce użytkownik poprosi o wypakowanie nieistniejącego pliku to zostanie wygenerowany błąd: KeyError
# Należy tylko wyświetlić odpowiedni komunikat o błędzie (ukryć prawdziwą przyczynę)
        if exc_type == KeyError:
            print('>>>>> There is no file in archive! {}'.format(exc_val))
            return True
# w pozostałych przypadkach błąd ma być zgłoszony na zewnątrz
        elif exc_type == FileNotFoundError:
            print('>>>>> Incorrect directory/file: {}'.format(exc_val))
            return  True
        else:
            return False
 
 
with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'E:/Python/00 Python_DC/temp/euroxref.zip') as f:
 
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('E:/Python/00 Python_DC/temp')
        z.extract(a_file, '.', None)

# Uwaga! Jeśli do błędu dochodzi w metodzie __enter__, to pokazana na tej lekcji metoda nie zadziała,
# bo wtedy blok with wcale się nie wykonuje, nie ma więc też metody __exit__
