import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as CoreUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserQuerySet(models.QuerySet):
    pass


class UserManager(CoreUserManager.from_queryset(UserQuerySet)):
    def create_user(self, username, password=None, **extra_field):
        if not username:
            raise ValueError("User must have a username.")
        user = self.model(username=username, **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **extra_field):
        user = self.create_user(username, password, **extra_field)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


def _upload_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    prefix = str(uuid.uuid4())[:5]
    return "avatars/{prefix}-{name}{ext}".format(
        prefix=prefix,
        name=filename_base,
        ext=filename_ext,
    )


class User(AbstractUser):
    avatar = models.ImageField(blank=True, null=True, upload_to=_upload_to)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.username
