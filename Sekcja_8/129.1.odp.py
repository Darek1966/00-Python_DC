
import datetime as dt
 
class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

# Twoim zadaniem jest napisanie metody klasy o nazwie publish_offer, która:
# jako argument przyjmie listę wycieczek 
    @classmethod
    def publish_offer(cls, trips):
# zadeklaruje lokalną listę list_of_errors, w której będą zapamiętane wyniki testu dla wycieczek zawierających błędy 
        list_of_errors = []
# dla każdej wycieczki z listy list_of_errors wywoła metodę check_data
        for trip in trips:
            try:
                trip.check_data()
# jeżeli błąd to ValueError, to do list_of_errors doda napis  w postaci "<symbol_wycieczki>: <treść błędu>"
            except ValueError as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
# jeżeli błąd to Exception, to do  list_of_errors doda napis  w postaci "<symbol_wycieczki>: <treść błędu>"
            except Exception as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
# jeżeli po sprawdzeniu wszystkich wycieczek w list_of_errors są jakieś błędy, to zgłosi exception o treści "The list of trips has errors: <lista_błędów>"        
        if len(list_of_errors) > 0:
            raise Exception("The list of trips has errors: {}".format(list_of_errors))
# w przeciwnym razie wyświetli komunikat "the offer will be published..." (normalnie w tym miejscu odbywałoby się publikowanie wycieczek, ale my ten punkt pomijamy)
        else:
            print('the offer will be published...')
        
 
trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]
# w bloku try:
# najpierw zostanie wyświetlony komunikat o rozpoczęciu sprawdzania wycieczek
# potem będzie wywołana metoda publish_offer
# na zakończenie zostanie wyświetlony napis "done" 
try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
# w bloku except: jeśli doszło do błedu,
#  wyświetl "przerażający" komunikat o błędzie i szczegóły tego błędu
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')

'''
W tym ćwiczeniu zobaczyłeś, jak można skumulować kilka mniejszych błędów w jeden większy. 
Użytkownik od razu mógł zobaczyć wszystkie wadliwe dane, dokonać korekt i ponownie uruchomić swój program.
'''