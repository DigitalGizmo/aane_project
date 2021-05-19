# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20150413_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aaperson',
            name='birth_year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aaperson',
            name='death_year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operson',
            name='birth_year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operson',
            name='death_year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
