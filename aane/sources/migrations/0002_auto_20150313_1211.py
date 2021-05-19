# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='primarysource',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='day',
            field=models.IntegerField(default=0, verbose_name='Day of month (number)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='month',
            field=models.IntegerField(default=0, verbose_name='Month (number)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='year_end',
            field=models.IntegerField(default=0, verbose_name='End year if range'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='year_start',
            field=models.IntegerField(default=0, verbose_name='Start year or single'),
            preserve_default=True,
        ),
    ]
