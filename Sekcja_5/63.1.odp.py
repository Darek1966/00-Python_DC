'''
Pracujesz nad aplikacją, która intensywnie pracuje z plikami. 
Klient zażyczył sobie, aby każda taka operacja została dodatkowo zalogowana. 
Log powinien mieć postać mniej więcej taką:
Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:29:17
Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2029-01-12 9:33:18
Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:39:57
Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2029-01-12 9:44:18
Wiadomo, że:
- wszystkie te funkcje przyjmują jeden parametr path (więc mogą korzystać z takiego samego wrappera)
- klient może chcieć zapisać dane logowania oddzielnie do innego pliku dla każdej funkcji (więc wrappery jednak czymś będą się nieznacznie różnić)
Chcesz rozwiązać problem stosując wrapper. 
Idealnie będzie napisać jedną funkcję  przyjmującą jako parametry:
- logged_action określającą wykonywaną czynność np. FILE_CREATE lub FILE_DELETE
- log_file_path określającą do jakiego pliku zapisywać informacje
'''
# zaimportuj moduł os, functools, a z modułu datetime zaimportuj  datetime aliasując go jako dt
import os
from datetime import datetime as dt
import functools
 
# Napisz funkcję wrapper_with_log_file, która: przyjmuje parametry logged_action, log_file_path
def wrapper_with_log_file(logged_action, log_file_path):
# w tej funkcji napisz funkcję wrapper_with_log_to_known_file, która:przyjmie parametr func - określający dla jakiej funkcji ma być utworzony wrapper    
    def wrapper_with_log_to_known_file(func):

# w tej funkcji napisz funkcję the_real_wrapper, która przyjmie argument path określający plik,  na jakim ma być wykonywana operacja tworzenia lub usuwania plików, która:
# otworzy plik log_file_path dopisując do niego dane
# zapisze informację o wykonywanej czynności logged_action, na jakim pliku była wykonywana ta akcja path, oraz datę i godzinę, kiedy to się stało dt.now().strftime("%Y-%m-%d %H:%M:%S")
# funkcja the_real_wrapper zwróci wynik wywołania funkcji func z parametrem path
# funkcja wrapper_with_log_to_known_file ma zwróć funkcję the_real_wrapper
        def the_real_wrapper(path):
           
            with(open(log_file_path,'a')) as f:
                f.write('Action {} executed on {} on {}\n'.format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
                 
            return func(path)
        
        return the_real_wrapper
# funkcja wrapper_with_log_file ma zwróć funkcję wrapper_with_log_to_known_file    
    return wrapper_with_log_to_known_file

# Oznacz funkcje: create_file - dekoratorem tworzącym wrapper z parametrami FILE_CREATE i ścieżką pliku log r'c:/temp/file_create.txt'
@wrapper_with_log_file('FILE_CREATE',r'E:\Python\00 Python_DC\Sekcja_5/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")

# Oznacz funkcje: delete_file - dekoratorem tworzącym wrapper z parametrami FILE_DELETE i ścieżką pliku log r'c:/temp/file_delete.txt
@wrapper_with_log_file('FILE_DELETE',r'E:\Python\00 Python_DC\Sekcja_5/file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)
 
 
create_file(r'E:\Python\00 Python_DC\Sekcja_5\dummy_file.txt')
delete_file(r'E:\Python\00 Python_DC\Sekcja_5\dummy_file.txt')
create_file(r'E:\Python\00 Python_DC\Sekcja_5\dummy_file.txt')
delete_file(r'E:\Python\00 Python_DC\Sekcja_5\dummy_file.txt')
