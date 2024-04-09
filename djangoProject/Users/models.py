from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    USER_CHOICES = (
        ('admin','ADMIN'),
        ('editor', 'EDITOR'),
        ('viwer', 'VIWER')

    )

    email = models.EmailField('email',unique=True)
    usertype = models.CharField(max_length=20, choices= USER_CHOICES, default='galerist')
    img = models.ImageField(upload_to='media', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIDER_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('created_at',)