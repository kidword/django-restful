from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class Authtication(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get("token")
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        # return 'vain', 'test'
