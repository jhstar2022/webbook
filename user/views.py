from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm


### Registration
class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('user:register')
        # 회원가입 페이지
        form = RegisterForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_register.html', context)
    

    def post(self, request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('user:login')
        else:
            form = RegisterForm()
        return render(request, 'user/user_register.html', {'form': form})

### Login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('webbook:list')
        
        form = LoginForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('webbook:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password) # True, False
            
            if user:
                login(request, user)
                return redirect('webbook:list')
            
        
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)


### Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('webbook:list')