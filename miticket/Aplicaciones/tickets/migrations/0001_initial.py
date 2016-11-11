# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NombresApellidos', models.CharField(max_length=100)),
                ('TipoDoc', models.CharField(max_length=10)),
                ('NumeroDoc', models.CharField(max_length=20)),
                ('Nacionalidad', models.CharField(max_length=20)),
                ('FechaNac', models.DateField()),
                ('Telefono', models.CharField(max_length=15, null=True, blank=True)),
                ('DocScaneado', models.ImageField(upload_to=b'Media')),
                ('Observacion', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lugares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Origen', models.CharField(max_length=30)),
                ('Destino', models.CharField(max_length=30)),
                ('Categoria', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Lugares',
            },
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FechaIda', models.DateField()),
                ('FechaVuelta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('LugarEntrega', models.CharField(max_length=100)),
                ('Comprado', models.BooleanField(default=False)),
                ('Email', models.EmailField(max_length=254, null=True, blank=True)),
                ('FechaReserva', models.DateField(auto_now_add=True)),
                ('IdCliente', models.ManyToManyField(to='tickets.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tarifa', models.CharField(max_length=20, null=True, blank=True)),
                ('Precio', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('FechaCreacion', models.DateField(auto_now_add=True)),
                ('IdLugar', models.ForeignKey(to='tickets.Lugares')),
            ],
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TipoTransporte', models.CharField(max_length=20)),
                ('NombreTransporte', models.CharField(max_length=20)),
                ('PrivadoGrupal', models.CharField(max_length=10, choices=[(b'Privado', b'Privado'), (b'Grupal', b'Grupal')])),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='IdTransporte',
            field=models.ForeignKey(to='tickets.Transporte'),
        ),
        migrations.AddField(
            model_name='paquete',
            name='IdTour',
            field=models.ManyToManyField(to='tickets.Tour'),
        ),
    ]
