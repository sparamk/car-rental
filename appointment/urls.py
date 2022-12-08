from django.urls import path, include
from . import views
urlpatterns = [
    path("scheduletestdrive/", views.scheduleTestDrive, name='scheduletestdrive'),
    path("scheduleAppointment/", views.scheduleAppointment, name='scheduleappointment'),
    path('appointment/', views.Appointment, name='appointment')
]