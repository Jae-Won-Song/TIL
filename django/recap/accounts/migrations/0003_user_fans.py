# Generated by Django 3.2.16 on 2023-01-18 02:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_mbti'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fans',
            field=models.ManyToManyField(related_name='stars', to=settings.AUTH_USER_MODEL),
        ),
    ]
