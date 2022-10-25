import datetime as dt

class MilionDays:       # obiekt iterable, który nie posiada własnego iteratora __iter__
                        # posiada metodę __getitem__ pozwala odwoływać się do poszczególnych elementów generowanych przez class MilionDays
                        # nie ma problemu dla polecenia for, ale jest problem dla polecenia next (potrzebuje zdefiniowania dodatkowego iteretora)   

    def __init__(self, year, month, day, maxdays):
        self.date = dt.datetime(year, month, day)
        self.maxdays = maxdays

    def __getitem__(self, item):
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration()

md = MilionDays(2000,1,1,10)

# print(md[0], md[1], md[2], md[10])

it = iter(md)   # dodatkowy iterator dla next

print(next(it))
print(next(it))
print(next(it))

for d in md:
    print(d)
