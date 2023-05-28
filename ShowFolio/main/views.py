from django.shortcuts import render
from django.http import HttpResponse

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