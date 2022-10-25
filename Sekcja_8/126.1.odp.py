
import requests
import os
import shutil
import urllib3.exceptions
 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
 
 
url = 'http://www.mobilo24.eu/spis/'
dir = 'E:/Python/00 Python_DC/temp/'
tmpfile = 'download.tmp'
file = 'spis_1.html'
 
tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)
 
try:
    if os.path.exists(tmpfile_path):
        print('Removing {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
        
    print('Downloading url {}'.format(url))
    save_url_to_file(url, tmpfile_path)
    
    print('Copying file {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)

# requests.exceptions.ConnectionError - ten błąd łatwo sprowokujesz wpisując nieprawidłowy adres URL
except requests.exceptions.ConnectionError:
    print('Error downloading the file. The URL {} is incorrect'.format(url))

# FileNotFoundError - może się pojawić w trakcie prób, gdy plik download.tmp nie będzie istniał, a wykonywać będzie się instrukcja kopiowania plików 
except FileNotFoundError:
    print('File cannot be found: {}'.format(tmpfile_path))

# PermissionError - ten błąd uzyskasz zaznaczając atrybut "tylko do odczytu" dla pliku spis.html 
except PermissionError:
    print('Problem accessing a file: {}'.format(file_path))

# Exception - ogólna obsługa błędów "na wszelki wypadek   
except Exception as e:
    print('General Error downloading the URL {}'.format(url))
    print('Error details: {}'.format(e))
    
else:
    print('URL downloaded successfully {}'.format(file))
    
finally:
    if os.path.exists(tmpfile_path):
        print('Final removal of the file {}'.format(tmpfile_path))
        os.remove(tmpfile_path) 
    print('DONE!')
