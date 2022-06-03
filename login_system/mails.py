from email.message import EmailMessage


def send_email(to, subject, text):
    try:
        import smtplib

        gmail_user = 'mail'
        gmail_password = 'password'

        message = EmailMessage()
        message.set_content(text)
        message['Subject'] = subject
        message['From'] = gmail_user
        message['To'] = to

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.send_message(message)
        server.close()
        return True
    except:
        return False

