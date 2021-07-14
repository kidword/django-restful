from rest_framework import exceptions


class Authtication():
    def authenticate(self, request):
        token = request.GET.get("token")
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return 'vain', 'test'

    def authenticate_header(self, request):
        pass
