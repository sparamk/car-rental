from django.db import models
from django.contrib.auth.models import User
import requests
# Create your models here.

class Appointment_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.CharField(max_length = 30)
    date_scheduled = models.CharField(max_length = 2)
    date_added = models.DateTimeField(auto_now_add=True)