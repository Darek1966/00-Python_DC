
from logging import Filterer


def double (x):  # prosta funkcja
    return x * 2

x = 10
x = double(x)
print(x)

# główna zasada funkcji lambda
x = 10
f = lambda x: x * 2  # funkcja bez nazwy tzw. anonimowa
print(f(x))

######################################################
# drugi przykład
def power(x, y):
    return x ** y    # ** do potęgi

x = 5
y = 3
print(power(x, y))

# to samo z lambda
f = lambda x, y: x ** y
print(f(x, y))

######################################################

list_numbers = [1, 2, 3, 4, 11, 14, 15, 20, 21]

def is_odd(x):              # wyłuskanie liczb nieparzystych
    return x % 2 !=0

print(is_odd(7), is_odd(4))

# funkcja filter

filtered_list = list(filter(is_odd, list_numbers))
print(filtered_list)
# [1, 3, 11, 15, 21]

# z lambda

filtered_list = list(filter(lambda x: x % 2 !=0, list_numbers))
print(filtered_list)
# [1, 3, 11, 15, 21]

# jeszcze prościej
print(list(filter(lambda x: x % 2 != 0, list_numbers)))
# [1, 3, 11, 15, 21]

#######################################################

def generate_multiply_funkcjon(n):
    return lambda x: n * x
mul_2 = generate_multiply_funkcjon(2)
mul_3 = generate_multiply_funkcjon(3)

print(mul_2(13), mul_3(8))
# 26 24
