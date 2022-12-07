from django.db import models
from django.utils.timezone import now


# Create your models here.
class Cars(models.Model):
    car_name = models.CharField(max_length = 20)
    color = models.CharField(max_length = 10)
    capacity = models.CharField(max_length = 2)
    rent_per_hour = models.CharField(max_length=6, default=1)
    cost_of_vehicle = models.CharField(max_length=6, default=2000)
    is_available = models.BooleanField(default = True)
    description = models.CharField(max_length = 100)
    car_condition = models.BooleanField(default=1)
    subscription = models.CharField(max_length=6,default='1')
    date_added = models.DateTimeField(auto_now_add=True)

class Coupons(models.Model):
    coupon_code = models.CharField(max_length = 20)
    discount = models.CharField(max_length = 2)
    date_added = models.DateTimeField(auto_now_add=True)
