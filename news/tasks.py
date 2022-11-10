from celery import shared_task
import time

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

# Проблема с отправкой почты, поэтому написано в лоб
# для понимания запуска задач, на текущем этапе.
@shared_task
def send_mail_c():
    preview, title = 'Получите письмо', 'Новое письмо'
    pk = 5
    # print(preview, title)
  # def send_mail(preview, pk, title, list_mail):
    tt ='http://127.0.0.1:8000'
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{tt}/news/{pk}',
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email='magsy56@yandex.ru',
        # to = list_mail,
        to=['vagren@mail.ru'],
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()