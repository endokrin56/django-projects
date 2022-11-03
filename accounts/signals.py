from django.core.mail import EmailMultiAlternatives
from django.db import models
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

# Create your models here.
from django.template.loader import render_to_string


def send_mail(title, body_text, list_mail):
    html_context = render_to_string(
        'user_created_email.html',
        {
            'text': body_text,
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email='magsy56@yandex.ru',
        to = list_mail,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()

@receiver(user_signed_up, dispatch_uid="some.unique.string.id.for.allauth.user_signed_up")
def user_signed_up_(request, user, **kwargs):
    # pass
    # user_signed_up now send email
    send_mail('Добро пожаловать на новостной сайт',
              'Уважаемый %s,Ваша регистрация на  на новостном сайте прошла  успешно'% user.username, [user.email])