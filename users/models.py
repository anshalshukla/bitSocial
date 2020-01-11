from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notify = models.BooleanField(User, default=True)
    image = models.ImageField(default="default.png", upload_to="profile.pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            new_size = (200, 200)
            img.thumbnail(new_size)
            img.save(self.image.path)

