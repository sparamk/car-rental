from django.urls import path, include
from . import views

urlpatterns = [
     path('buyVehicle/', views.buyVehicle, name='buyVehicle'),
     path('sellVehicle/', views.sellVehicle, name='sellVehicle')
     
]