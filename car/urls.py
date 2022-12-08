from django.urls import path, include
from . import views
urlpatterns = [
    path("checkcaravlb/", views.checkCarAvlb, name='checkcaravlb'),
]