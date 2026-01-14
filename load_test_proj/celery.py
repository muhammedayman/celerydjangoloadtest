from celery import Celery
import os
from extranet_backend.settings import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'extranet_backend.settings')

app = Celery('extranet_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

