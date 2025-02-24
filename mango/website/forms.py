from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import HotelUser, Booking

from django import forms
from django.forms.widgets import PasswordInput, TextInput

class RegisterForm(UserCreationForm):
    class Meta:
        model = HotelUser

        fields = ['first_name', 'last_name', 'username', 'email', 'phonenum', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class BookingForm(forms.ModelForm):

    class Meta: 
        model = Booking

        fields = ['booking_startdate','booking_enddate','booking_people']

        widgets = {'booking_startdate': forms.DateInput(attrs={'type': 'date'}),
                  'booking_enddate': forms.DateInput(attrs={'type': 'date'}) }