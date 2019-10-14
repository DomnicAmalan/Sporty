from flask_mail import Mail, Message

mail = Mail()

def send_confirmation_mail(email):
    msg = Message(subject="Hello",
                      sender="sportvolt0@gmail.com",
                      recipients=["amalandomnic@gmail.com"], # replace with your email for testing
                      body="This is a test email I sent with Gmail and Python!")
    mail.send(msg)