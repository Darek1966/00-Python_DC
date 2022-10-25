
workDays = [19, 21, 22, 21, 20, 22]  # lista dni roboczych w poszczególnych miesiącach

print(workDays) # [19, 21, 22, 21, 20, 22]

print (workDays[3]) # 21

enumeratedDays = list(enumerate(workDays))
print(enumeratedDays) # [(0, 19), (1, 21), (2, 22), (3, 21), (4, 20), (5, 22)]

for pos, value in enumeratedDays:
    print('pozycja', pos, 'wartość', value)
'''
pozycja 0 wartość 19
pozycja 1 wartość 21
pozycja 2 wartość 22
pozycja 3 wartość 21
pozycja 4 wartość 20
pozycja 5 wartość 22
'''
