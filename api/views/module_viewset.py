from rest_framework import viewsets
from api.models.module import Module
from api.serializers.module_serializer import ModuleSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
