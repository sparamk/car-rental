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
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
    path('webhook/', views.stripe_webhook),
    path('contactUs/',views.contactUs,name= "contactUs"),
    path('suggestRoadTrip/',views.suggestRoadTrip,name="suggestRoadTrip")
]

