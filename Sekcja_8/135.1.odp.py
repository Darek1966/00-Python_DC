
import datetime as dt

# Zdefiniuj klasę TripException, która rozszerzy ilość informacji przedstawianych podczas błędu. 
# Klasa ta będzie przechowywać po prostu dodatkowy atrybut description:
class TripException(Exception): # klasa ma dziedziczyć z Exception
 
    def __init__(self, text, description):  # metoda __init__ ma przyjąć argumenty text i description
        super().__init__(text)          # text zostanie przekazany podczas wywoływania metody __init__ klasy rodzicielskiej
        self.description = description  # description zostanie zapisane jako lokalny atrybut
# metoda __str__ ma zwracać to co zwróciłaby klasa rodzicielska, a dodatkowo informacje zapisane w atrybucie description 
    def __str__(self):
        return "{}, info: {}".format(super().__str__(), self.description)
 
# Zdefiniuj klasę TripNameException dziedziczącą z TripException. 
# Ten rodzaj błędu będzie zgłaszany zawsze wtedy, gdy pojawi się problem z nazwą wycieczki. 
# Wszystkie te błędy będą miały wspólne description, dlatego zdefiniujemy je na stałe w __init__: 
class TripNameException(TripException):
 
    def __init__(self, text): # metoda __init__ ma przyjąć tylko argument text
# argument text zostanie przekazany jako pierwszy argument do __init__ klasy rodzicielskiej
# drugi argument może być bardziej rozbudowanym opisem usterki, np. 'Name of the trip is missing. You need to name the trip somehow...'
        super().__init__(text, 'Name of the trip is missing. You need to name the trip somehow...')
 
# Zdefiniuj klasę TripDateException dziedziczącą z TripException. 
# Ten rodzaj błędu będzie zgłaszany zawsze wtedy, gdy pojawi się problem z datami wycieczki. 
# Wszystkie te błędy będą miały wspólne description, dlatego zdefiniujemy je na stałe w __init__: 
class TripDateException(TripException):
 
    def __init__(self, text):  # metoda __init__ ma przyjąć tylko argument text
# argument text zostanie przekazany jako pierwszy argument do __init__ klasy rodzicielskiej
# drugi argument może być bardziej rozbudowanym opisem usterki, np. 'The dates are incorrect. 
# The starting date should be earlier than the ending date...'
        super().__init__(text, 'The dates are incorrect. The starting date should be earlier than the ending date...')
 
 
class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
# Zmień wyjątki zgłaszane w metodzie check_data
    def check_data(self):
        if len(self.title) == 0:
# w pierwszym przypadku zgłoś TripNameException i skróć tekst przekazywany jako argument
            raise TripNameException("Name error")
        if self.start > self.end:
# w drugim przypadku zgłoś TripDateException i też skróć tekst przekazywany jako argument
            raise TripDateException("Date error")
# W metodzie publish_offer:
# obsłuż nowe rodzaje błędów: TripNameException  i TripDateException
    @classmethod
    def publish_offer(cls, trips):
 
        list_of_errors = []
 
        for trip in trips:
            try:
                trip.check_data()
            except TripNameException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except TripDateException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
# z kolei zgłaszając błąd wykorzystaj TripException przekazując jako argumenty
# tekst - "The list of trips has errors"
# i jako drugi argument list_of_errors       
        if len(list_of_errors) > 0:
            raise TripException("The list of trips has errors", list_of_errors)
        else:
            print('the offer will be published...')
        
 
trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]
 
try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')
    