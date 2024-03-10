"""
Test user models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class ModelTests(TestCase):
    def test_valid_user_credentials(self):
        pass
