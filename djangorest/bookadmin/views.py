from rest_framework.viewsets import ModelViewSet
from .serializer import BookSerializers, UserInfoSerializer, UserGroupSerializer
from .models import BookInfo, HeroInfo, UserInfo
from rest_framework.parsers import JSONParser, FormParser, FileUploadParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet


class BookInfoViews(APIView):
    # authentication_classes = [Authtication, ]   # 用户认证
    # permission_classes = [MyPermission, ]    # 权限认证
    # throttle_classes = [VisitThrottle]   # 访问频率认证
    # versioning_class = URLPathVersioning  # 获取版本  request.version
    parser_classes = [JSONParser, FormParser]  # 解析前端发送数据

    def get(self, request):
        queryset = BookInfo.objects.all()
        serializer = BookSerializers(queryset, many=True)
        return Response(serializer.data)


class UserInfoViews(APIView):
    def get(self, request):
        queryset = UserInfo.objects.all()
        pg = PageNumberPagination()
        pagedata = pg.paginate_queryset(queryset=queryset, request=request, view=self)
        serializer = UserInfoSerializer(pagedata, many=True)
        return Response(serializer.data)

    def post(self, request, ):
        pass


class UserGroupView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        """
        文件上传
        file_obj = request.data['file']
        filename = file_obj._name

        with open(filename, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        """
        json_data = request.data
        ser = UserGroupSerializer(data=json_data)
        if ser.is_valid():
            print(ser.validated_data)
        else:
            print(ser.errors)

        return Response("提交数据")


class ViewSet(GenericViewSet):

    def get(self, request):
        pass