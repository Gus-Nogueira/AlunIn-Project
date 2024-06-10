from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Your account has been created successfully")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
    return render(request, 'register.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')
