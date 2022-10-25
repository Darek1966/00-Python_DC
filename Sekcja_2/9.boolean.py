
def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i+1, options[i]))
 
    choice = input('Wybierz opcję powyżej lub naciśnij enter, aby wyjść: ')
    return choice
    
 
choice='x'
options = ['load data', 'export data', 'analyze & predict']
 
while choice:
 
    choice = DisplayOptions(options)
 
    # wykonane tylko wtedy, gdy coś zostało wprowadzone
    if choice:
        try:
            choice_num = int(choice)-1
            if choice_num >=0 and choice_num < len(options):
                print("wybrałeś {} - {}".format(choice_num+1, options[choice_num]))
            else:
                print("wybierz wartość z listy lub naciśnij enter")
        except:
            print("Musisz wpisać numer")
    else:
        print('----- END -----')
