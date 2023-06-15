from django.db import models

from .user import User


class Achievement(models.Model):
    class AchievChoice(models.TextChoices):
        CREATED_PAGE = "CREATED_PAGE"
        FIRST_PROJECT = "FIRST_PROJECT"
        FIFTY_LIKES = "FIFTY_LIKES"
        TEN_LIKES = "TEN_LIKES"
        FIRST_COMMENT = "FIRST_COMMENT"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.CharField(choices=AchievChoice.choices, max_length=100)
    mark_as_read = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "achievement")
