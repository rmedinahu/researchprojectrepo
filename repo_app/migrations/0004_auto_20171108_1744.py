# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo_app', '0003_auto_20171002_1805'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='membership',
            index=models.Index(fields=['member'], name='repo_app_me_member__a01dc0_idx'),
        ),
    ]