import smtplib
import email
import time
from tkinter.font import names

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('sender username','password' )  # set up your email id before running the program
current_time=time.strftime
list_names=[]#store the names of the person detected
def mail(text):
    subject="Identified a Face"
    message='Subject: {}\n\n{}'.format(subject,text)
    server.sendmail('sender email id','reciever email id',message)  # Enter the senders and recievers address before running the program
text="Face detected -- {} at time--{}".format(names,current_time) #
mail(text)