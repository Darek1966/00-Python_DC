
clients = {
    "INFO" : 0.5,
    "DATA" : 0.2,
    "SOFT" : 0.2,
    "INTER" : 0.1,
    "OMEGA" : 0.0
}

myClient = input("Wpisz nazwe klienta: ")
totalCost = 7200

# obsługa błędu (wpisany np. ABC którego nie ma w słowniku)
try:      
    print(" % stosunek {} wynosi {}".format(myClient, clients[myClient]))
except Exception as e:          # wykona się jak będzie błąd i zakończy działanie
    print("Przepraszamy, mamy bład..........\n Detal:\n {}".format(e))
else:                           # wykona się jak nie będzie błędów
    print("Rachunek dla {} wynosi {}".format(myClient, clients[myClient] * totalCost))
finally:                        # wykona się zawsze, niezależnie czy jest błąd czy nie
    print("-= Obliczenia zakonczone =-")
