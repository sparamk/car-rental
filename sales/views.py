from django.shortcuts import render
from appointment.views import *
from car.views import *
from appointment.models import *

# Create your views here.
def sellVehicle(request):
    return render(request, 'appointment.html')


def buyVehicle(request):
    return render(request, 'appointment1.html')


