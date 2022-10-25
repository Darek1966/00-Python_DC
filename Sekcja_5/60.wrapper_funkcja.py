import datetime
import functools

# po import functools - nw funkcja
def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        # print('-'*10)
        # print('Funkcja start {}'.format(datetime.datetime.now().isoformat()))
        print('Funkcja "{}" start {}'.format(func.__name__, datetime.datetime.now().isoformat()))
        print('Parametry zmiany placy:')
        result = func(*args, **kwargs)
        # print('+'*10)
        print('Funkcja zwrot {}'.format(result))
        return result
    return func_with_wrapper

@CreateFunctionWithWrapper  # @ - dekorowanie funcji
# funkcja ChangeSalary jest udekorowana, w momencjie utworzenia Python obuduje ją w: def CreateFunctionWithWrapper(func)
def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print('Zmiana wynagrodzenia dla {} do {} jak bonus={}'.format(emp_name, new_salary, is_bonus))
    return new_salary

print(ChangeSalary('Darek', 20000, True))

# funkcja do śledzenia funkcji przesłanej jako argument
'''
def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        # print('-'*10)
        # print('Funkcja start {}'.format(datetime.datetime.now().isoformat()))
        print('Funkcja "{}" start {}'.format(func.__name__, datetime.datetime.now().isoformat()))
        print('Parametry zmiany placy:')
        result = func(*args, **kwargs)
        # print('+'*10)
        print('Funkcja zwrot {}'.format(result))
        return result
    return func_with_wrapper
'''
# nowa zmienna - to co zwróci fun WynagrodzenieNowe jak wywołamy ją z parametrem Wynagrodzenie
# ChangeSalaryWithLog = CreateFunctionWithWrapper(ChangeSalary)

# print(ChangeSalaryWithLog('Darek', 20000, True))
# print(ChangeSalaryWithLog('Darek', 20000, is_bonus = True))

# inny sposób - też zadziała z wrapperem
# ChangeSalary = CreateFunctionWithWrapper(ChangeSalary) # zamiast tego - import functools

print(ChangeSalary('Darek', 20000, is_bonus = True))
