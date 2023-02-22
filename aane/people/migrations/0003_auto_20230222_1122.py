# Generated by Django 3.2.14 on 2023-02-22 16:22

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20210518_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operson',
            options={'ordering': ['pk'], 'verbose_name': 'Others/Enslavers'},
        ),
        migrations.AddField(
            model_name='aaperson',
            name='full_bio',
            field=django_quill.fields.QuillField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='operson',
            name='full_bio',
            field=django_quill.fields.QuillField(blank=True, default=''),
        ),
    ]
