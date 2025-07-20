from rest_framework import serializers
from api.models.rol_form_permission import RolFormPermission


class RolFormPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolFormPermission
        fields = '__all__'
