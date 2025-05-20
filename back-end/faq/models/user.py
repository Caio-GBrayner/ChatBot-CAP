import uuid
from django.db import models
from .enums import UserType
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default= uuid.uuid4)
    username = models.CharField(max_length=150, null= False, blank=False, unique=True)
    first_name = None
    last_name = None
    email = None
    user_type = models.CharField(max_length=2, choices=UserType.choices, default=UserType.VIEWER)
    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'