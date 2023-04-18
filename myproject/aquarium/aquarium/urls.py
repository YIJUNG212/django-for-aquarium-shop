from django.urls import path, include
from rest_framework import routers
from buyapp.views import UserList, MemberViewSet, index

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
#要註冊想要出現的ViewSet
#先將router初始化
#router2 = routers.DefaultRouter()
#註冊前請先引用對應的ViewSet
from buyapp.views import RegisterViewSet
#要使用path include 及routers 也要import 相關設定
from django.urls import path, include
from rest_framework import routers
#註冊ViewSet
router.register(r'register', RegisterViewSet,basename="register")

#這裡設定只要有path('api/', include(router.urls)), 跟上面的router = routers.DefaultRouter(),就會自動加入ViewSet
urlpatterns = [
    path('', index),
    path('users/', UserList.as_view(), name='user-list'),
    path('api/', include(router.urls)),
    
    #path('myapi/', include(router2.urls)),
]