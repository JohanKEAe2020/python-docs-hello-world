from flask import Flask
app = Flask(__name__)
from time import ctime
import smtplib, ssl

@app.route("/")
def advarselsemail():
    
    port = 465                                      #Email port           
    smtp_server = "smtp.gmail.com"                  #SMTP-server
    sender_email = "Keagruppe6A@gmail.com"          #Sender Email
    receiver_email = "Keagruppe6A@gmail.com"        #Receiver Email
    password = "NaturCenterAmagerStrand"            #Password to sender Email

    name="Thomas"                                   #Variabler til Emailens indhold
    antal=75                                        #Skal indtastes manuel
    tid=ctime()
    subject="Dagens advarsel"

    message = 'Subject: {}\n\n'.format(subject)     #Email strengen
    message+='Hej {}, \n\n'.format(name)
    message+='Antallet af mennsker var over: {} \n'.format(antal)
    message+='Tidspunkt: {} \n\n'.format(tid)
    message+="Venlig hilsen RPI."

    context = ssl.create_default_context()          #Oprettelse af SSL
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)        
        server.sendmail(sender_email, receiver_email, message)  #Afsendelse af email
    return "Advarsel afsendt"                       #Webside skrift
