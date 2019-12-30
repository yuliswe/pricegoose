import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


droppie_gmail = 'pricedropca@gmail.com'
password = 'Droppie123'

# build basic email msg
msg = MIMEMultipart()
msg['From'] = 'pricedropca@gmail.com'
msg['To'] = 'pricedropca@gmail.com'
msg['Subject'] = 'Welcome to Price Goose'

report_file = open('email_templates/welcome.html')
html = report_file.read()
txt = MIMEText(html, 'html')
msg.attach(txt)

# set up connection
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(droppie_gmail, password)

users = [droppie_gmail]
for user in users:
    mailserver.sendmail(droppie_gmail, user, msg.as_string())

mailserver.quit()
