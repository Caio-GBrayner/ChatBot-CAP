from django.db import models

class UserType(models.TextChoices):
    ADMIN = 'AD'
    EDITOR = 'ED'
    VIEWER = 'VW'