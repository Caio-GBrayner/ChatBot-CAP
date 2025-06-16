
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from ..viewers.auth_viewer import (
    CustomTokenObtainPairView,
    CustomTokenVerifyView,
    logout_view,
)
from ..views.user_views import UserRegisterView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('logout/', logout_view, name='auth_logout'),
    path('register/', UserRegisterView.as_view())
]
