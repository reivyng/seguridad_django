from rest_framework import viewsets
from api.models.permission import Permission
from api.serializers.permission_serializer import PermissionSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
