# Generated by Django 3.2.14 on 2023-02-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0020_auto_20220722_1509'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sourceentry',
            options={'ordering': ['primary_source', 'volume', 'low_year', 'low_month', 'low_day']},
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='image_status',
            field=models.IntegerField(choices=[(0, 'TBD'), (1, 'NotFound'), (2, 'NoImg'), (3, 'Scanned'), (5, 'Cnvrted'), (6, 'Posted'), (7, 'Hilite')], default=0, help_text='Image Status', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='percent_left',
            field=models.IntegerField(blank=True, null=True, verbose_name='% from left'),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='percent_right',
            field=models.IntegerField(blank=True, null=True, verbose_name='% width'),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='percent_top',
            field=models.IntegerField(blank=True, null=True, verbose_name='% from top'),
        ),
    ]