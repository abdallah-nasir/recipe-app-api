"""
This file contains All logic func for testing
"""
import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    first_name = factory.Sequence(lambda n: f"first_name{n}")
    last_name = factory.Sequence(lambda n: f"last_name{n}")
    password = factory.PostGenerationMethodCall("set_password", "password")
    is_active = True
    is_superuser = False
