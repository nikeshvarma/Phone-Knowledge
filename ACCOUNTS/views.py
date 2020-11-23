from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .forms import UserRegisterForm, LoginForm


def validate_username(request):
    username = request.GET.get('username')
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def validate_email(request):
    email = request.GET.get('email')
    data = {
        'is_registered': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


def signup(request):
    registerform = UserRegisterForm()
    try:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                pass1 = form.cleaned_data['password1']
                pass2 = form.cleaned_data['password2']
                if pass1 == pass2:
                    if not User.objects.filter(email__exact=form.cleaned_data['email']).exists():
                        user = User.objects.create_user(username=form.cleaned_data['username'].lower(),
                                                        email=form.cleaned_data['email'],
                                                        password=form.cleaned_data['password1']
                                                        )
                        user.save()
                        login(request, user)
                        return redirect('homepage')
                    else:
                        messages.add_message(request, messages.WARNING, "This Email address already registered")
                        return redirect('signupuser')
                else:
                    messages.add_message(request, messages.WARNING, "Password didn't match")
                    return redirect('signupuser')
            else:
                return redirect('signupuser')
        else:
            args = {'forms': registerform}
            return render(request, 'Account/SignUp.html', args)
    except IntegrityError:
        messages.add_message(request, messages.WARNING, "This Username already taken")
        return redirect('signupuser')


def loginuser(request):
    loginform = LoginForm()
    args = {'form': loginform}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user=user)
                return redirect('homepage')
            else:
                messages.add_message(request, messages.WARNING, 'Invalid username or password')
                return redirect('loginuser')
        else:
            return redirect('loginuser')
    else:
        return render(request, 'Account/Login.html', args)


@login_required
def logoutuser(request):
    logout(request)
    return redirect('homepage')
