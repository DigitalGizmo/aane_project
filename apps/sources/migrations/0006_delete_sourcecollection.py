# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0005_auto_20150415_1426'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SourceCollection',
        ),
    ]
