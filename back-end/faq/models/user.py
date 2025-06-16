import uuid
from django.db import models
from .enums import UserType
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default= uuid.uuid4)
    username = models.CharField(max_length=150, null= False, blank=False, unique=True)
    first_name = None
    last_name = None
    email = models.EmailField(null=True, blank=True, unique=True)
    user_type = models.CharField(max_length=2, choices=UserType.choices, default=UserType.VIEWER)

    def save(self, *args, **kwargs):
        if self.user_type == UserType.ADMIN:
            self.is_superuser=True

        elif self.user_type == UserType.EDITOR:
            self.is_staff=True
            self.is_superuser=False

        else:
            self.is_staff=False
            self.is_superuser=False
        self.is_active =True

        super().save(*args, **kwargs)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
