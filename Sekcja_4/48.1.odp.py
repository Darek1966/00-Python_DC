'''
Przygotowujesz program dla sklepu z farbami. Klienci pytają czasami ile farby potrzeba do pomalowania mieszkania.
Napisz funkcję calculate_paint, która:
przyjmuje argument efficency_ltr_per_m2 - określającą ile farby trzeba do pomalowania metra kwadratowego
przyjmuje dowolną ilość kolejnych argumentów odpowiadających za powierzchnie do pomalowania dla pokoi mieszkania,
które ma być pomalowane funkcja ma zwracać informację o ilości potrzebnej farby.
Przetestuj funkcję na dwa sposoby:
przekazując powierzchnie do pomalowania w poszczególnych pokojach po prostu po przecinku wywołując funkcję
definiując listę z powierzchniami, a następnie przekazując do funkcji tą listę
'''
def calculate_paint(efficency_ltr_per_m2, *rooms):
 
    total_area = sum(rooms)
    paint = total_area * efficency_ltr_per_m2
    return paint

# pierwszy sposób (0.25 na m2, powierzchnia pokoi: 42, 28, 30)
print(calculate_paint(0.25, 42, 28, 30))

# drugi sposób
rooms = [42, 28, 30]
print(calculate_paint(0.25,*rooms))    
