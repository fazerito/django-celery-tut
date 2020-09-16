from celery import task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .utils import save_weather_data

@periodic_task(run_every=(crontab(minute='*/30')))
def task_get_weather_periodic():
    save_weather_data(None)

@task
def task_get_weather(city):
    save_weather_data(city)
