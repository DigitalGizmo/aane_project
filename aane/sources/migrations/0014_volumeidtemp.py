# Generated by Django 3.2.3 on 2022-06-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0013_alter_volume_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolumeIdTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.IntegerField(blank=True, null=True)),
                ('volume_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]