
import datetime as dt

class MilionDaysIterator:          # jest iteratorem ale nie jest iterable

    def __init__(self, date, max):
        self.date = date
        self.maxdays = max
    
    def __next__(self):
        if self.maxdays <=0:
            raise StopIteration()
        ret = self.date
        self.maxdays -= 1
        self.date += dt.timedelta(days=1)
        return ret     
    '''
    def __iter__(self):     # nie jest potrzebne
        return self
    '''

class MilionDays:      # jest iterable ale nie posiada własnego iteratora

    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays
        self.iterator = MilionDaysIterator(self.date, self.maxdays)


    def __iter__(self):
        return self.iterator

md = MilionDays(2000,1,1,3)
print(next(iter(md)))       # next też działa w takiej postaci
for d in md:
    print(d) 

