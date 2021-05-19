# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0012_auto_20150428_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourceentry',
            name='low_month',
            field=models.IntegerField(blank=True, verbose_name='Month (number)', null=True, choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'), (9, 'Sep'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec')]),
            preserve_default=True,
        ),
    ]
