from django.urls import path
from . import views

app_name = 'socity'

urlpatterns = [
    path('', views.home, name='home'),
]
