from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=127)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Post(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
