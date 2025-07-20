from rest_framework import viewsets
from api.models.person import Person
from api.serializers.person_serializer import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
