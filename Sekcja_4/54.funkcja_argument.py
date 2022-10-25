
def Upiecz(what):
    print('Pieczenie {}'.format(what))

def Dodaj(what):
    print('Dodaj {}'.format(what))

def Mieszaj(what):
    print('Miksuj {}'.format(what))

przepis = [(Dodaj, 'mleko'), (Dodaj, 'maka'), (Dodaj, 'cukier'), (Mieszaj, 'intensywnie'), (Upiecz, 'ciasto')]

# pierwsza metoda
for activity, obj in przepis:
    activity(obj)

print('-'*30)

# druga metoda
def Ugotuj(activity, obj):
    activity(obj)

Ugotuj(Upiecz, 'ciasteczka')

for activity, obj in przepis:
    Ugotuj(activity, obj)
