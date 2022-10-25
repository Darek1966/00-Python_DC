
def ProcessInvoice(netto, brutto):

    if netto >= brutto:
    #    raise Exception('Netto nie może być większe niż brutto')  # zgłaszanie błędu - inny zapis

        raise ValueError('Netto nie może być większe niż brutto')
    else:
        print('Przetwarzanie faktury: netto={}, brutto={}'.format(netto, brutto))

def EndOfMonth():
    netto = 1250
    brutto = 1000   # błędna wartość: brutto < netto

    try:
        ProcessInvoice(netto, brutto)
    
    except ValueError as e:
        print('Wartości na fakturze są nieprawidłowe: {}'.format(e))
        raise ValueError('Błąd podczas przetwarzania faktur') from e

    except Exception as e:
        print('Błąd przetwarzania faktury: {}'.format(e))
        raise Exception('Ogólny błąd podczas przetwarzania faktur')


EndOfMonth()
