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