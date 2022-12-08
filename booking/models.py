from django.db import models
from owner.models import *
from django.contrib.auth.models import User, Group

# Create your models here.
class Book_Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # car = models.ForeignKey(Cars, on_delete=models.CASCADE, default=0)
    capacity = models.CharField(max_length=3)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    rent = models.FloatField()
    subscription = models.CharField(max_length=6,default='silver')
    is_paid = models.BooleanField(default=False)
    confirmation = models.CharField(max_length=1, default=0)
    booked_date = models.DateTimeField(auto_now_add=True)
    confirmed_date = models.DateTimeField(auto_now=True)
    session_id = models.TextField(default='')
    discount = models.IntegerField(max_length=10,default=0)