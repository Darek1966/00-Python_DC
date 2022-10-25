
aTuple = (1, 2, 3, 4, 5)    # obiekt iterable (można przejść pętlą for)

for x in aTuple:
    print(x)

# print(next(aTuple))     # next nie można wywołać, nie ma własnego iteratora

# it = iter(aTuple)         # własny iterator dla next
'''
print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''
print('--------------------------------------------')
aList = [1, 2, 3, 4, 5]      # obiekt iterable (można przejść pętlą for)
'''
for i in aList:
    print(i)
'''
# print(next(aList))      # next nie można wywołać, nie ma własnego iteratora
'''
it = iter(aList)          # własny iterator dla next

print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''
aSet = {1, 2, (3, 4), 'another element', 3, 4}  # obiekt iterable (można przejść pętlą for)
'''
for i in aSet:
    print(i)
'''

# print(next(aSet))        # next nie można wywołać, nie ma własnego iteratora
'''
it = iter(aSet)          # własny iterator dla next

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''
# with open('E:/Python/00 Python_DC/temp/lines.txt', 'r') as file:     # obiekt iterable (można przejść pętlą for)
#    for line in file:
#        print(line)
''' 
with open('E:/Python/00 Python_DC/temp/lines.txt', 'r') as file:     
    while True:
        print(next(file))   # przejdzie wszystkie i będzie stopIteration
'''
with open('E:/Python/00 Python_DC/temp/lines.txt', 'r') as file:     # obiekt iterable i ma włssny iterator
    while True:
        try:
            print(next(file))
        except StopIteration:
            break  
 