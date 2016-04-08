# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-08 06:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20160408_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='Votes', to=settings.AUTH_USER_MODEL, verbose_name=b'Users'),
        ),
    ]
