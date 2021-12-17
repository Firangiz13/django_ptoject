from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('men/', views.men, name = "men"),
    path('women/', views.women, name = "women"),
    path('kids/', views.kids, name = "kids"),
    path('<int:id>/', views.details, name="details"),
    path('cart/', views.cart, name = "cart"),
    path('checkout/', views.checkout, name = "checkout")
]