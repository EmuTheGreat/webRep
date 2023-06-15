from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users import models as user_models


@admin.register(user_models.User)
class AdminCustomUser(UserAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("username", "password")},
        ),
        (
            "Personal",
            {"fields": ("email", "avatar", "bio", "first_name", "last_name")},
        ),
        (
            "Advanced options",
            {
                "fields": (
                    "is_staff",
                    "groups",
                    "is_active",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = [
        "id",
        "username",
    ]
    search_fields = ["username"]
    list_display_links = ["username"]


@admin.register(user_models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["id", "template", "title"]


@admin.register(user_models.PortfolioFile)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["id", "portfolio"]


@admin.register(user_models.Achievement)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["id", "achievement", "user"]


@admin.register(user_models.PasswordResetRecord)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["id", "uuid", "user_id", "is_used"]
