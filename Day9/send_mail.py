import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart

# envirement variable
username = 'exemple@gmail.com'
password = 'password'

def send_mail(text='Email Body', subject='Hello world',
from_email='Abderrahim soumer<exemple@gmail.com>', to_emails= None, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = username
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText('<h1> this is working</h1>', "html")
        msg.attach(html_part)

    msg_str = msg.as_string()
    # Log in to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()


