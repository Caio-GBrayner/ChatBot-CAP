from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenVerifyView,
)
from rest_framework.response import Response
from rest_framework import status
from ..serializers import CustomTokenObtainPairSerializer
from rest_framework.decorators import (
    api_view,
    permission_classes,
)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenVerifyView(TokenVerifyView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            from rest_framework_simplejwt.tokens import UntypedToken
            token = request.data.get('token')
            decoded = UntypedToken(token)
            response.data.update(decoded.payload)
        return response

@api_view(['POST'])
def logout_view(request):
    response = Response(
        {"detail": "Success logout"},
        status=status.HTTP_200_OK
    )

    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')

    return response