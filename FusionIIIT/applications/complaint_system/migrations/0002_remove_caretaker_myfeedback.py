# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-08 12:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caretaker',
            name='myfeedback',
        ),
    ]
