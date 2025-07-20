from rest_framework import viewsets
from api.models.form_module import FormModule
from api.serializers.form_module_serializer import FormModuleSerializer


class FormModuleViewSet(viewsets.ModelViewSet):
    queryset = FormModule.objects.all()
    serializer_class = FormModuleSerializer
