
import smtplib
 
mailFrom = 'Your automation system'
mailTo = ['dar.ch@wp.pl']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello
 
This mail confirms that processing has finished without problems,
 
Have a nice day!'''
 
message = '''From: {}
Subject: {}
 
{}
'''.format(mailFrom, mailSubject, mailBody)
 
user = 'dar.ch@wp.pl'
password = '52CE82841FFA978F0B4A2F1B029FAD5A'
 
try:
    server = smtplib.SMTP_SSL('smtp.wp.pl', 465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')
    