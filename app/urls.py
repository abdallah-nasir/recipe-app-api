import sys
from django.contrib import admin
from django.urls import path, include
from .views import schema_view, RecipeApiView
from django.conf import settings


urlpatterns = [
    path("", RecipeApiView.as_view(), name="hello"),
    path("admin/", admin.site.urls),
    path("accounts/", include("users.urls", namespace="accounts")),
    # Swagger
    path("docs<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
if getattr(settings, "DEBUG", False) and "test" not in sys.argv:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
