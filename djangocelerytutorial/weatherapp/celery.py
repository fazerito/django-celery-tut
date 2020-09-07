import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocelerytutorial.settings')

app = Celery('cel')
app.config_from_object('django.conf:settings', namespace='CELERY')
