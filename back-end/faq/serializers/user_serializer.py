from rest_framework import  serializers
from ..models import User
from ..models.enums import UserType


class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=UserType.choices)

    class Meta:
        model = User
        fields = ['id', 'username', 'user_type', 'created_at', 'password']
        extra_kwargs = {
            'password' : {'write_only': True},
            'created_at': {'read_only': True},
        }