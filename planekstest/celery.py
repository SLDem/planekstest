from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planekstest.settings')

app = Celery('planekstest')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND='django-db')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
