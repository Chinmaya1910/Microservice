from __future__ import unicode_literals,absolute_import

import os
from kombu import Exchange, Queue
from celery import Celery   

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')

app=Celery('admin')

app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.task_queues = [
#     Queue('tasks', Exchange('tasks'), routing_key='tasks',
#           queue_arguments={'x-max-priority': 10}),
# ]
# app.conf.task_queue_max_priority = 10
app.autodiscover_tasks()


