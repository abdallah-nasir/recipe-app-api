from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class RecipeApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"Recipies Api": "Ok"})


schema_view = get_schema_view(
    openapi.Info(
        title="Recipe API",
        default_version="v0",
        description="Test Recipe Api",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="abdallah.nasir@ymail.com"),
        license=openapi.License(name="Recipe Api License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
