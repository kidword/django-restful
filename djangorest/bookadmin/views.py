from rest_framework.viewsets import ModelViewSet
from .serializer import BookSerializers, HeroInfoSerializers
from .models import BookInfo, HeroInfo
from .authtication import Authtication


class BookInfoViews(ModelViewSet):
    authentication_classes = [Authtication, ]   # 认证设置

    serializer_class = BookSerializers
    queryset = BookInfo.objects.all()


class HeroInfoViews(ModelViewSet):
    serializer_class = HeroInfoSerializers
    queryset = HeroInfo.objects.all()

