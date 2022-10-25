# Ta klasa jest "iterable" - można obiekt csvreader przetwarzać pętlą for, jednak czy ta klasa ma iterator?
import csv
 
with open('E:/Python/00 Python_DC/temp/data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Uruchom program i zobacz jak on aktualnie dziala
# Zakomentuj dwie ostatnie linie skryptu (pętla for)

#    for row in csvreader:
#        print('|'.join(row))

# Najpierw "próbnie" spróbuj pobrać zawartość kolejnych linijek pliku CSV korzystając z kilku ręcznych wywołań funkcji next
# Jeśli funkcja next działa, to.... obiekt ma swój iterator i nie trzeba korzystać z funkcji iter()

# Napisz pętlę while wykonującą się w nieskończoność
    while True:
        try:
# w tej pętli napisz try/except pobierający kolejny element z obiektu csvreader
            data = next(csvreader)
            print(data)
        except StopIteration:
            break
    print('Wszystkie dane zostały przetworzone')
# jeśli dojdzie do błędu StopIteration, to przerwij wykonanie pętli

