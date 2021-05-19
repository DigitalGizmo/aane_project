# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20150413_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aaperson',
            name='first_appearance_year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='free_start_year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='last_appearance_year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='owner_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
