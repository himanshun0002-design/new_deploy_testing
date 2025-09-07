from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'socity'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('learn-more/', views.learn_more, name='learn_more'),
    path('societies/', login_required(views.society_list), name='society_list'),
    path('society/add/', login_required(views.add_society), name='add_society'),
    path('society/<int:society_id>/', login_required(views.society_detail), name='society_detail'),
    path('society/<int:society_id>/add-flat/', login_required(views.add_flat), name='add_flat'),
]
