# Generated by Django 2.1.5 on 2020-01-03 13:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_auto_20200103_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='like_by',
        ),
        migrations.AddField(
            model_name='post',
            name='like_by',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
