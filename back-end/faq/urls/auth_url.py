
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from ..viewers.auth_viewer import (
    CustomTokenObtainPairView,
    CustomTokenVerifyView,
    logout_view,
)

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('logout/', logout_view, name='auth_logout'),
]