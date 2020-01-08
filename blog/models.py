from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name="liked_by")

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        "blog.Post", on_delete=models.CASCADE, related_name="comments", null=True
    )

    def __str__(self):
        return self.comment

