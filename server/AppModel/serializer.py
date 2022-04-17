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

class ExamScoreInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamScore
        fields = ('user_name','company_name','score')
class QuestionBankSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionBank
        fields = ('title','qtype','a','b','c','d','e','answer','score')
