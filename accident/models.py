from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Report_Accident(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_accident = models.TextField()
    accident_date = models.DateTimeField(auto_now_add=True)

class Road_Side_Assistance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    road_side_assistance = models.TextField()
    assistance_date = models.DateTimeField(auto_now_add=True)

class Vehicle_Theft_Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_theft_report = models.TextField()
    theft_date = models.DateTimeField(auto_now_add=True)