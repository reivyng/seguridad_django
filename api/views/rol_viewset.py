from rest_framework import viewsets
from api.models.rol import Rol
from api.serializers.rol_serializer import RolSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
