# Program to automatically send email when something goes down
# by calling the function email()
# like this --> email(["example@somewhere.com","somewhereelse@other.com"])
import smtplib # Necessary modules
from email.mime.text import MIMEText

xhoni = "xhp1@pitt.edu"

def sendMail(recievers,content,subject="Alert"):
    sender = "Floor2TowerB@gmail.com"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = sender
    if type(recievers) == type(["LIST"]): msg['To'] = ",".join(recievers)
    else: msg['To'] = recievers
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login("Floor2TowerB","Fl00r2Rules!!/")
        server.sendmail(sender,recievers,msg.as_string())
    except:
        print("UNABLE TO SEND EMAIL")
