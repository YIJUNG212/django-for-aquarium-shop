
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
############真正的會員系統######
from .models import VipInfodata
import datetime
class VipInfoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=VipInfodata
        fields="__all__"
    # def to_internal_value(self, data):
    #     if 'cBirthday' in data:
    #         # 將傳入的日期字串轉換成 datetime.date 對象
    #         data['cBirthday'] = datetime.datetime.strptime(data['cBirthday'], '%Y-%m-%d').date()
    #     return super().to_internal_value(data)

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



###############這裡是restframwork提供內建的USERSET範圍
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')