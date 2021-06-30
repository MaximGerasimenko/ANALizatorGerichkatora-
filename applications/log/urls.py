from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'log'

urlpatterns = [
    path('', views.main_view, name="home"),
]
