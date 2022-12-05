from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signUp, name="signup"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('changepassword/<uidb64>/<token>', views.changePassword, name='changepassword'),
    path('modifyprofile/', views.modifyProfile, name="modifyprofile"),
    path('deleteaccount/', views.deleteAccount, name="deleteaccount"),
    path('forgotpassword/', views.forgotPassword, name="forgotpassword"),
    path('changeprofilepassword/', views.changeProfilePassword, name="changeprofilepassword"),
]

