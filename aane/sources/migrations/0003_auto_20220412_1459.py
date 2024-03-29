# Generated by Django 3.2.3 on 2022-04-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0002_auto_20210518_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourceentry',
            name='image_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='percent_height',
            field=models.IntegerField(blank=True, null=True, verbose_name='% height'),
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='percent_left',
            field=models.IntegerField(blank=True, null=True, verbose_name='% to left'),
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='percent_right',
            field=models.IntegerField(blank=True, null=True, verbose_name='% to right'),
        ),
        migrations.AddField(
            model_name='sourceentry',
            name='percent_top',
            field=models.IntegerField(blank=True, null=True, verbose_name='% top to top'),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='aa_id',
            field=models.IntegerField(blank=True, help_text='Only if known for sure', null=True),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='low_day',
            field=models.IntegerField(blank=True, help_text='number', null=True, verbose_name='Day'),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='low_month',
            field=models.IntegerField(blank=True, choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'), (9, 'Sep'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec')], null=True, verbose_name='Month'),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='low_year',
            field=models.IntegerField(blank=True, help_text='Low year if range', null=True, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='operson_id',
            field=models.IntegerField(blank=True, help_text="blank if free. If unknown, choose the special 'Unknow Owner'", null=True, verbose_name='Owner ID'),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='page_num',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='upr_day',
            field=models.IntegerField(blank=True, help_text='upper range', null=True, verbose_name='Day'),
        ),
        migrations.AlterField(
            model_name='sourceentry',
            name='upr_month',
            field=models.IntegerField(blank=True, null=True, verbose_name='Month'),
        ),
    ]
