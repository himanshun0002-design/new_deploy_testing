from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Society, Flat, ResidentProfile
from .forms import SocietyForm, FlatForm, ResidentRegistrationForm
from django.utils import timezone

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
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
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
        form = ResidentRegistrationForm(request.POST)
        if form.is_valid():
            # Create user
            user = form.save()
            
            # Get or create society
            society = form.cleaned_data['society_name']
            
            # Create or get flat
            flat, created = Flat.objects.get_or_create(
                society=society,
                flat_number=form.cleaned_data['flat_number'],
                defaults={
                    'floor': form.cleaned_data['floor'],
                    'is_occupied': True
                }
            )
            
            # Create resident profile
            ResidentProfile.objects.create(
                user=user,
                flat=flat,
                phone_number=form.cleaned_data['phone_number'],
                is_owner=form.cleaned_data['is_owner'],
                move_in_date=form.cleaned_data['move_in_date']
            )
            
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('socity:home')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = ResidentRegistrationForm()
    
    return render(request, 'socity/register.html', {'form': form})

@login_required
def add_society(request):
    if request.method == 'POST':
        form = SocietyForm(request.POST)
        if form.is_valid():
            society = form.save()
            messages.success(request, 'Society added successfully!')
            return redirect('socity:society_list')
    else:
        form = SocietyForm()
    return render(request, 'socity/add_society.html', {'form': form})

def society_list(request):
    societies = Society.objects.prefetch_related('flats').all().order_by('name')
    for society in societies:
        society.occupied_count = society.flats.filter(is_occupied=True).count()
    return render(request, 'socity/society_list.html', {'societies': societies})

@login_required
def society_detail(request, society_id):
    society = get_object_or_404(Society, id=society_id)
    flats = society.flats.all().order_by('flat_number')
    residents = ResidentProfile.objects.filter(flat__society=society)
    return render(request, 'socity/society_detail.html', {
        'society': society,
        'flats': flats,
        'residents': residents,
    })

@login_required
def add_flat(request, society_id):
    society = get_object_or_404(Society, id=society_id)
    
    if request.method == 'POST':
        form = FlatForm(request.POST)
        if form.is_valid():
            flat = form.save(commit=False)
            flat.society = society
            flat.save()
            messages.success(request, 'Flat added successfully!')
            return redirect('socity:society_detail', society_id=society.id)
    else:
        form = FlatForm()
    
    return render(request, 'socity/add_flat.html', {
        'form': form,
        'society': society
    })

def about(request):
    return render(request, 'socity/about.html')

def services(request):
    return render(request, 'socity/services.html')

def contact(request):
    return render(request, 'socity/contact.html')

def register(request):
    return render(request, 'socity/register.html')

def learn_more(request):
    return render(request, 'socity/learn_more.html')
