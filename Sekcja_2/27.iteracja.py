
workDays = [19, 21, 22, 21, 20, 22]
miesiące = ['I', 'II', 'III', 'IV', 'V', 'VI']

miesiącDzień = dict(zip(miesiące, workDays))
print(miesiącDzień) # powstanie słownik {klucz, wartość}

for key in miesiącDzień:
    print('Klucz to', key, 'Wartość to', miesiącDzień[key])

for value in miesiącDzień.values():
    print('Wartość to', value)

