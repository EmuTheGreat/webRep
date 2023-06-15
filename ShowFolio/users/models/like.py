from django.db import models

from .user import User
from .portfolio import Portfolio


class PortfolioLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="likes"
    )

    created_at = models.DateTimeField(auto_now_add=True)
