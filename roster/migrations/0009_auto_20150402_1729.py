# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0008_player_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.CharField(default=b'', max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
    ]
