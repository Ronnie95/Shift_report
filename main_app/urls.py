from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home.as_view(), name="home"),
    path('success/',views.Sucess.as_view(),name="success"),
]