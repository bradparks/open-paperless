# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-03 06:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document_states', '0005_auto_20170803_0638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workflowtransitiontriggerevent',
            old_name='stored_event_type',
            new_name='event_type',
        ),
    ]
