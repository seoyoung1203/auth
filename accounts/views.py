from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login  # 장고의 login 함수 이름을 auth_login로 바꾸기(이름 중복 때문)
from django.contrib.auth import logout as auth_logout
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 올바른 값은 그대로 유지
            form.save()
            return redirect('accounts:login')
    else:
        form= CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid(): # 유저정보는 저장할 필요가 없기 때문에 save 안함
             auth_login(request, form.get_user())
             return redirect('accounts:login')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }

    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')