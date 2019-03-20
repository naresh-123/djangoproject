# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('productnumber', models.IntegerField()),
                ('productname', models.CharField(max_length=20)),
                ('productcost', models.IntegerField()),
                ('productclass', models.CharField(max_length=20)),
                ('productweight', models.IntegerField()),
            ],
        ),
    ]