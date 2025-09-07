from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'socity/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('socity:home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'socity/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('socity:home')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('socity:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('socity:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('socity:register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, 'Registration successful!')
        return redirect('socity:home')

    return render(request, 'socity/register.html')

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
