
import datetime as dt
import sys

start = dt.datetime.now()
print('Egzekucja rozpoczęła się o: {}'.format(start))

# dates = [dt.date(2000,1,1) + dt.timedelta(days=i) for i in range(2500000)]
# print('rozmiar dat to{}'.format(sys.getsizeof(dates)))
# for d in dates:                                           # zajmuje dużo pamięci
#    pass

class MilionDays:           # klasa - jako - iterator (zajmuje dużo mniej pamięci komputera)

    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays

    def __next__(self):
        if self.maxdays <=0:
            raise StopIteration()
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1
        return ret
        
# md = MilionDays(2000,1,1,2500000)
# print('rozmiar dat to {}'.format(sys.getsizeof(md)))    # rozmiar pliku w bajtach
# print(next(md))
# print(next(md))
# print(next(md))

# for i in range (2500000):
#    next(md)

    def __iter__(self):
        return self

md = MilionDays(2000,1,1,2500000)
print('rozmiar dat to {}'.format(sys.getsizeof(md)))
for d in md:
    pass

stop = dt.datetime.now()
print('Egzekucja rozpoczęła się o: {}'.format(stop))
print('Czas całkowity:  {}'.format(stop - start))
