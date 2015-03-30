# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('number', models.CharField(unique=True, max_length=2)),
                ('hand', models.CharField(max_length=4)),
                ('height', models.CharField(max_length=5)),
                ('year', models.CharField(max_length=10)),
                ('hometown', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Players',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('name',), 'verbose_name_plural': 'Teams'},
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='roster.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='school',
            field=models.CharField(default=b'', unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
