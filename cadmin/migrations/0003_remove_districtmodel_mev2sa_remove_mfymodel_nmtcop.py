# Generated by Django 5.0 on 2024-01-18 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0002_remove_districtmodel_v8yof2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='districtmodel',
            name='meV2sa',
        ),
        migrations.RemoveField(
            model_name='mfymodel',
            name='nmTCop',
        ),
    ]
