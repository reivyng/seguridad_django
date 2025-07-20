from rest_framework import serializers
from api.models.rol import Rol


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
