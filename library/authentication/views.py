from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from authentication.forms import CustomUserCreationForm, LoginForm


def index(request):
    return render(request, 'authentication/index.html')


def register(request):
    """Register a new user"""
    if request.method != "POST":
        form = CustomUserCreationForm
    else:
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('auth:index')

        else:
            context = {'form': form, 'error': 'Invalid email or password'}
            return render(request, 'registration/register.html', context)

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('auth:index')
            else:
                error = 'An error occurred while log in the user. Please try again'

    else:
        form = LoginForm()
        error = None

    return render(request, 'registration/login.html', {'form': form, 'error': error})
