from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
# from .models import User
from .forms import RegisterForm, LoginForm

# Create your views here.
# user 관련된 기능
# 회원가입
# 로그인
# 로그아웃

### Registration
class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('webbook:list')
        # 회원가입 페이지
        # 정보를 입력할 폼을 보여주어야 한다.
        form = RegisterForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_register.html', context)
    
    
    ## 중복확인 건너띔
    # def post(self, request):
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         return redirect('user:login')
        
    #     else:
    #         form = RegisterForm()
    #     return render(request, 'user/user_register.html', {'form': form})

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
            
        # form.add_error(None, '아이디가 없습니다.')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)


### Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('webbook:list')