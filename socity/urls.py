from django.urls import path
from . import views

app_name = 'socity'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('learn-more/', views.learn_more, name='learn_more'),
]
