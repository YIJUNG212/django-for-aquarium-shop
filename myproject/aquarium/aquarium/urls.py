from django.urls import path, include
from rest_framework import routers
from buyapp.views import UserList, MemberViewSet, index

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)


urlpatterns = [
    path('', index),
    path('users/', UserList.as_view(), name='user-list'),
    path('api/', include(router.urls)),
]