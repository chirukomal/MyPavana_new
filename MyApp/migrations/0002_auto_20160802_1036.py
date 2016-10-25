# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-02 05:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compltestockdetails',
            old_name='exp_data',
            new_name='exp_date',
        ),
        migrations.RenameField(
            model_name='compltestockdetails',
            old_name='manf_data',
            new_name='manf_date',
        ),
        migrations.RenameField(
            model_name='dealersinfo',
            old_name='dealer',
            new_name='person_info',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_used',
        ),
    ]
