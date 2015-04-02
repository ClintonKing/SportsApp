# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0009_auto_20150402_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='photo',
        ),
    ]
