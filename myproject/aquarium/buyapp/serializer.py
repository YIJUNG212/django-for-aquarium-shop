from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Member

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
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



