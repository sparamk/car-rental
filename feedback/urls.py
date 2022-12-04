from django.urls import path, include
from . import views

urlpatterns = [
    path('sendfeedback/', views.sendFeedback, name='sendfeedback'),
]