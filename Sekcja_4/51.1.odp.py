'''
W tym zadaniu zbudujesz proces służący do budowy łańcucha transformacji danych liczbowych.
Utwórz w swoim skrypcie następujące funkcje:
'''
def double(x):
    return 2 *x
 
def square(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2

# Zdefiniuj liczbę number o wartości 8
number = 8

# Zdefiniuj listę transformations składającą sie z funkcji:
transformations = [double, square, div2, negative]
 
print('Starting transformations')
# Do tymczasowej zmiennej tmp_return_value wpisz wartość number
tmp_return_value = number

'''
Napisz pętlę, która:
przejdzie przez wszystkie pozycje listy transformations
za każdym razem wywoła odpowiednią funkcję, przekazując do niej aktualną wartość argumentu tmp_return_value
wyświetli aktualną wartość zmiennej tmp_return_value
'''
for transformation in transformations:
 
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))

'''
Przetestuj działanie skryptu również dla listy transformacji z operacjami:
[square, square, div2, double]
'''
number = 125
transformations = [square, square, div2, double]
      
print('Starting transformations')
tmp_return_value = number
for transformation in transformations:
 
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))
