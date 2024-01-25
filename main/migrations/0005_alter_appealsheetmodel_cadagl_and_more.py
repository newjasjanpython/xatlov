# Generated by Django 5.0 on 2024-01-20 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0003_remove_districtmodel_mev2sa_remove_mfymodel_nmtcop'),
        ('main', '0004_alter_appealsheetmodel_cadagl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appealsheetmodel',
            name='cAdagL',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='VXE6it', to='cadmin.mfymodel'),
        ),
        migrations.AlterField(
            model_name='appealsheetmodel',
            name='fA0b7j',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='XtYo0K', to='cadmin.districtmodel'),
        ),
    ]
