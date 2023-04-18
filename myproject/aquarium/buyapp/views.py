from django.contrib.auth.models import User
from rest_framework import generics
from .serializer import UserSerializer
from django.shortcuts import HttpResponse

from rest_framework import viewsets
from .serializer import MemberSerializer
from .models import Member

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import QueryDict

from django.db.models import Max
from rest_framework.decorators import action

#import 資料表register
from .models import Register
#import 最大值的函式,因為等等要用這個來處理ID問題
from django.db.models import Max
#解析器也要import

from .serializer import RegisterSerializer

from django.shortcuts import get_object_or_404
from django.http import QueryDict
from django.db.models import Max

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Register
from .serializer import RegisterSerializer




from django.shortcuts import get_object_or_404
from django.http import QueryDict
from django.db.models import Max

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
###VipInfo範圍


from .models import VipInfo
from .serializer import VipInfoSerializer

class VipInfoViewSet(viewsets.ModelViewSet):
    queryset = VipInfo.objects.all()
    serializer_class = VipInfoSerializer
####律定格式範圍#####
    def parse_form_data(self, data):
        # 將非 JSON 格式的 POST 請求轉成 QueryDict 格式
        if isinstance(data, QueryDict):
            # 如果已經是 QueryDict 格式，就直接返回
            return data

        # 取得請求標頭中的 Content-Type 值
        content_type = self.request.META.get('CONTENT_TYPE', '').split(';')[0].lower()

        # 如果 Content-Type 為 application/x-www-form-urlencoded，則使用 QueryDict 解析
        if content_type == 'application/x-www-form-urlencoded':
            return QueryDict(data)

        # 如果 Content-Type 為 multipart/form-data，則使用 request.POST 解析
        elif content_type == 'multipart/form-data':
            return self.request.POST

        # 其他情況，就直接返回原始請求數據
        else:
            return data
    ####律定格式範圍#####

    @action(detail=False, methods=['get'])
    def max_id(self, request):
        max_id = self.queryset.aggregate(Max('id'))['id__max']
        return Response({'max_id': max_id})

    def list(self, request):
        queryset = self.get_queryset()
        serializer = VipInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = VipInfo.objects.all()
        register = get_object_or_404(queryset, pk=pk)
        serializer = VipInfoSerializer(register)
        return Response(serializer.data)

    def create(self, request):
        data = self.parse_form_data(request.data)
        serializer = VipInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            register = VipInfo.objects.get(pk=pk)
        except VipInfo.DoesNotExist:
            return Response({'detail': '找不到資源。'}, status=status.HTTP_404_NOT_FOUND)

        data = self.parse_form_data(request.data)
        serializer = VipInfoSerializer(register, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            register = VipInfo.objects.get(pk=pk)
        except VipInfo.DoesNotExist:
            return Response({'detail': '找不到資源。'}, status=status.HTTP_404_NOT_FOUND)

        register.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

######################################
##############################################
#Register範圍
from .models import Register
from .serializer import RegisterSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
####律定格式範圍#####
    def parse_form_data(self, data):
        # 將非 JSON 格式的 POST 請求轉成 QueryDict 格式
        if isinstance(data, QueryDict):
            # 如果已經是 QueryDict 格式，就直接返回
            return data

        # 取得請求標頭中的 Content-Type 值
        content_type = self.request.META.get('CONTENT_TYPE', '').split(';')[0].lower()

        # 如果 Content-Type 為 application/x-www-form-urlencoded，則使用 QueryDict 解析
        if content_type == 'application/x-www-form-urlencoded':
            return QueryDict(data)

        # 如果 Content-Type 為 multipart/form-data，則使用 request.POST 解析
        elif content_type == 'multipart/form-data':
            return self.request.POST

        # 其他情況，就直接返回原始請求數據
        else:
            return data
    ####律定格式範圍#####

    @action(detail=False, methods=['get'])
    def max_id(self, request):
        max_id = self.queryset.aggregate(Max('id'))['id__max']
        return Response({'max_id': max_id})

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RegisterSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Register.objects.all()
        register = get_object_or_404(queryset, pk=pk)
        serializer = RegisterSerializer(register)
        return Response(serializer.data)

    def create(self, request):
        data = self.parse_form_data(request.data)
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            register = Register.objects.get(pk=pk)
        except Register.DoesNotExist:
            return Response({'detail': '找不到資源。'}, status=status.HTTP_404_NOT_FOUND)

        data = self.parse_form_data(request.data)
        serializer = RegisterSerializer(register, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            register = Register.objects.get(pk=pk)
        except Register.DoesNotExist:
            return Response({'detail': '找不到資源。'}, status=status.HTTP_404_NOT_FOUND)

        register.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


####################################################

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def parse_form_data(self, data):
        # 將非 JSON 格式的 POST 請求轉成 QueryDict 格式
        if isinstance(data, QueryDict):
            # 如果已經是 QueryDict 格式，就直接返回
            return data

        # 取得請求標頭中的 Content-Type 值
        content_type = self.request.META.get('CONTENT_TYPE', '').split(';')[0].lower()

        # 如果 Content-Type 為 application/x-www-form-urlencoded，則使用 QueryDict 解析
        if content_type == 'application/x-www-form-urlencoded':
            return QueryDict(data)

        # 如果 Content-Type 為 multipart/form-data，則使用 request.POST 解析
        elif content_type == 'multipart/form-data':
            return self.request.POST

        # 其他情況，就直接返回原始請求數據
        else:
            return data

    @action(detail=False,methods=['get'])
    def max_id(self,request):
        max_id =self.queryset.aggregate(Max('id'))['id__max']
        return Response({'max_id':max_id})

    def list(self, request):
        queryset = self.get_queryset()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Member.objects.all()
        member = get_object_or_404(queryset, pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def create(self, request):
        data = self.parse_form_data(request.data)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response({'detail': '找不到資源。'}, status=status.HTTP_404_NOT_FOUND)

        data = self.parse_form_data(request.data)
        serializer = MemberSerializer(member, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response({'detail': '找不到資源。'}, status=status.HTTP_404_NOT_FOUND)

        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    return HttpResponse("我是主頁")








# @require_http_methods(['GET'])
# def my_view(request):
#     # your view code here
#     pass

# def redirect_to_https(view_func):
#     def wrapper(request, *args, **kwargs):
#         if not request.is_secure():
#             url = request.build_absolute_uri(request.get_full_path())
#             secure_url = url.replace("http://", "https://")
#             return redirect(secure_url)
#         return view_func(request, *args, **kwargs)
#     return wrapper
# def index(request):
#     return HttpResponse("test")