from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login correct")
            return redirect('budget:home')
        messages.error(request, "Error in Login! Please try again...")
        return redirect('users:login_user')
    return render(request, "users/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout completed")
    return redirect('users:login_user')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Auth and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Register is good! Welcome!")
            return redirect('budget:home')
    else:
        form = SignUpForm()
        return render(request, "users/register.html", {'form': form})
    return render(request, "users/register.html", {'form': form})
