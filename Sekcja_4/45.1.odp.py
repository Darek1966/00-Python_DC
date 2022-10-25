
def show_progress(how_many, character='*'):
 
    line = character * how_many
    print(line)
# zmieniamy wartość how_many (character * how_many)
show_progress(10)
show_progress(15)
show_progress(30)

# zmieniamy obie wartości w show_progress
show_progress(10, '-')
show_progress(15, '+')
