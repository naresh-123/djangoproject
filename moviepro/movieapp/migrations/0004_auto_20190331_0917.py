# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-31 03:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_auto_20190331_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='adharnumber',
            new_name='adharnumber1',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='mobile',
            new_name='mobile1',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='moviename',
            new_name='moviename1',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='showtime',
            new_name='showtime1',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='username',
            new_name='username1',
        ),
    ]
