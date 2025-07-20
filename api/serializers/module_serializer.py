from rest_framework import serializers
from api.models.module import Module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
