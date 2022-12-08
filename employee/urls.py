from django.urls import path, include
from . import views

urlpatterns = [
    path("sfr/", views.sfr, name="sfr" ),
    path("usfr/", views.usfr, name='usfr'),
    path("finalizebooking/", views.finalizeBooking, name='finalizebooking'),
    path("adddiscount/", views.addDiscount, name='adddiscount'),
    path("deletediscount/", views.deleteDiscount, name='deletediscount'),
]