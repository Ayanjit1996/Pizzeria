from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta  # Import timedelta

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PizzaShop.settings')

# Create a Celery instance.
app = Celery('PizzaShop')

# Using a string here means the worker doesn't have to serialize the configuration
# object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Define the CELERY_BEAT_SCHEDULE
CELERY_BEAT_SCHEDULE = {
    'update-order-status': {
        'task': 'pizzeria.tasks.update_order_status',  # Task path
        'schedule': timedelta(minutes=1),  # Run every 1 minute
    },
}