
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
 
'''
Zbuduj generator tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym
'''
routes = ( (start, stop) for start in ports for stop in ports)
 
'''
Wyeliminuj z powyższego generatora połączenie z portu do tego samego portu
'''
counter=0
for (start, stop) in routes:
    print("{} - {}".format(start, stop))
    counter+=1
          
print(counter)
 
'''
 Ponieważ połączenie z A do B dubluje się z połączeniem z B do A 
 - wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.
'''
 
routes = ( (start, stop) for start in ports for stop in ports if start != stop)
 
counter=0
for (start, stop) in routes:
    print("{} - {}".format(start, stop))
    counter+=1
          
print(counter)
 
'''
Policz ilość generowanych połączeń w krokach 1,2,3. 
W tym celu napisz pętlę for, która: wyświetli wygenerowane wartości i policzy je
'''
 
routes = ( (start, stop) for start in ports for stop in ports if start < stop)
 
counter=0
for (start, stop) in routes:
    print("{} - {}".format(start, stop))
    counter+=1
          
print(counter)
