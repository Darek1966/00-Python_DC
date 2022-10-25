'''
Napisz context manager generujący HTML.
Nazwij go HtmlCM
W metodzie __init__ nie rób nic
W metodzie __enter__ wyświetl nagłówek tabelki HTML, mniej więcej w taki sposób:
<TABLE>
 <TR>
     <TH>Number</TH><TH>Description</TH>
 </TR>
'''
class HtmlCM:
 
    def __init__(self):
        pass
    '''
    W metodzie __exit__ wyświetl zamykający tag dla tabeli, mniej więcej tak:
    </TABLE>
    '''
    def __enter__(self):
        print("<TABLE>")
        print(" <TR>")
        print("     <TH>Number</TH><TH>Description</TH>")
        print(" </TR>")
        return self
 
    def __exit__(self, type, value, traceback):
        print("</TABLE>")
'''
Wykorzystaj nowy context manager korzystając z odpowiedniej konstrukcji with ...
Wewnątrz context managera wyświetl 2 wiersze tabeli, mniej więcej tak:

 <TR>
     <TD>1</TD><TD>Say hello!</TD)
 </TR>
 <TR>
     <TD>2</TD><TD>Say good bye!</TD)
 </TR>

'''
 
with HtmlCM() as html:
 
    print(" <TR>")
    print("     <TD>1</TD><TD>Say hello!</TD)")
    print(" </TR>")
    print(" <TR>")
    print("     <TD>2</TD><TD>Say good bye!</TD)")
    print(" </TR>")
