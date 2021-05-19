# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20150415_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='aaperson',
            name='freed_name',
            field=models.CharField(max_length=32, blank=True, default=''),
            preserve_default=True,
        ),
    ]
