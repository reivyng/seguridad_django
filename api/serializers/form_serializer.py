from rest_framework import serializers
from api.models.form import Form


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
