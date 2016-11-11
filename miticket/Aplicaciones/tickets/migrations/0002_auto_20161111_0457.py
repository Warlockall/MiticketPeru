# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='DocScaneado',
            field=models.ImageField(null=True, upload_to=b'Media'),
        ),
    ]
