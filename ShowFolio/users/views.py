from django.contrib.auth import login, logout, authenticate
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from . import forms
from .models import User, Portfolio, PortfolioFile, Achievement, PasswordResetRecord


class RegisterView(View):
    def post(self, request, *args, **kwargs):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=request.POST.get("email")).exists():
                return render(request, "users/register.html")
            user = form.save()
            login(request, user)
            return redirect("set-avatar")
        return render(request, "users/register.html")

    def get(self, request, *args, **kwargs):
        return render(request, "users/register.html")


class RegisterS2View(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        user = request.user

        if len(request.FILES) == 0:
            return render(request, "users/profile.html")
        if data.get("profile-about"):
            user.avatar = request.FILES["avatar"]
            user.bio = data.get("profile-about")
            user.save(update_fields=["avatar", "bio"])
            logout(request)
            Achievement.objects.create(
                user=user, achievement=Achievement.AchievChoice.CREATED_PAGE
            )
            return redirect("login")
        return render(request, "users/profile.html")

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return render(request, "users/register.html")
        return render(request, "users/profile.html")


class LoginView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        if data.get("login") and data.get("password"):
            username = request.POST["login"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(f"/user/{user.username}/")
        return render(request, "users/login.html")

    def get(self, request, *args, **kwargs):
        return render(request, "users/login.html")


class ResetPasswordView(View):
    def post(self, request, *args, **kwargs):
        form = forms.ResetPassword(data=request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            user = User.objects.filter(email=email).first()
            if user:
                domain = "http://127.0.0.1:8000"  # TODO: replace on your domain
                reset_obj = PasswordResetRecord.objects.create(user_id=user.pk)
                reset_link = f"{domain}/reset_password_confirm/{reset_obj.uuid}/{reset_obj.user_id}/"
                mail.send_mail(
                    subject="Восстановление пароля на платформе Resumer",
                    message=f"Перейдите по ссылке ниже для восстановления пароля:\n{reset_link}",
                    from_email="no-reply@gmail.com",
                    recipient_list=[email],
                )
            return render(request, "users/reset-password-01.html")
        return render(request, "users/reset_password.html")

    def get(self, request, *args, **kwargs):
        return render(request, "users/reset_password.html")


class ResetPasswordConfirm(View):
    def post(self, request, uuid, pk, *args, **kwargs):
        password_1 = request.POST.get("password")
        password_2 = request.POST.get("repeat-password")
        user_link = PasswordResetRecord.objects.get(uuid=uuid, user_id=pk)
        if user_link.is_used:
            return redirect("main-page")

        if password_1 and password_1 == password_2:
            user = User.objects.get(pk=pk)
            user.set_password(password_1)
            user.save(update_fields=["password"])
            user_link.is_used = True
            user_link.save(update_fields=["is_used"])
        return render(request, "users/login.html")

    def get(self, request, uuid, pk, *args, **kwargs):
        return render(request, "users/reset-password-02.html")


class UserProfileView(View):
    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, slug, *args, **kwargs):
        user = User.objects.get(username=slug)
        ports = Portfolio.objects.filter(owner=user, is_published=True)
        images = [p.portfoliofile_set.first() for p in ports]
        data = list(zip(ports, images))
        interval = len(ports) // 3
        part_1 = data[:interval]
        part_2 = data[interval : interval * 2]
        part_3 = data[interval * 2 :]
        return render(
            request,
            "users/user.html",
            context={
                "user": user,
                "part_1": part_1,
                "part_2": part_2,
                "part_3": part_3,
            },
        )


class TeamView(TemplateView):
    template_name = "users/team.html"


class MainView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            achievements = Achievement.objects.filter(
                user=request.user, mark_as_read=False
            )
            achievements_templates = {
                Achievement.AchievChoice.FIRST_PROJECT: "users/achievement-02.html",
                Achievement.AchievChoice.FIFTY_LIKES: "users/achievement-05.html",
                Achievement.AchievChoice.FIRST_COMMENT: "users/achievement-03.html",
                Achievement.AchievChoice.CREATED_PAGE: "users/achievement-01.html",
                Achievement.AchievChoice.TEN_LIKES: "users/achievement-04.html",
            }
            if achievements:
                achievement = achievements.first()
                achievement.mark_as_read = True
                achievement.save(update_fields=["mark_as_read"])
                return render(request, achievements_templates[achievement.achievement])
        return render(request, "users/index.html")


class PortfolioCreateView(View):
    def post(self, request, *args, **kwargs):
        if "pk" in kwargs:
            portfolio = Portfolio.objects.get(pk=kwargs.get("pk"))
            portfolio.title = request.POST.get("title")
            portfolio.description = request.POST.get("desc")
            portfolio.is_published = True
            portfolio.save(update_fields=["title", "description", "is_published"])
            ach = Achievement.objects.filter(
                user=request.user,
                achievement=Achievement.AchievChoice.FIRST_PROJECT,
            )
            if not ach:
                Achievement.objects.create(
                    user=request.user,
                    achievement=Achievement.AchievChoice.FIRST_PROJECT,
                )

            return redirect("user-profile", request.user.username)
        variant_url = kwargs.get("variant")
        variant = {
            "1": "users/portfolio-01.html",
            "2": "users/portfolio-02.html",
            "3": "users/portfolio-03.html",
            "4": "users/portfolio-04.html",
            "5": "users/portfolio-05.html",
            "6": "users/portfolio-06.html",
        }
        if variant_url in ("1", "4") and len(request.FILES) != 4:
            return render(request, variant[variant_url])
        elif variant_url in ("2", "3", "5", "6") and len(request.FILES) != 5:
            return render(request, variant[variant_url])
        variant_forms = {
            "1": "users/portfolio-01-form.html",
            "2": "users/portfolio-02-form.html",
            "3": "users/portfolio-03-form.html",
            "4": "users/portfolio-04-form.html",
            "5": "users/portfolio-05-form.html",
            "6": "users/portfolio-06-form.html",
        }
        portfolio = Portfolio.objects.create(template=variant_url, owner=request.user)
        files = PortfolioFile.objects.bulk_create(
            [
                PortfolioFile(image=f, portfolio=portfolio)
                for f in request.FILES.values()
            ]
        )
        return render(
            request,
            variant_forms[variant_url],
            context={"images": files, "obj": portfolio},
        )

    def get(self, request, *args, **kwargs):
        if "variant" in kwargs:
            variant = {
                "1": "users/portfolio-01.html",
                "2": "users/portfolio-02.html",
                "3": "users/portfolio-03.html",
                "4": "users/portfolio-04.html",
                "5": "users/portfolio-05.html",
                "6": "users/portfolio-06.html",
            }
            return render(request, variant[kwargs["variant"]])
        return render(request, "users/portfolio.html")


class UserAchievementsView(View):
    def get(self, request, slug, *args, **kwargs):
        return render(request, "users/achievements.html")


class SearchView(View):

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search")
        if search:
            portfs = Portfolio.objects.filter(title__icontains=search)
            if portfs:
                images = [p.portfoliofile_set.first() for p in portfs]
                data = list(zip(portfs, images))
                return render(request, "users/search.html", context={"data": data})
        return render(request, "users/search.html")
