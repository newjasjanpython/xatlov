# Generated by Django 5.0 on 2024-01-11 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0002_remove_districtmodel_v8yof2'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appealsheetmodel',
            name='cAdagL',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='VXE6it', to='cadmin.mfymodel'),
        ),
        migrations.AlterField(
            model_name='appealsheetmodel',
            name='fA0b7j',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='XtYo0K', to='cadmin.districtmodel'),
        ),
    ]