import os
import uuid

from django.db import models

from .portfolio import Portfolio


def _upload_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    prefix = str(uuid.uuid4())[:5]
    return "portfolio/{prefix}-{name}{ext}".format(
        prefix=prefix,
        name=filename_base,
        ext=filename_ext,
    )


class PortfolioFile(models.Model):
    image = models.ImageField(upload_to=_upload_to, max_length=255)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
