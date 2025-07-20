from rest_framework import viewsets
from api.models.rol_form_permission import RolFormPermission
from api.serializers.rol_form_permission_serializer import (
    RolFormPermissionSerializer as RFPSerializer
)


class RolFormPermissionViewSet(viewsets.ModelViewSet):
    queryset = RolFormPermission.objects.all()
    serializer_class = RFPSerializer
