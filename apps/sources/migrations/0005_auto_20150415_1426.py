# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0004_auto_20150415_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarysource',
            name='source_type',
            field=models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], max_length=32),
            preserve_default=True,
        ),
    ]
