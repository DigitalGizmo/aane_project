# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0007_auto_20150427_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sourceentry',
            old_name='original_id',
            new_name='legacy_id',
        ),
        migrations.RenameField(
            model_name='sourceentry',
            old_name='day',
            new_name='low_day',
        ),
        migrations.RenameField(
            model_name='sourceentry',
            old_name='month',
            new_name='low_month',
        ),
        migrations.RenameField(
            model_name='sourceentry',
            old_name='year_start',
            new_name='low_year',
        ),
        migrations.RenameField(
            model_name='sourceentry',
            old_name='year_end',
            new_name='upr_year',
        ),
    ]
