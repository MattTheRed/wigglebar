from django.db import models
from django.conf import settings
from django.forms import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Bar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    icon = models.ImageField(upload_to="icons")
    icon_url = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    button_text = models.CharField(max_length=100)
    button_link = models.URLField(max_length=255)
    background_color = models.CharField(max_length=7)
    message_color = models.CharField(max_length=7)
    button_background_color = models.CharField(max_length=7)
    button_text_color = models.CharField(max_length=7)
    BOOL_CHOICES = ((True, 'On'), (False, 'Off'))
    is_enabled = models.BooleanField(choices=BOOL_CHOICES)


    def _get_icon(self):
        if self.icon:
            return self.icon.url
        else:
            return self.icon_url

    get_icon = property(_get_icon)

