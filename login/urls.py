from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'login'

urlpatterns = [
    path('profile', views.profile, name="profile"),
]
