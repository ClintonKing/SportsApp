# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0005_auto_20150325_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='photo',
            field=models.CharField(default=b'', unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='roster.Player', blank=True),
            preserve_default=True,
        ),
    ]
