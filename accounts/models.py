from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='media/accounts/', blank=True, default='media/accounts/img.png')
