from flask import Flask
app = Flask(__name__)
from time import ctime
import smtplib, ssl

@app.route("/")
def hello():
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "Keagruppe6A@gmail.com"  # Enter your address
    receiver_email = "Keagruppe6A@gmail.com"  # Enter receiver address
    password = "NaturCenterAmagerStrand" #input("Type your password and press enter: ")

    name="Thomas"
    antal=700
    tid=ctime()


    message = """\
    Subject: Dagens statistik \n\n"""
    message+='Hej, {} \n\n'.format(name)
    message+='Antallet af mennsker var over: {} \n'.format(antal)
    message+='Tidspunkt: {} \n\n'.format(tid)
    message+="Venlig hilsen RPI."

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return "Hello, World!"
