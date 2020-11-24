from django.db import models
from users.models import User


class Follow(models.Model):
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    approved = models.BooleanField(default=False)
    pending_request = models.BooleanField(default=True)

