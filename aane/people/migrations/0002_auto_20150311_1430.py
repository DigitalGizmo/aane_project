# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('first_name', models.CharField(blank=True, null=True, max_length=32)),
                ('last_name', models.CharField(blank=True, null=True, max_length=32)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('unknown', 'unknown')], max_length=12)),
                ('bio', models.TextField(blank=True, null=True)),
                ('birth_year', models.IntegerField(default=0)),
                ('death_year', models.IntegerField(default=0)),
                ('role', models.CharField(choices=[('owner', 'owner'), ('user', 'user'), ('service_provider', 'service_provider')], max_length=12)),
                ('race', models.CharField(choices=[('white', 'white'), ('african_american', 'african_american'), ('native', 'native')], max_length=12)),
                ('slave_owner_id', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['pk'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='aaperson',
            options={'ordering': ['pk']},
        ),
    ]
