# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20161111_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='IdPaquete',
            field=models.ForeignKey(default=1, to='tickets.Paquete'),
            preserve_default=False,
        ),
    ]
