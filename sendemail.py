import smtplib

fromaddr = 'shaq.grant.95@gmail.com'
toaddr = 'shaq.grant.95@gmail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
fromname ='Shaq'
fromaddr = 'shaq.grant.95@gmail.com'
toname = 'Shaq'
toaddr='shaq.grant.95@gmail.com'
subject = 'Hello'
msg = 'This is a test email.'
messagetosend = message.format(

 fromname,
 fromaddr,
 toname,
 toaddr,
 subject,
 msg)

# Credentials (if needed)

username = 'shaq.grant.95@gmail.com'

password = 'ysaervecmejltckw'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()
