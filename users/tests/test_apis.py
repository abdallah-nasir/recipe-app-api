"""
Test user's Api endpoints
"""
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class TestUserApi(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_creation_success(self):
        """Test creating a new user"""
        url = reverse("accounts:register")
        data = {
            "email": "test@test.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "password": "password",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for key, value in data.items():
            if key != "password":
                self.assertEqual(value, response.data[key])

    def test_user_creatation_with_wrong_password(self):
        """Test creating a new user"""
        url = reverse("accounts:register")
        data = {
            "email": "",
            "first_name": "first_name",
            "last_name": "last_name",
            "password": "",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)
        self.assertIn("email", response.data)
