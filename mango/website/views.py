from django.shortcuts import render, redirect

from .models import HotelUser, Booking

from .forms import RegisterForm, LoginForm, BookingForm, ProfileForm

from django.contrib.auth import authenticate

from django.contrib.auth.models import auth

from django.contrib.auth.decorators import login_required

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
        status = ""
        if "option1" in request.POST:
            status = request.POST['option1']
            print(status)


        elif "option2" in request.POST:
            status = "VIP reservation"

        print("NewRequest: ", newrequest)
        form = BookingForm(newrequest)
        print(form)
        if form.is_valid():  
            obj = form.save(commit=False)
            print(obj)
            print("123" + status)
            if status == "No VIP":
                cost = int(obj.booking_people) * 25000
            elif status == "VIP reservation":
                cost = int(obj.booking_people) * 35000
            
            print(cost)
            obj.booking_user_id_id = request.user.id
            obj.booking_VIP_status = status
            obj.booking_cost = cost
            obj.save()


            return redirect('')
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