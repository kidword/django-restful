from rest_framework import serializers
from .models import BookInfo, HeroInfo, UserInfo

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


"""
class UserInfoSerializer(serializers.Serializer):
    ooo = serializers.CharField(source="get_user_type_display")
    username = serializers.CharField()
    password = serializers.CharField()
    gp = serializers.CharField(source="group.user_type")
    # rls = serializers.CharField(source="roles.all")
    rls = serializers.SerializerMethodField()  # 自定义显示

    def get_rls(self, row):
        role_obj_list = row.roles.all()
        ret  = []
        for item in role_obj_list:
            ret.append({'id': item.id, 'title': item.title})
        return ret
"""


class UserInfoSerializer(serializers.ModelSerializer):
    # group = serializers.HyperlinkedIdentityField(view_name='gp', lookup_field='group_id', lookup_url_kwarg='pk')

    class Meta:
        model = UserInfo
        fields = ['id', 'username' ,'group', 'roles']   # [id, username,]
        # extra_kwargs = {"group": {'source': 'group.user_type'}}
        # depth = 1


class PasswordValidator(object):
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if value != self.base:
            message = 'This field must be %s.' % self.base
            raise serializers.ValidationError(message)

    def set_context(self, serializer_field):
        """
        This hook is called by the serializer instance,
        prior to the validation call being made.
        """
        # 执行验证之前调用,serializer_fields是当前字段对象
        pass


class UserGroupSerializer(serializers.Serializer):
    title = serializers.CharField(error_messages={'required': '标题不能为空'}, validators=[PasswordValidator('yes')])