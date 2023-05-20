# Generated by Django 4.0.4 on 2023-05-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de Empleado',
                'verbose_name_plural': 'Tipos de Empleados',
                'db_table': 'tipo_empleado',
                'ordering': ['id'],
            },
        ),
    ]