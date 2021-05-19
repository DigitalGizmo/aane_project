# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20150311_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='operson',
            name='title',
            field=models.CharField(max_length=24, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='operson',
            name='year_lower',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='operson',
            name='year_upper',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='bio',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='first_name',
            field=models.CharField(max_length=32, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='last_name',
            field=models.CharField(max_length=32, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='place_of_origin',
            field=models.CharField(max_length=64, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operson',
            name='bio',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operson',
            name='first_name',
            field=models.CharField(max_length=32, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operson',
            name='last_name',
            field=models.CharField(max_length=32, default='', blank=True),
            preserve_default=True,
        ),
    ]
