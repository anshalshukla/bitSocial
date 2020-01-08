from django.db import models
from django.contrib.auth.models import User


class Follow_List(models.Model):
    geek = models.OneToOneField(
        User, related_name="geek", on_delete=models.CASCADE, null=True
    )
    follow = models.ManyToManyField(User, related_name="followed_by", blank=True)

    def __str__(self):
        return self.geek.username
