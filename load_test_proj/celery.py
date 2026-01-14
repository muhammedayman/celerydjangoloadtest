from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'load_test_proj.settings')

app = Celery('load_test_proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# celery -A load_test_proj  worker -l info
# celery -A load_test_proj worker -l info -P solo
# python manage.py load_test --num 2000 --size 10