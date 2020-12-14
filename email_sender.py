import smtplib  # this is a simple mail transmission protocol
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Shane Rich'
email['to'] = 'maike_schafer@hotmail.com'
email['subject'] = 'Is Shane still in the dog box?'

email.set_content(
    'I am sending an email with Python and not my gmail account!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dataandgis@gmail.com', 'Moglichkeit1!')
    smtp.send_message(email)
    print('all good!')
