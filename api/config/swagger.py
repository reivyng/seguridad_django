from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API de Seguridad Django",
        default_version='v1',
        description="Documentación de la API para el sistema de seguridad",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
