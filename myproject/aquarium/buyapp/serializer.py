
from rest_framework import serializers

from .models import Member
#有要用USER模式的,要import USER這張內建的資料表
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #下面這行指令其實也可以改成 fields="__all__"
        fields = ['id', 'username', 'email']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields="__all__"

from .models import VipInfo
class VipInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=VipInfo
        fields="__all__"

#先import 資料表

from .models import Register
#import一個Serializer
from rest_framework import serializers
#創立一個資料解析的類別
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        #設定資料表是用Register
        model=Register
        #解析欄位是所有
        fields="__all__"



