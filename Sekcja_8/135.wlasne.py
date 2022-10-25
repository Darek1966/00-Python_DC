
class BITException(Exception):
    
    def __init__(self, text, area):     # area - powierzchnia
        super().__init__(text)
        self.area = area

    def __str__(self):
        return '{}, area {}'.format(super().__str__(), self.area)

class BITSecurityExeption(BITException):
    pass

class BITDataFormatExeption(BaseException):
    pass
'''
try:
    # zrób coś
    raise BITException('format pliku jest nieprawidłowy', 'Dane finansowe')
except BITException as e:
    print('Błąd aplikacji: {}'.format (e))

try:
    # zrób coś
    raise BITException('format pliku jest nieprawidłowy', 'Dane osobowe')
except BITException as e:
    print('Błąd aplikacji: {}'.format (e))
'''
# po utworzeniu class BITSecurityExeption i BITDataFormatExeption
try:
    # zrób coś
    raise BITException('format pliku jest nieprawidłowy', 'Dane finansowe')
except BITSecurityExeption as e:
    print('Błąd ochrony aplikacji: {}'.format (e))
except BITDataFormatExeption as e:
    print('Błąd zniekształcenia danych: {}'.format (e))
except BITException as e:
    print('Błąd aplikacji: {}'.format (e))
except Exception as e:
    print('Generalny błąd aplikacji: {}'.format (e))
