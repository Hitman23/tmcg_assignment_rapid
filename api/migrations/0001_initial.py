# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number_of_contacts', models.IntegerField(default=0)),
            ],
        ),
    ]
