
workDays = [19, 21, 22, 21, 20, 22]  # lista dni roboczych w poszczególnych miesiącach


enumeratedDays = list(enumerate(workDays))
print(enumeratedDays) # [(0, 19), (1, 21), (2, 22), (3, 21), (4, 20), (5, 22)]

for pos, value in enumeratedDays:
    print('pozycja', pos, 'wartość', value)

miesiące = ['I', 'II', 'III', 'IV', 'V', 'VI']

miesiącDzień = list(zip(miesiące, workDays))
print(miesiącDzień)

for m, d in miesiącDzień:
    print('Miesiąc', m, 'Dzień', d)

for pos, (m, d) in enumerate(zip(miesiące, workDays)):
    print('Pozycja', pos, 'Miesiąc', m, 'Dzień', d)

