from django import forms
from .models import Society, Flat, ResidentProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SocietyForm(forms.ModelForm):
    class Meta:
        model = Society
        fields = ['name', 'address']

class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = ['flat_number', 'floor']

class ResidentRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)
    society_name = forms.ModelChoiceField(queryset=Society.objects.all(), required=True)
    flat_number = forms.CharField(max_length=50)
    floor = forms.IntegerField()
    is_owner = forms.BooleanField(required=False)
    move_in_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
