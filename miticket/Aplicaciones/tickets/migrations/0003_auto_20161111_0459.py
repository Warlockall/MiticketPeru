# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20161111_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='DocScaneado',
            field=models.ImageField(null=True, upload_to=b'Media', blank=True),
        ),
    ]
