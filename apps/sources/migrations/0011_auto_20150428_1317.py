# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0010_auto_20150428_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourceentry',
            name='page_num',
            field=models.CharField(blank=True, max_length=64, verbose_name='Page info', null=True),
            preserve_default=True,
        ),
    ]
