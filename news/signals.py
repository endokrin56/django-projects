from django.db.models.signals import  m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_managers, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import PostCategory
# from .NewsPaper import settings


def send_mail(preview, pk, title, list_mail):
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
        to = ['vagren@mail.ru'],
    )
    msg.attach_alternative(html_context, 'text/html')
    #msg.send()

@receiver(m2m_changed, sender=PostCategory)
def notify_new_post(sender, instance,  **kwargs):
    if kwargs['action'] == 'post_add':
        categorys = instance.category.all()
        list_mail: list[str] =[]
        for category in categorys:
            list_mail += category.mailing.all()

        list_mail = [st.email  for st in list_mail]

        #send_mail(instance.preview(), instance.pk, instance.headPost, list_mail)