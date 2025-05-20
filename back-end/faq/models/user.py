import uuid
from django.db import models
from .enums import UserType
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default= uuid.uuid4)
    username = models.CharField(max_length=150, null= False, blank=False, unique=True)
    first_name = None
    last_name = None
    email = models.EmailField(null=True, blank=True)
    user_type = models.CharField(max_length=2, choices=UserType.choices, default=UserType.VIEWER)
    # created_at = models.DateTimeField(auto_now_add=True)

    # def email(self) -> str :
    #     return ''

    # def save(self, *args, **kwargs):
    #     if self.user_type == UserType.ADMIN:
    #         self.is_staff = True
    #         self.is_superuser = True
    #     elif self.user_type == UserType.EDITOR:
    #         self.is_staff = True
    #         self.is_superuser = False
    #     else:
    #         self.is_staff = False
    #         self.is_superuser = False
    #
    #     self.is_active = True
    #     super().save(*args, **kwargs)
    #
    # def has_perm(self, perm, obj=None):
    #     if self.user_type == UserType.ADMIN:
    #         return True
    #     elif self.user_type == UserType.EDITOR:
    #         return perm in ['add', 'change', 'delete', 'create']
    #     return False

    class Meta:
        swappable = 'AUTH_USER_MODEL'