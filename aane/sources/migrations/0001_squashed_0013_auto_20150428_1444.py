# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-05-18 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('sources', '0001_initial'), ('sources', '0002_auto_20150313_1211'), ('sources', '0003_auto_20150409_1654'), ('sources', '0004_auto_20150415_1408'), ('sources', '0005_auto_20150415_1426'), ('sources', '0006_delete_sourcecollection'), ('sources', '0007_auto_20150427_1615'), ('sources', '0008_auto_20150427_1618'), ('sources', '0009_auto_20150428_1102'), ('sources', '0010_auto_20150428_1315'), ('sources', '0011_auto_20150428_1317'), ('sources', '0012_auto_20150428_1324'), ('sources', '0013_auto_20150428_1444')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimarySource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('pvma_call_num', models.CharField(blank=True, max_length=32, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('year_start', models.IntegerField(default=0, verbose_name='Start year or single')),
                ('year_end', models.IntegerField(default=0, verbose_name='End year if range')),
            ],
        ),
        migrations.CreateModel(
            name='SourceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.CharField(max_length=255)),
                ('clarified', models.CharField(blank=True, default='', max_length=255)),
                ('aa_id', models.IntegerField(blank=True, null=True, verbose_name='aa id if known for sure')),
                ('operson_id', models.IntegerField(blank=True, null=True, verbose_name='2ndary person ID, only if aa id not known')),
                ('name_note', models.CharField(blank=True, default='', max_length=64, verbose_name='Name note if no id known')),
                ('primary_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sources.PrimarySource')),
                ('low_day', models.IntegerField(blank=True, null=True, verbose_name='Day of month (number)')),
                ('low_month', models.IntegerField(blank=True, choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'), (9, 'Sep'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec')], null=True, verbose_name='Month (number)')),
                ('upr_year', models.IntegerField(blank=True, null=True, verbose_name='Upper year if range')),
                ('low_year', models.IntegerField(blank=True, null=True, verbose_name='Lower year or single')),
                ('date_range', models.CharField(blank=True, default='', max_length=32, verbose_name='Date range (from title field)')),
                # ('location', models.CharField(blank=True, default='', max_length=32, verbose_name='Other location info')),
                ('page_num', models.CharField(blank=True, default='', max_length=64, verbose_name='Page info')),
                ('pvma_call_num', models.CharField(blank=True, default='', max_length=32)),
                ('date_note', models.CharField(blank=True, default='', max_length=124)),
                ('date_status', models.IntegerField(choices=[(0, 'As written'), (1, 'Before'), (2, 'After'), (3, 'Uncertain'), (4, 'Unknown')], default=0)),
                ('legacy_id', models.IntegerField(blank=True, null=True)),
                ('access_order', models.IntegerField(blank=True, null=True)),
                ('dollars', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('event', models.CharField(blank=True, default='', max_length=128)),
                ('farthing', models.IntegerField(blank=True, null=True)),
                ('legacy_enslaved_id', models.IntegerField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
                ('pence', models.IntegerField(blank=True, null=True)),
                ('pounds', models.IntegerField(blank=True, null=True)),
                ('shillings', models.IntegerField(blank=True, null=True)),
                ('transaction_note', models.CharField(blank=True, default='', max_length=64)),
                ('upr_day', models.IntegerField(blank=True, null=True, verbose_name='Day of month (number)')),
                ('upr_month', models.IntegerField(blank=True, null=True, verbose_name='Month (number)')),
                ('vol_book', models.CharField(blank=True, default='', max_length=32, verbose_name='Volume or book info')),
            ],
        ),
        migrations.AddField(
            model_name='primarysource',
            name='source_collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sources.SourceCollection'),
        ),
        migrations.AlterModelOptions(
            name='primarysource',
            options={'ordering': ['pk'], 'verbose_name': 'Source'},
        ),
        migrations.RemoveField(
            model_name='primarysource',
            name='pvma_call_num',
        ),
        migrations.RemoveField(
            model_name='primarysource',
            name='source_collection',
        ),
        migrations.AddField(
            model_name='primarysource',
            name='operson_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='O Person id if known'),
        ),
        migrations.AddField(
            model_name='primarysource',
            name='pub_info',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='primarysource',
            name='source_type',
            field=models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], max_length=32),
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='title',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='year_end',
            field=models.IntegerField(blank=True, null=True, verbose_name='End year if range'),
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='year_start',
            field=models.IntegerField(blank=True, null=True, verbose_name='Start year or single'),
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='primarysource',
            name='title',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
