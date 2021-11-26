from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('homepage', views.homepage),
    path('query', views.queryShow),
]
