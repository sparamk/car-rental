from django.shortcuts import render
from appointment.views import *
from sales.views import *
from booking.views import *
from user.views import *

# Create your views here.
def checkCarAvlb(request):
    signUp()