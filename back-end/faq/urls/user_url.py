from django.urls import path
from ..viewers import UserViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<uuid:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
]