from flask_mail import Mail, Message
from app.helpers import verification_code
from flask import render_template

mail = Mail()

def send_confirmation_mail(email, code):
    try:
        msg = Message(subject="Hello",
                        sender="sportvolt0@gmail.com",
                        recipients=[email], # replace with your email for testing
                        body="Verification Email",
                        html=email_message_template(code))
        mail.send(msg)
    except Exception as e:
        return False

def email_message_template(code):
    link = "http://127.0.0.1:3333/api/verify/user/"+code
    return render_template('others/email.html', code=link)