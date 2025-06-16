from django.test import TestCase
# from ..models import User
from ..models.enums import UserType
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            username="testuser",
            password="testpass123",
            user_type=UserType.VIEWER
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.user_type, UserType.VIEWER)
        self.assertTrue(user.id)

    def test_user_type_choices(self):
        choices = User._meta.get_field('user_type').choices
        self.assertEqual(choices, UserType.choices)