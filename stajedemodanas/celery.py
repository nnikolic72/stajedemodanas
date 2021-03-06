import os
from celery import Celery
import configurations

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stajedemodanas.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

configurations.setup()

if not settings.BROKER_URL:
    broker_url = f'amqp://{settings.RABBIT_USER}:{settings.RABBIT_PASS}@{settings.RABBIT_SERVER}/{settings.RABBIT_DB}'
else:
    broker_url = settings.BROKER_URL

celery = Celery('stajedemodanas', broker=broker_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery.autodiscover_tasks()


@celery.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
