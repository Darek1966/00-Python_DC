
import datetime

netto = 100
brutto = 120
# netto powinno być zawsze mniejsze lub równe brutto
assert netto <= brutto, 'Netto powinno być mniejsze lub równe brutto'

orderDate = datetime.date(2022,10,13)       # order - zamówienie
deliveryDate = datetime.date(2022,10,18)    # delivery - dostawa
# data zamówienia powinna być wcześniejsza niż data dostarczenia
assert orderDate <= deliveryDate, 'Data dostawy nie może być wcześniejsza niż data zamówienia'
