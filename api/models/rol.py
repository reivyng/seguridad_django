from django.db import models


class Rol(models.Model):
    type_rol = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.type_rol
