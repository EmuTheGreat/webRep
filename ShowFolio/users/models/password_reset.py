from django.db import models
from uuid import uuid4


class PasswordResetRecord(models.Model):
    user_id = models.IntegerField()
    uuid = models.UUIDField(default=uuid4)

    create_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
