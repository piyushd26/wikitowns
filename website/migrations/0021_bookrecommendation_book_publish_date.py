# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20170426_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrecommendation',
            name='book_publish_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
