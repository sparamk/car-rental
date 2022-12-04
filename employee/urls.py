from django.urls import path, include
from . import views

urlpatterns = [
    path("sendfeedbackresponse", views.sendFeedbackResponse, name="sendfeedbackresponse" ),
]