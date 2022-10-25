
import urllib.request
import os
 
data_dir = 'E:\Python'
pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    # { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' }, # ta strona robi błąd (break)
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]
 
for page in pages:
 
    try:        # tworzymy ścieżkę path do pliku powstałą z połączenia data_dir, nazwy strony pobranej z pages i ".html"
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)
 
        print("Processing: {}  => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve (page["url"], path)  # urllib.request.urlretrieve - zapis strony na dysku
        print('...done')

    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break       # zakończy się w przypadku błędu
 
else:
    print('All pages downloaded successfully!!!')       # wykona się jak nie będzie błędu (nie będzie break)
