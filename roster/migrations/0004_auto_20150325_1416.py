# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0003_player_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('number',), 'verbose_name_plural': 'Players'},
        ),
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.IntegerField(unique=True, max_length=2),
            preserve_default=True,
        ),
    ]
