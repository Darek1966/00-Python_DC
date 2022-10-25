'''
Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim szefem 
otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:
'''
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
 
'''
Zbuduj listę tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym
 '''
routes = [ (start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))
'''
Wyeliminuj z powyższej listy połączenie z portu do tego samego portu
'''
routes = [ (start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))
'''
Ponieważ połączenie z A do B dubluje się z połączeniem z B do A 
- wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.
''' 
routes = [ (start, stop) for start in ports for stop in ports if start < stop]
print(routes)
'''
Policz ilość generowanych połączeń w krokach 1,2,3
'''
print(len(routes))
