
clients = {
    "INFO" : 0.5,
    "DATA" : 0.2,
    "SOFT" : 0.2,
    "INTER" : 0.1,
    "OMEGA" : 0.0
}

# celowo wprowadzamy nieprawidłowe działanie
# x = 1/0
# w terminalu komunikat: ZeroDivisionError: division by zero

# print(clients['ABC'])
# w terminalu komunikat: KeyError: 'ABC'

# x = float('ABC')
# w terminalu komunikat: ValueError: could not convert string to float: 'ABC'

myClient = input("Wpisz nazwę klienta: ")
totalCost = 7200

try:
    ratio = float(input("Wprowadź nowy stosunek: "))     
    print(" % stosunek domyślny {} wynosi {}, nowy to {}".format(myClient, clients[myClient], ratio))
    print("Koszt dla {} wynosi {}".format(myClient, ratio * totalCost))
    print("Nowy stosunek w porównaniu do starego stosunku wynosi:  {}".format(clients[myClient]/ratio))

except KeyError as e:
    print("Klienta {} nie ma na liście{}.\nDetal:\n{}".format(myClient, [ c for c in clients.keys()], e))

except ValueError as e:
    print("Problem, wprowadzona zła wartość - musi być liczba.\nDetal: {}".format(e))

except ZeroDivisionError as e:
    print("Ten błąd powstaje jak dzielisz przez zero.\nDetal:\n- {}".format(e))

except Exception as e:         
    print("Przepraszamy, mamy błąd..........\nDetal:\n {}".format(e))
   