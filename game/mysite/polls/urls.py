
from django.contrib import admin
from django.urls import path


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^prodlist/$', views.product_list, name='products'),
    # url(r'^checkout/$', views.someview, name='checkout'),
    url(r'^checkout/$', views.checkout, name='checkout')
   ]
