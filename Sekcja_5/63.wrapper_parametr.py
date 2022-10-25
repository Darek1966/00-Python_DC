
import datetime
import functools
# znak r aby beckslesh \ był traktowany jak beckslesh \, a nie inny znak
# logFilePath = r'E:\Python\00 Python_DC\Sekcja_5\function_log.txt' # otwieramy plik

# odznaczamy otwarcie pliku i tworzymy funkcję z dostępe do pliku
def CreateFunctionWithWrapper_LogToFile(logFilePath): # funkcja z dostępem do pliku
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath, "a") # otwieramy utworzony plik txt (a - dopisujemy dane)
            file.write("-"*20 + "\n") # kreski i wiersz niżej
            file.write('Funkcja "{}" start {}\n'.format(func.__name__, datetime.datetime.now().isoformat()))
            file.write('Parametry zmiany placy:\n')   # \n - znak ENTER
            file.write(" ".join("{}".format(x) for x in args)) # "{}" - powstanie napis, którego treścią będzie x (będzie skonwertowany do tekstu)
            file.write("\n")  # x - to kolejne argumenty zmiennej args
            file.write(" ".join("{} = {}".format(k, v) for (k, v) in kwargs.items())) # kwargs - tak jak dla arga {} = {} - napis = napis
            # k - key, v - values z tablice kwargs.items
            file.write("\n")
            result = func(*args, **kwargs)
            file.write('Funkcja zwrot {}\n'.format(result))
            file.close()
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper

@CreateFunctionWithWrapper_LogToFile(r'E:\Python\00 Python_DC\Sekcja_5\change_salary_log.txt')
def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print('Zmiana wynagrodzenia dla {} do {} jak bonus={}'.format(emp_name, new_salary, is_bonus))
    return new_salary

@CreateFunctionWithWrapper_LogToFile(r'E:\Python\00 Python_DC\Sekcja_5\change_position_log.txt')
def ChangePosition(emp_name, new_position):
    print('Zmiana pozycji dla {} do {}'.format(emp_name, new_position))
    return new_position

print(ChangeSalary('Darek', 20000, True))
print(ChangeSalary('Jan', 4000, is_bonus=True))
print(ChangePosition('Mariam', 'Kelner'))
print(ChangePosition('Darek', 'Manager'))
