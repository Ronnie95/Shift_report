from django.urls import path
from . import views

url_patters = [
    
    path('', views.Home.as_view(), name="home"),
]