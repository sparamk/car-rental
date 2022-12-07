from django.urls import path, include
from . import views
urlpatterns = [
    path("addcar/", views.addCar, name='addcar'),
    path("listcars/", views.listCars, name='listcars'),
    path("editcar/", views.editCar, name='editcar'),
    path("updatecar/", views.updateCar, name='updatecar'),
    path("deletecar/", views.deleteCar, name='deletecar'),
    path("blockuser/", views.blockUser, name='blockuser'),
    path("coupons/", views.coupons, name='coupons'),
    path("addcoupon/", views.addCoupon, name='addcoupon'),
    path("editcoupon/", views.editCoupon, name='editcoupon'),
    path("updatecoupon/", views.updateCoupon, name='updatecoupon'),
    path("deletecoupon/", views.deleteCoupon, name='deletecoupon'),
]
