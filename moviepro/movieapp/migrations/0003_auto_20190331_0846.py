# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-31 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_userdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='andharnumber',
            new_name='adharnumber',
        ),
        migrations.AlterField(
            model_name='userdata',
            name='showtime',
            field=models.DateTimeField(),
        ),
    ]
