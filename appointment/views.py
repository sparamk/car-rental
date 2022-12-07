from django.shortcuts import render
from car.views import *
from sales.views import *
from .models import *
# Create your views here.
def scheduleTestDrive(request):
    pass

def scheduleAppointment(request):
    pass

def Appointment(request):
    if request.method == 'POST':
        user = request.user
        appointment = request.POST['appointment']
        date_scheduled = datetime.datetime.strptime(request.POST['appointment_date']+ ' ' + request.POST['appointment_time'], '%Y-%m-%d %H:%M')
        appointment = Appointment_data()
        appointment.user = user
        appointment.appointment = appointment
        appointment.date_scheduled = date_scheduled
        appointment.save()
        messages.success(request, 'Your appointment has been scheduled')
        return render(request, 'appointment.html')
    return render(request, 'appointment.html')