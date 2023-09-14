from celery import shared_task
from .models import Order
from datetime import datetime, timedelta
from django.utils import timezone


@shared_task()
def update_order_status():

    current_time = timezone.now()
    # Update orders based on time intervals
    orders = Order.objects.all()
    for order in orders:
        if (current_time - order.order_placing_time).total_seconds() >= 60:
            order.status = 'Preparing'
        if (current_time - order.order_placing_time).total_seconds() >= 180:
            order.status = 'Dispatched'
        if (current_time - order.order_placing_time).total_seconds() >= 300:
            order.status = 'Delivered'
        order.save()