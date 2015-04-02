# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0007_remove_player_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='photo',
            field=models.CharField(default=b'', unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
