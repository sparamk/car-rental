from django.urls import path, include
from . import views
urlpatterns = [
    path('bookcar/', views.bookCar, name='bookcar'),
    path('bookings/', views.bookings, name='bookings'),
    path('editbooking/', views.editBooking, name='editbooking'),
    path('updatebooking/', views.updateBooking, name='updatebooking'),
    path('deletebooking/', views.deleteBooking, name='deletebooking'),
    path('finalizecar/', views.finalizeCar, name='finalizecar'),
    path('finalizecarbooking/', views.finalizeCarBooking, name='finalizecarbooking'),
    path('fareestimator', views.fareEstimator, name='fareestimator'),
]