from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializzers import UserSerializer

User = get_user_model()


class UserRegistrationAPIView(CreateAPIView):
    """
    Api to Create New User
    """

    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        res = super(UserRegistrationAPIView, self).create(request, *args, **kwargs)
        user = User.objects.get(email=res.data["email"])
        token = RefreshToken.for_user(user)
        res.data["refresh"] = str(token)
        res.data["access"] = str(token.access_token)
        return res
