import datetime
import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from django.core.mail import send_mail, EmailMultiAlternatives

#from .models import Post, Category
from NewsPaper.news.models import Post, Category

logger = logging.getLogger(__name__)


# наша задача по выводу текста на экран
def my_job():
    #  Your job processing logic here...
    print('hello from job')

def my_job1():
    send_mail(
        'Job mail',
        'hello from job!',
        from_email='magsy56@yandex.ru',
        recipient_list=['vagren@mail.ru'],
    )

# задача оповещения о новых статьях
def my_job2():
    #  Your job processing logic here...
    today = datetime.datetime.today()
    lastday = today - datetime.timedelta(days=1)
    posts = Post.objects.filter(post_datetime__gte=lastday)
    categories = set(posts.volues_list('category__context', flat=True))
    list_mail = set(Category.objects.filter(context__in=categories).volues_list('list_mail__email', flat=True))
    tt ='http://127.0.0.1:8000'
    html_context = render_to_string(
        'daily_email.html',
        {
            'posts': posts,
            'link': f'{tt}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=' Новые   научные статьи статьи',
        body='',
        from_email='magsy56@yandex.ru',
        #to=list_mail,
        to='vagren@mail.ru'
    )

    msg.attach_alternative(html_context, 'text/html')
    msg.send()

# функция, которая будет удалять неактуальные задачи
def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        scheduler.add_job(
            my_job2,
            trigger=CronTrigger(second="*/30"),
            # То же, что и интервал, но задача тригера таким образом более понятна django
            id="my_job2",  # уникальный айди
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")