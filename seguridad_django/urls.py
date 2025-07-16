from django.contrib import admin
from django.urls import path, include
from api.config.swagger import schema_view
from django.urls import path
from api.controllers.views import (
    UserListView,
    ProductoListView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.routes.urls')),
    path('users/', UserListView.as_view(), name='user-list'),
    path('productos/', ProductoListView.as_view(), name='producto-list'),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
