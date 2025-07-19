from .rol import Rol
from .form import Form
from .permission import Permission
from django.db import models


class RolFormPermission(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
