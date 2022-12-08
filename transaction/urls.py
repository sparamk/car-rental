from django.urls import path, include
from . import views
urlpatterns = [
    path("payment/", views.payment, name='payment'),
    path("applycoupon/", views.applyCoupon, name='applycoupon'),
    path("config/", views.stripe_config, name='config'),
    path("create-checkout-session/", views.create_checkout_session, name='create-checkout-session'),
    path('success/', views.success, name='success'),
    path('cancelled/', views.CancelledView.as_view()),
    path('webhook/', views.stripe_webhook),
]