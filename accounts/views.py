from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm
from .models import CustomerProfile
from django.contrib.auth import authenticate, login, logout
from restaurants.models import Restaurant


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            CustomerProfile.objects.create(
                user = user,
                phone = form.cleaned_data["phone"]
            )
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html",{
                "form":form
            })
    
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user is not None:
            login(request, user)
            return redirect("home")
        return render(request, "login.html",{
           "error": "Invalid username or password"
        })
        
    return render(request, 'login.html')


def home_view(request):
    restaurants = Restaurant.objects.filter(is_active = True)
    return render(request, "home.html",{
        "restaurants":restaurants
    })
    
def logout_view(request):
    logout(request)
    return redirect("login")
        
