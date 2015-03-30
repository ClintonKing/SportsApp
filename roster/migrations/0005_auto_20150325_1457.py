# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0004_auto_20150325_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.IntegerField(max_length=2),
            preserve_default=True,
        ),
    ]
