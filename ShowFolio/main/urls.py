from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('team', views.team, name='team'),
    path('login', views.login, name='login'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio-01', views.portfolio_01, name='portfolio-01'),
    path('portfolio-02', views.portfolio_02, name='portfolio-02'),
    path('portfolio-03', views.portfolio_03, name='portfolio-03'),
    path('portfolio-04', views.portfolio_04, name='portfolio-04'),
    path('portfolio-05', views.portfolio_05, name='portfolio-05'),
    path('portfolio-06', views.portfolio_06, name='portfolio-06'),
    path('portfolio-01-form', views.portfolio_01_form, name='portfolio-01-form'),
    path('portfolio-02-form', views.portfolio_02_form, name='portfolio-02-form'),
    path('portfolio-03-form', views.portfolio_03_form, name='portfolio-03-form'),
    path('portfolio-04-form', views.portfolio_04_form, name='portfolio-04-form'),
    path('portfolio-05-form', views.portfolio_05_form, name='portfolio-05-form'),
    path('portfolio-06-form', views.portfolio_06_form, name='portfolio-06-form'),
    path('user', views.user, name='user'),
    path('register_user', views.register_user, name='register_user'),
    path('user_login', views.user_login, name='user_login'),
]
