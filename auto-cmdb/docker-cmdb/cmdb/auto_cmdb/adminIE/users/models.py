from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UsersProfile(AbstractUser):
    mobile = models.CharField('手机', max_length=11)
