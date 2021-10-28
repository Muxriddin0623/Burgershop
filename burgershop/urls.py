from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostMenu.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('contact/', views.contact, name='contact'),

]
