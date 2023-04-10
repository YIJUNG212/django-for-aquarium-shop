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


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

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
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response({'detail': '找不到資源。'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MemberSerializer(member, data=request.data)
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