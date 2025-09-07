from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'socity/home.html')

def about(request):
    return render(request, 'socity/about.html')

def services(request):
    return render(request, 'socity/services.html')

def contact(request):
    return render(request, 'socity/contact.html')

@login_required
def register(request):
    return render(request, 'socity/register.html')

def learn_more(request):
    return render(request, 'socity/learn_more.html')
