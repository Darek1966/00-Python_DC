
'''
Piszesz funkcję log_it, która ma zapisać w pliku tekstowym np. log_it.txt przesłane do funkcji argumenty. 
Funkcja będzie wykorzystywana w innych miejscach programu, gdzie będzie wywoływana w strategicznych momentach, 
dokumentując działanie programu. Jeśli nie masz innych pomysłów to zadbaj o to aby:
można było przesłać dowolną ilość argumentów
podczas dopisywania informacji do pliku poszczególne argumenty rozdzielaj spacją
na końcu w pliku zapisz ENTER, aby kolejne wywołanie funkcji dopisywało od nowej linijki
'''
def log_it(*args):
 
    path = r'E:\Python\00 Python_DC\Sekcja_4\log_it.txt'
    with open(path, "a") as f:
 
        for line in args:
            f.write(line)
            f.write(' ')
 
        f.write("\n")
 
log_it('Rozpoczecie prognozowania przetwarzania')
log_it('ERROR', 'Niewystarczajace dane', 'faktury', '2022', 'lipiec', 'drugi tydzien', 'ENTER')
