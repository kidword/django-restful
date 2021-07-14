from rest_framework import serializers
from .models import BookInfo, HeroInfo

"""bookadmin应用序列化器定义"""


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"   # 所有字段


class HeroInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        fields = "__all__"
        depth = 1  # 关联表深度

    bookname = serializers.SerializerMethodField()

    hbook = serializers.CharField(required=True)
    hgender = serializers.CharField(required=True)

    # 获取外键关联字段
    def get_bookname(self, obj):
        return obj.hbook.btitle
