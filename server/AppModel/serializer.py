from rest_framework import serializers
from AppModel.models import *
from rest_framework.decorators import api_view


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ('nick_name','user_name','weixin_openid','phone_number')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ('weixin_id','phone_number')

class TestPaperInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestPaperInfo
        fields = ('title','starttime','endtime','examtime','pid')