from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _




class CustomAccountManager(BaseUserManager):

    def create_user(self, username, password):
        if not username:
            raise ValueError("User must have an username")
        if not password:
            raise ValueError("User must have an password")

        user = self.model(username=username)
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, university, password):
        if not username:
            raise ValueError("User must have an username")
        if not password:
            raise ValueError("User must have an password")

        user = self.model(username=username)
        user.university = university
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=20, unique=True)
    university = models.CharField(max_length=40)
    session_id = models.CharField(max_length=70, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    objects = CustomAccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['university']

    def __str__(self):
        return self.username
