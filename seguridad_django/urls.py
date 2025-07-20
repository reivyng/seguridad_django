from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# Swagger imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Seguridad API",
        default_version='v1',
        description="Documentación del backend del sistema de seguridad",
        terms_of_service="https://www.tusitio.com/terminos/",
        contact=openapi.Contact(email="fabrianymedina9@gmail.com"),
        license=openapi.License(name="Licencia BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('api/v1/', include('api.routes.urls')),  # Usa include aquí

    # Documentation
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
