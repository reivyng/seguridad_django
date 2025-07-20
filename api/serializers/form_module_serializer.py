from rest_framework import serializers
from api.models.form_module import FormModule


class FormModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormModule
        fields = '__all__'
