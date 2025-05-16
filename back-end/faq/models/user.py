import uuid
from django.db import models
from .enums import UserType

class User (models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default= uuid.uuid4)
    username = models.CharField(max_length=255, null= False, blank=False, unique=True)
    password = models.TextField(null= False, blank=False)
    user_type = models.CharField(max_length=2, choices=UserType.choices, default=UserType.VIEWER)
    created_at = models.DateTimeField(auto_now_add=True)