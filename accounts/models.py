from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def _create_user(self, name, is_staff, is_superuser, password, **extra_fields):
        user = self.model(
            name=name,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, **extra_fields):
        return self._create_user(name, False, False, **extra_fields)

    def create_superuser(self, name, **extra_fields):
        user = self._create_user(name, True, True, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    name = models.CharField('Full Name', max_length=35, unique=True, null=False, blank=False)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
