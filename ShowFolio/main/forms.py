from django import forms

class RegistrationForm(forms.Form):
    login = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Имя', max_length=100)
    lastname = forms.CharField(label='Фамилия', max_length=100)

class LoginForm(forms.Form):
    login = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
