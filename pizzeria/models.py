from django.db import models
from datetime import datetime

def set_default_order_placing_time():
    return datetime.now()

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_placing_time = models.DateTimeField(default=set_default_order_placing_time)
    status = models.CharField(max_length=20, default='Accepted')

    def __str__(self):
        return f"Order #{self.order_id}"

class Pizza(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='pizzas')
    pizzabase = models.CharField(max_length=50)
    cheese = models.CharField(max_length=50)
    toppings = models.JSONField()

    def __str__(self):
        return f"Pizza in Order #{self.order_id}"
