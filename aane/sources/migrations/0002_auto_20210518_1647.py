# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-05-18 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0001_squashed_0013_auto_20150428_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='primarysource',
            options={'ordering': ['source_type', 'title'], 'verbose_name': 'Source'},
        ),
        migrations.AlterModelOptions(
            name='sourceentry',
            options={'ordering': ['low_year', 'low_month', 'low_day']},
        ),
        # migrations.RemoveField(
        #     model_name='sourceentry',
        #     name='location',
        # ),
        migrations.AlterField(
            model_name='sourceentry',
            name='operson_id',
            field=models.IntegerField(blank=True, help_text="blank if free. If unknown, choose the special 'Unknow Owner", null=True, verbose_name='Owner ID'),
        ),
    ]
