"""
Test user models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class ModelTests(TestCase):
    def test_valid_user_credentials(self):
        user = User.objects.create_user(email="test@test.com", password="password")
        self.assertEqual(user.email, "test@test.com")
        self.assertTrue(user.check_password("password"))

    def test_incomplete_user_credentials(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="password")

    def test_create_superuser(self):
        user = User.objects.create_superuser(email="test@test.com", password="password")
        self.assertTrue(user.is_superuser)
