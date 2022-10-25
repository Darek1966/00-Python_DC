
list = list (range(10))
print('Lista:', list, type(list), id(list)) # ten sam id

list2 = list
print('Lista:', list2, type(list2), id(list2)) # ten sam id
# jak dodam nowy element do list2 to będzie on też w list

# rozwiązanie - copy
list2 = list.copy()
print('Lista:', list2, type(list2), id(list2)) # inny id

# inny sposób zamiast copy to slice
list2 = list[:]
print('Lista:', list2, type(list2), id(list2)) # inny id

print(list[5:7]) # [5, 6]

print(list[5: ]) # [5, 6, 7, 8, 9]

print(list[ : ]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list[ : -1]) # [0, 1, 2, 3, 4, 5, 6, 7, 8] 

print(list[5 : -1]) # [5, 6, 7, 8]

print(list[5 : -3]) # [5, 6]

print(list[ : 8 : 2]) # [0, 2, 4, 6]

print(list[ -1: 0 : -1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1] 

print(list[ -1:  : -1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
