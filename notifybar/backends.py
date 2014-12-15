from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class CaseInsensitiveModelBackend(ModelBackend):
    """
    Authenticate against django.contrib.auth.models.User using
    e-mail address instead of username.
    """

    def authenticate(self, username=None, email=None, password=None):
        try:
            if username:
                email = username
            user = User.objects.get(email__iexact = email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
