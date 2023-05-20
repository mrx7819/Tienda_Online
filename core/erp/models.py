from django.db import models
from datetime import datetime
# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    rut = models.CharField(max_length=12, verbose_name='Rut', unique=True, null=False)
    fecha_entrada = models.DateField(verbose_name='Fecha de entrada', default=datetime.now)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    edad = models.PositiveBigIntegerField(verbose_name='Edad', default=0)
    salario = models.DecimalField(verbose_name='Salario', max_digits=9, decimal_places=2, default=0.00)
    estado = models.BooleanField(verbose_name='Estado', default=True)
    foto_perfil = models.ImageField(upload_to='media/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
    
class TipoEmpleado (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=50, verbose_name='Descripcion')
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Tipo de Empleado'
        verbose_name_plural = 'Tipos de Empleados'
        db_table = 'tipo_empleado'
        ordering = ['id']