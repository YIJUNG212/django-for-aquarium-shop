from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.http import HttpResponse
from shopapp.serializers import UserSerializer
from shopapp.views import UserViewSet,VipInfoViewSet#要調用視圖

# Routers註冊區,這裡可以註冊多組視圖,並指定在api/底下的前綴
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vip', VipInfoViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

###額外加的JWT設定,這樣可以把simplejwt內建的兩個viewset模組調用
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)


###JWT token範圍,下面這段沒有會正常嗎?
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
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



urlpatterns = [
    ##根目錄用了include,等於是包括這個router.urls,而這個urls剛剛才register完
    path('api/', include(router.urls)),
    #下面這行拿掉會沒有login的畫面
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #加jwt token path
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('api/tokenall/', TokenObtainPairView.as_view(), name='tokenall'),

]
