# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0003_auto_20150409_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarysource',
            name='operson_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='O Person id if known'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='year_end',
            field=models.IntegerField(blank=True, null=True, verbose_name='End year if range'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='year_start',
            field=models.IntegerField(blank=True, null=True, verbose_name='Start year or single'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='aa_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='aa id if known for sure'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='day',
            field=models.IntegerField(blank=True, null=True, verbose_name='Day of month (number)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='month',
            field=models.IntegerField(blank=True, null=True, verbose_name='Month (number)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='operson_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='2ndary person ID, only if aa id not known'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='year_end',
            field=models.IntegerField(blank=True, null=True, verbose_name='End year if range'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='year_start',
            field=models.IntegerField(blank=True, null=True, verbose_name='Start year or single'),
            preserve_default=True,
        ),
    ]
