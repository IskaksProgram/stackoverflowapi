import os 

from celery import Celery  # celery работает в осихренном.



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stackoverflowapi.settings')

app = Celery('stackoverflowapi.settings')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



# celery -A stackoverflowapi worker -l info   для запуска




























