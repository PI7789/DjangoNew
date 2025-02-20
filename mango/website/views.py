from django.shortcuts import render, redirect

from .models import HotelUser

from .forms import RegisterForm, LoginForm

from django.contrib.auth import authenticate

from django.contrib.auth.models import auth

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('')
    context = {'form': form}

    return render(request, 'pages/register.html' , context=context)

def login(request):
    form = LoginForm

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('')
    context = { 'login_form' : form }
    return render(request, 'pages/login.html', context=context)