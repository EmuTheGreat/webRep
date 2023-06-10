from django import forms
from django.contrib.auth.models import User
from main.models import CustomUser


class RegistrationForm(forms.Form):
    login = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Имя', max_length=100)
    lastname = forms.CharField(label='Фамилия', max_length=100)

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован.')
        return email


class LoginForm(forms.Form):
    login = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
