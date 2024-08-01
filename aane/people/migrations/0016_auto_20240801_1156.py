# Generated by Django 3.2.18 on 2024-08-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0015_auto_20240726_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operson',
            options={'ordering': ['last_name'], 'verbose_name': 'Others/Enslavers'},
        ),
        migrations.AddField(
            model_name='aaperson',
            name='tier',
            field=models.IntegerField(blank=True, choices=[('1', 'core'), ('2', 'wide')], null=True, verbose_name='Tier'),
        ),
        migrations.AlterField(
            model_name='operson',
            name='role',
            field=models.CharField(choices=[('owner', 'enslaver'), ('user', 'service consumer'), ('service_provider', 'service provider'), ('former', 'former enslaver')], max_length=24),
        ),
    ]
