
from turtle import clear


instrukcja = ['cześć', 'jak się masz', 'wyjście', 'masz pieniądze','dziekuję','bay bay']
instrukcjaStart = []

for instr in instrukcja:              # else dla pętli for
    print('Powiedz coś:', instr)
    instrukcjaStart.append(instr)

    if instr == 'wyjście':
        print('Wychodzę!!!')
        instrukcjaStart.clear()
        break
else:  # else zadziała jak nie wykona się break
    print('Kończę akcję i wychodzę:', instrukcjaStart) # else zadziała jak brak 'wyjście'


print('-' *30)
instrukcjaStart.clear()

i = 0    # dla while potrzebna zmienna sterująca
while i < len(instrukcja):              # else dla pętli while
    print('Powiedz coś:', instrukcja[i])
    instrukcjaStart.append(instrukcja[i])

    if instrukcja[i] == 'wyjście':
        print('Wychodzę!!!')
        instrukcjaStart.clear()
        break
    i += 1

else:  # else zadziała jak niewykona się break
    print('Kończę akcję i wychodzę:', instrukcjaStart) # else zadziała jak brak 'wyjście'
