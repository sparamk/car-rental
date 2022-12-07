from django.urls import path, include
from . import views
urlpatterns = [
    path("referfriend/", views.referFriend, name='referfriend'),
    path("digitalcheckin/", views.digitalCheckin, name='digitalcheckin'),
    path("mywallet/", views.myWallet, name='mywallet'),
]