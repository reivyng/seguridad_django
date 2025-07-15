from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API de Seguridad con Django",
      default_version='v1',
      description="Documentación de la API con autenticación JWT",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="soporte@tudominio.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

