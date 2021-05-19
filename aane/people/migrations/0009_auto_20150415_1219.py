# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20150413_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operson',
            name='slave_owner_id',
        ),
        migrations.AlterField(
            model_name='operson',
            name='legacy_owner_id',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operson',
            name='original_id',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operson',
            name='race',
            field=models.CharField(choices=[('white', 'white'), ('african_american', 'african_american'), ('native', 'native')], max_length=24),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operson',
            name='role',
            field=models.CharField(choices=[('owner', 'owner'), ('user', 'user'), ('service_provider', 'service_provider')], max_length=24),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operson',
            name='year_lower',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operson',
            name='year_upper',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
