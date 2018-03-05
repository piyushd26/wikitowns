# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-28 11:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_auto_20180227_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiterecommendation',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='websiterecommendation',
            name='downvote',
            field=models.ManyToManyField(blank=True, related_name='website_downvote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='websiterecommendation',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='websiterecommendation',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='website_upvote', to=settings.AUTH_USER_MODEL),
        ),
    ]