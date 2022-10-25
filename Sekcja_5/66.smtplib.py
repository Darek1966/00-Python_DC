
from email import message
import smtplib

mailFrom = 'Python_Darek'                           # od kogo
mailTo = ['dar.ch@wp.pl']
mailSubject = 'Email od Python'                     # temat
mailBody = '''Hello'''

message = '''From:    {} 
Subject:    {} 
       {}
'''.format(mailFrom, mailSubject, mailBody)

user = 'dar.ch@wp.pl'
password = '52CE82841FFA978F0B4A2F1B029FAD5A'

try:
    server = smtplib.SMTP_SSL('smtp.wp.pl', 465)
    server.ehlo()                                  # przesyła informację o komputerze
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')
