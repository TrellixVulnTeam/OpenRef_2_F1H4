# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 20:20
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openref', '0006_auto_20170419_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 20, 20, 27, 159254, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 20, 20, 43, 464884, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
