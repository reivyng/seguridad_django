from rest_framework import viewsets
from api.models.form import Form
from api.serializers.form_serializer import FormSerializer


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
