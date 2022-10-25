
projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
'''
Korzystając ze "sprytnej" metody pracy z for wyświetl komunikaty w postaci:
The leader of "...nazwa projektu..." is ...imię i nazwisko lidera...
'''
for p, l in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(p,l))

'''
Utwórz kolejną listę z datami rozpoczęcia projektów:
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...
'''
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p, l,d in zip(projects, leaders, dates):
    print('The leader of "{}" started {} is {}'.format(p,d,l))
 
'''
Korzystając ze "sprytnego" złożenia enumerate i zip - dodaj do komunikatu dodatkowo numer kolejny projektu rozpoczynając od 1:
...numer kolejny... - The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...
'''
for i, (p,l,d) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1,p,d,l))
    