# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20150316_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aaperson',
            options={'ordering': ['pk'], 'verbose_name': 'African American'},
        ),
        migrations.AlterModelOptions(
            name='operson',
            options={'ordering': ['pk'], 'verbose_name': 'Other/Owner'},
        ),
        migrations.AddField(
            model_name='operson',
            name='legacy_owner_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='operson',
            name='original_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
