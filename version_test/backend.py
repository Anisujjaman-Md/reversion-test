from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication

User = get_user_model()

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        try:
            token = self.get_raw_token(header)
            validated_token = self.get_validated_token(token)
            user = self.get_user(validated_token)
        except Exception:
            return None

        return (user, token)

class CustomBackend(JWTAuthentication):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None
        try:
            if '@' in username:
                user = self.get_user(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None