# Generated by Django 3.0.2 on 2020-02-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio Unitario')),
                ('descripcion', models.TextField(max_length=300, verbose_name='Descripción')),
                ('imagen', models.ImageField(upload_to=None, verbose_name='Imagen')),
            ],
        ),
    ]