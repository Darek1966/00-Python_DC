
days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days
workdays = days.copy()
workdays = ['mon','tue','wed','thu','fri']

print ("Cały tydzień:", days, id(days))
print ("Dni pracujące:", workdays, id(workdays))
