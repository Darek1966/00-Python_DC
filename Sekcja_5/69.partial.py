
# email dociera na pocztę na stronie www.wp.pl
import smtplib
import functools
 
def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):
    message = '''From: {}
    Subject: {}
    
    {}
'''.format(mailFrom, mailSubject, mailBody)
 
    try:
        server = smtplib.SMTP_SSL('smtp.wp.pl', 465)
        server.ehlo()
        server.login(user,password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error sending email')
        return False

mailFrom = 'Your automation system'
mailTo = ['dar.ch@wp.pl']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello !
 
This mail confirms that processing has finished without problems,
 
Have a nice day!'''

user = 'dar.ch@wp.pl'
password = '52CE82841FFA978F0B4A2F1B029FAD5A' 

SendInfoEmailFromWp = functools.partial(SendInfoEmail, user, password, mailSubject = 'Execution alert')

SendInfoEmailFromWp(mailFrom = mailFrom, mailTo = mailTo, mailBody = mailBody)

# SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
