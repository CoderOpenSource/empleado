# Generated by Django 4.1.4 on 2023-01-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0006_empleado_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(null=True, upload_to='empleado'),
        ),
    ]