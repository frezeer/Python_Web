from threading import Thread
from flask_mail import Message

from flask import  current_app , app

from . import mail

def send_async_mail(message):
    with app.app_context():
        mail.send(message)

def welcome_mail(user):
    Message = Message('Bienvenido a mi proyecyo python',
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[user.email])

    message.html= render_temaplate('email/welcome.html', user=user)
    thread = Thread(Target=send_async_mail, args=[message])
    thread.start()
