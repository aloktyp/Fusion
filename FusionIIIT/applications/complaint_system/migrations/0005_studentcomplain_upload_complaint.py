# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-08 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_system', '0004_remove_studentcomplain_upload_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcomplain',
            name='upload_complaint',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
