# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-08 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_hostel', '0002_auto_20190908_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingdetail',
            old_name='caretaker_id',
            new_name='caretaker',
        ),
    ]
