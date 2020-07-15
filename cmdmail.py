#IMPORTING THE REQUIRED LIBRARIES
import smtplib
import os
from email.message import EmailMessage

"""-------This part contains the code--------"""
# Creating an object of the class
msg = EmailMessage()
# Function for taking input
def getinfo():
    
    sub = input("Enter the subject: ")
    To = input("Input emails(seperate by commas):")
    To = list(To.split(","))
    Content = input("Enter the content: ")
    return sub,To,Content

# Email address and password are stored in enviornment variables thus safe
EMAIL_ADDRESS = os.environ.get('DB_USER')
EMAIL_PASSWORD = os.environ.get('DB_PASS')

# Calling class to get the inputs
"""Please add \ after the path or help me in fixing it """
PATH = input("Please Enter The Path Of The Project: ")

SUB,TO,CONTENT = getinfo()

"""This part is very importat since it does the job"""
#  var files has list of all files in path
files = os.listdir(PATH)

# Giving the variables the values
msg['Subject'] = SUB
msg['From'] = EMAIL_ADDRESS
msg['To'] = ", ".join(TO)
msg.set_content(CONTENT)


# Iterating through files in path and adding them as an attachment
for file in files:
    with open(PATH+"\\"+file,'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype = 'application',subtype='octet-stream',filename=file_name)


# Sending your mail :)
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
    print("Mail Sent Succesfully")
