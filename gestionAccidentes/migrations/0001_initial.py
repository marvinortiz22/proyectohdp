# Generated by Django 3.2.13 on 2022-06-16 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteAccidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=20)),
                ('municipio', models.CharField(max_length=30)),
                ('lugar', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accidente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionAccidentes.reporteaccidente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DatosExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantVictimas', models.IntegerField(blank=True, null=True, verbose_name='Cantidad de victimas')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='images')),
                ('accidente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionAccidentes.reporteaccidente')),
            ],
        ),
    ]
