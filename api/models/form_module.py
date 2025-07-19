from .form import Form
from .module import Module
from django.db import models


class FormModule(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
