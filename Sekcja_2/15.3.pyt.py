
import datetime as dt
 
today_weekday = dt.date.today().strftime("%A")
'''
if today_weekday == 'Monday':
    print("pomagam mamie")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("Robisz pranie")
elif today_weekday == 'Thursday':
    print("jestem na służbie")
elif today_weekday == 'Friday':
    print("mam dwa spotkania")
elif today_weekday == 'Saturday':
    print("Masz lekcje")
else:
    print("NIEDZIELA BĘDZIE DLA NAS")
'''
print("pomagam mamie" if today_weekday == 'Monday' else
      "Robisz pranie" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      "jestem na służbie" if today_weekday == 'Thursday' else
      "mam dwa spotkania" if today_weekday == 'Friday' else
      "Masz lekcje" if today_weekday == 'Saturday' else
      "NIEDZIELA BĘDZIE DLA NAS")

