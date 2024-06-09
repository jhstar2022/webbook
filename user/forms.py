from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('email',)
        # fields = UserCreationForm.Meta.fields + ('email',)
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email address is already in use.")
            return email


class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['email', 'password']
        # widgets = {
        #     'email': forms.EmailInput(attrs={'placeholder': 'email'}),
        #     'password': forms.PasswordInput(attrs={'placeholder': 'password'}),
        # }