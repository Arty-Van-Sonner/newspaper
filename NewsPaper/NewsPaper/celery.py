import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace = 'CELERY')
app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'news.tasks.printer',
        'schedule': 5,
        'args': (5,),
    },
}
app.autodiscover_tasks()
