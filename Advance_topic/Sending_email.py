import smtplib

# i am using gmail service so i will be write smtp.gmail.com
server = smtplib.SMTP('smtp.gmail.com', 587)
# and the port is 587

server.starttls()  # it will start the server with transport layer service security

# it will get email and password that you want to send from
server.login('sender_email_id', 'password')

server.sendmail('sender_email_id', 'receiver_email_id',
                'message')  # for mail send
print("Mail sent")
