from django.db import models
from django.conf import settings
from django.utils.http import urlquote
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class BarUserManager(BaseUserManager):
    def create_user(self, email,
                    password=None):
        print "made it here"
        email = self.normalize_email(email).lower()
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.save(using=self._db)
        print "and here"
        return user

    def create_superuser(self, email,
                         password):
        print "Password:", password
        user = self.create_user(email,
                                password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        print user
        print user.password
        return user

class BarUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    website_url = models.URLField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = BarUserManager()
    #REQUIRED_FIELDS = ["email"]

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.id)

