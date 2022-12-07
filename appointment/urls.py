from django.urls import path, include
from . import views
urlpatterns = [
    path("scheduletestdrive/", views.scheduleTestDrive, name='scheduletestdrive'),
    path("scheduleappointment/", views.scheduleAppointment, name='scheduleappointment'),
    path('appointment/', views.Appointment, name='appointment')
]