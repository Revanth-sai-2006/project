from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User


def home(request):
    return render(request, 'HealthApp/index.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User

def UserRegisterPageCall(request):
    return render(request, 'HealthApp/register.html')

def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password_confirmation')

        if pass1 != pass2:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'HealthApp/register.html', {'username': username, 'email': email})

        if User.objects.filter(username=username).exists():
            messages.info(request, 'OOPS! Username already taken.')
            return render(request, 'HealthApp/register.html', {'username': username, 'email': email})

        if User.objects.filter(email=email).exists():
            messages.info(request, 'OOPS! Email already registered.')
            return render(request, 'HealthApp/register.html', {'username': username, 'email': email})

        user = User.objects.create_user(username=username, password=pass1, email=email)
        user.save()

        messages.success(request, 'Account created successfully!')
        return redirect('home')  # Redirect to the homepage or another view after successful registration

    return render(request, 'HealthApp/register.html')

def UserLoginPageCall(request):
    return render(request, 'HealthApp/login.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if len(username) == 10:
                messages.success(request, 'Login successful as patient!')
                return redirect('patientapp:patienthomepage')
            elif len(username) == 4:
                messages.success(request, 'Login successful as staff!')
                return redirect('staffapp:staffhomepage')
            else:
                messages.error(request, 'Username length does not match criteria.')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'HealthApp/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')


