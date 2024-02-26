#Shuru ma import the necessary modules
from email.message import EmailMessage
#Email message module le allows us to create email messages with Python
import ssl
# I dont know the modules but SSL(Secure Sockets Layer)encryption provides access to ssl
import smtplib
# yo module defines classes which implement the SMTP protocol for sending email


#Defining Email Credentials and Content:
#These are just some variables that I created for sending and receiver and the subject and body of the process in Strings
email_sender = "amanshrestha3003@gmail.com"
email_password = "sbmw fhyt uycp beab"

email_receiver = 'peacepalden@gmail.com'
subject = "AMAN SHRESTHA"
body = """Major technology companies have cut thousands of jobs since the start of 2024 as the rise of artificial intelligence (AI) and interest rates upend the tech sector."""

em = EmailMessage() #EmailMessage object has been created, em chai object name ho

#Creating the Email Message
#From ,To, and subject are set using the object em attibutes
em['From']= email_sender
em['To']= email_receiver
em['subject']=subject
em.set_content(body)# and methods

#Establishing an SSL Context
context =ssl.create_default_context() # so basically this line creates a default SSL context, which is necessaty for establishing a secure connection to Gmail's SMTP server.

#Sending the email
#creates an STMP_SSL object with gmail's SMTP server address which is "smtp.gmail.com", port number('465'), and SSL context
with smtplib.SMTP_SSL("smtp.gmail.com",465,context =context) as smtp:
    smtp.login(email_sender, email_password)#logs in to the SMTP server using the sender's email address and password
    smtp.sendmail(email_sender,email_receiver, em.as_string())# elle chai sends the email using sendmail() method,passing the sender's email address, recipient's email address, and the email message converted to a string using 'as_string()'

#SMTP stands for Simple Mail Transfer Protocol. It is a communication protocol used for sending email messages between servers. 
#SMTP is responsible for handling the outgoing mail on an email client or server and delivering it to the recipient's email server.

#SSL stands for Secure Sockets Layer. It is a cryptographic protocol that provides secure communication over a computer network.
#SSL ensures that data transmitted between a client and a server is encrypted and remains confidential during transmission.



