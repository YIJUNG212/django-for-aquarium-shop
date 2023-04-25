from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.http import HttpResponse

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
     # 将 is_staff 设置为只读
    is_staff = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['id','url', 'username','password', 'email', 'is_staff']

### ViewSets define the view behavior.
#權限問題要導入
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions
#密碼問題要引入
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth.hashers import make_password
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    AUTHENTICATION_CLASSES=[]
    #authentication_classes = [JWTAuthentication,]   這個應該是要加在其他需要token進入的viewset
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff:
                # 管理员可以查看、修改和删除所有用户信息
                return User.objects.all()
            else:
                # 普通用户只能查看自己的信息
                return User.objects.filter(pk=user.pk)
        # 未登录用户不能查看任何用户信息
        return User.objects.none()
    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # 未登录用户可以看到创建新数据记录的页面
            return self.create(request, *args, **kwargs)
        return super().list(request, *args, **kwargs)
    def perform_create(self, serializer):
         # 將密碼加密後再存儲使用者
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        serializer.save()

    def perform_update(self, serializer):
        # 更新用户信息时确保只能更新当前登录用户的信息
        user = self.request.user
        if user == serializer.instance or user.is_staff:
            # 只有用户本人或管理员可以修改用户信息
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
        else:
            raise PermissionDenied("You don't have permission to update this user.")

    def perform_destroy(self, instance):
        # 删除用户信息时确保只能删除当前登录用户的信息
        user = self.request.user
        if user == instance:
            raise PermissionDenied("You don't have permission to delete your own account.")
        elif user.is_staff:
            # 只有管理员可以删除用户信息
            instance.delete()
        else:
            raise PermissionDenied("You don't have permission to delete this user.")
# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

###額外加的JWT設定
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)


urlpatterns = [
    ##根目錄用了include,等於是包括這個router.urls,而這個urls剛剛才register完
    path('api/', include(router.urls)),
    #下面這行拿掉會沒有login的畫面
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #加jwt token path
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),

]

###JWT token範圍
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.name
        # ...

        return token
###用戶手動創建 token
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }