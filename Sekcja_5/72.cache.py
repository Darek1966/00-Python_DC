import time

def Factorial(n):  # factorial - silnia
    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)
start = time.time()
for i in range(1, 11):     # silnia liczb od 1 do 10
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()
print('Execution time', stop - start)
'''
Wolno liczy (ponad 6 sek.):
1! = 1
2! = 2       
3! = 6       
4! = 24      
5! = 120     
6! = 720     
7! = 5040    
8! = 40320   
9! = 362880  
10! = 3628800
'''
