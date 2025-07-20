from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.form_viewset import FormViewSet
from api.views.form_module_viewset import FormModuleViewSet
from api.views.module_viewset import ModuleViewSet
from api.views.permission_viewset import PermissionViewSet
from api.views.person_viewset import PersonViewSet
from api.views.rol_viewset import RolViewSet
from api.views.rol_form_permission_viewset import RolFormPermissionViewSet
from api.views.user_viewset import UserViewSet

router = DefaultRouter()
router.register(r'forms', FormViewSet)
router.register(r'form-modules', FormModuleViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'roles', RolViewSet)
router.register(r'rol-form-permissions', RolFormPermissionViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
