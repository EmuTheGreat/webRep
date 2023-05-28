from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.forms import RegistrationForm


def index(request):
    return render(request, 'main/index.html')
def team(request):
    return render(request, 'main/team.html')
def login(request):
    return render(request, 'main/login.html')
def portfolio(request):
    return render(request, 'main/portfolio.html')
def user(request):
    return render(request, 'main/user.html')
#region portfolio 1-6
def portfolio_01(request):
    return render(request, 'main/portfolio-01.html')
def portfolio_02(request):
    return render(request, 'main/portfolio-02.html')
def portfolio_03(request):
    return render(request, 'main/portfolio-03.html')
def portfolio_04(request):
    return render(request, 'main/portfolio-04.html')
def portfolio_05(request):
    return render(request, 'main/portfolio-05.html')
def portfolio_06(request):
    return render(request, 'main/portfolio-06.html')
#endregion
#region portfolio form
def portfolio_01_form(request):
    return render(request, 'main/portfolio-01-form.html')
def portfolio_02_form(request):
    return render(request, 'main/portfolio-02-form.html')
def portfolio_03_form(request):
    return render(request, 'main/portfolio-03-form.html')
def portfolio_04_form(request):
    return render(request, 'main/portfolio-04-form.html')
def portfolio_05_form(request):
    return render(request, 'main/portfolio-05-form.html')
def portfolio_06_form(request):
    return render(request, 'main/portfolio-06-form.html')
#endregion

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Создание пользователя
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['name']
            last_name = form.cleaned_data['lastname']

            # Создание и сохранение пользователя
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Редирект после успешной регистрации
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid login credentials.'})
    return render(request, 'main/login.html')
