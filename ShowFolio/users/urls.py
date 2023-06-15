from django.template.defaulttags import url
from django.urls import include, path
from . import views


urlpatterns = [
    path(r"register/", views.RegisterView.as_view(), name="create-user"),
    path(r"register/set_user_info/", views.RegisterS2View.as_view(), name="set-avatar"),
    path(r"login/", views.LoginView.as_view(), name="login"),
    path(r"reset_password/", views.ResetPasswordView.as_view(), name="reset-password"),
    path(
        r"reset_password_confirm/<uuid:uuid>/<int:pk>/",
        views.ResetPasswordConfirm.as_view(),
        name="reset-password",
    ),
    path(r"user/<slug:slug>/", views.UserProfileView.as_view(), name="user-profile"),
    path(
        r"user/<slug:slug>/achievements/",
        views.UserAchievementsView.as_view(),
        name="user-achievements",
    ),
    path(r"team/", views.TeamView.as_view(), name="team"),
    path(r"", views.MainView.as_view(), name="main-page"),
    path(r"portfolio/", views.PortfolioCreateView.as_view(), name="create-portfolio"),
    path(
        r"portfolio/<slug:variant>/",
        views.PortfolioCreateView.as_view(),
        name="create-portfolio",
    ),
    path(
        r"portfolio/<slug:variant>/<int:pk>/",
        views.PortfolioCreateView.as_view(),
        name="create-portfolio",
    ),
    path(
        r"search/",
        views.SearchView.as_view(),
        name="search",
    ),
]
