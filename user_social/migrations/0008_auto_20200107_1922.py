# Generated by Django 2.1.5 on 2020-01-07 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_social', '0007_auto_20200105_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow_list',
            name='geek',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geek', to=settings.AUTH_USER_MODEL),
        ),
    ]
