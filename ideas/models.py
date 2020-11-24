from django.db import models
from datetime import datetime

from users.models import User

VISIBILITY_CHOICES = (
    ("PUBLIC", "PUBLIC"),
    ("PROTECTED", "PROTECTED"),
    ("PRIVATE", "PRIVATE")
)


class Idea(models.Model):
    text = models.TextField(blank=False, max_length=254)
    visibility = models.CharField(
        max_length=20,
        choices=VISIBILITY_CHOICES,
        default='PUBLIC'
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now)

