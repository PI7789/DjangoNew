from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import HotelUser, Booking, Payments

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

        fields = ['booking_startdate','booking_enddate','booking_people',]

        widgets = {'booking_startdate': forms.DateInput(attrs={'type': 'date'}),
                  'booking_enddate': forms.DateInput(attrs={'type': 'date'}) }
        
class ProfileForm(forms.ModelForm):

    class Meta:
        model = HotelUser

        fields = ['username', 'first_name','last_name','email', 'phonenum']

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payments

        fields = ['card_num','card_name','card_cvc','card_exp']

        widgets = {'card_exp': forms.DateInput(attrs={'type':'date'}),
                   }