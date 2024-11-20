from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
# from django.conf import settings


class SharedAPIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('Authorization')
        # Check if the API key matches the key in settings
        if api_key == "CS218":
            return (None, None)  # No user associated, just allow access
        else:
            raise AuthenticationFailed('Invalid API key')
