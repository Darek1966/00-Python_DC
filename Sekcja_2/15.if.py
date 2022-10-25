
dzień = 2 # można zmieniać wartość

weekend = 1
zwykłyDzień = 2
święto = 3

if dzień ==1 :  # if - jeśli - zrób
    # print(dzień)
    pass # pass - nic nie rób

elif dzień == 2:  # elif - w przeciwnym wypadku - zrób
    # print(dzień)
    pass  # może to być miejsce, które później uzupełnimy

else:              # else - inaczej - w pozostałych przykadkach - zrób
    # print(dzień)
    pass

dzieńOpis = 'weekend' if dzień == 1 else 'zwykłyDzień' if dzień == 2 else 'święto' # w jednej linii - uproszczone
print(dzieńOpis)

