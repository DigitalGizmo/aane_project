# Generated by Django 3.2.3 on 2022-07-20 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0018_auto_20220709_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='primarysource',
            name='tiff_location',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='primary_source',
            field=models.ForeignKey(help_text='We will soon go by volume only', on_delete=django.db.models.deletion.PROTECT, to='sources.primarysource'),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='scan_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]