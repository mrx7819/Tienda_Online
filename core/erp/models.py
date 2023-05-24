from django.db import models
from datetime import datetime
# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, null=False, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, unique=True)
    contraseña = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=9, null=False, unique=True)