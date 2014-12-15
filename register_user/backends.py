from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

# class CaseInsensitiveModelBackend(ModelBackend):
#   """
#   By default ModelBackend does case _sensitive_ username authentication, which isn't what is
#   generally expected.  This backend supports case insensitive username authentication.
#   """
#   def authenticate(self, username=None, password=None):
#     try:
#       user = User.objects.get(username__iexact=username)
#       if user.check_password(password):
#         return user
#       else:
#         return None
#     except User.DoesNotExist:
#       return None

class CaseInsensitiveModelBackend(ModelBackend):
    """
    Authenticate against django.contrib.auth.models.User using
    e-mail address instead of username.
    """
    def authenticate(self, username=None, password=None):
        print "in auth "
        try:
            user = User.objects.get(email__iexact = username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
            try:
                return User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return None
