from django.shortcuts import render, redirect, get_object_or_404

from .models import HotelUser, Booking

from .forms import RegisterForm, LoginForm, BookingForm, ProfileForm, PaymentForm

from django.contrib.auth import authenticate

from django.contrib.auth.models import auth

from django.contrib.auth.decorators import login_required

import random

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

@login_required(login_url="login")
def booking(request):
    form = BookingForm()
    if request.method=="POST":
        newrequest = request.POST.copy()
        newrequest.update({'booking_user_id_id':request.user})
        status = request.POST.get("VIP_Selector", "") # this gets the value from VIP_Selector variable


        

        form = BookingForm(newrequest)
        if form.is_valid():  
            obj = form.save(commit=False)

            arrive = obj.booking_startdate

            depart = obj.booking_enddate

            result = depart - arrive

            flightnum = obj.booking_flight + 1

            hour = random.randint(0,24)

            minute = random.randint(0,12)

            minute5 = minute * 5

            minute5 = str(minute5).zfill(2)

            flight_string = str(hour) + ":" + minute5

            if status == "option1":
                cost = int(obj.booking_people) * 25000
                status = "Normal Stay"
            elif status == "option2":
                cost = int(obj.booking_people) * 35000
                status = "VIP Stay"
            
            cost = int(result.days) * cost

            obj.booking_user_id_id = request.user.id
            obj.booking_VIP_status = status
            obj.booking_cost = cost
            obj.booking_flight = flight_string
            obj.save()


            return redirect('payment')
        else:
            print("error")
    context = {'BForm': form}
    
    return render(request, 'pages/booking.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect('')
@login_required(login_url='login')
def profile(request):
    tablestuff = Booking.objects.filter(booking_user_id_id=request.user)

    profiletable = request.user

    form = ProfileForm(instance=request.user)

    if request.method == "POST":

        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():

            form.save()


    context = {'profileform': form,
               'profiledb': profiletable,
               'records': tablestuff}

    return render(request, 'pages/profile.html', context = context)


###############################################################################################

def payment(request):
    form = PaymentForm()

    if request.method == "POST":

        form = PaymentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('')

    context = {'paymentform':form}

    return render(request, 'pages/payment.html', context=context)

def info(request, booking_id):
    record = get_object_or_404(Booking, booking_id=booking_id)

    arrival = request.GET.get('arrival')

    VIPstatus = request.GET.get('VIPstatus')

    flight = record.booking_flight

    print(flight)

    print("arrival: " + arrival)

    print("VIP status : "+ VIPstatus)

    return render(request, 'pages/info.html')