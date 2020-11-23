from django.db import models
from users.models import User


class Follow(models.Model):
    followed = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
