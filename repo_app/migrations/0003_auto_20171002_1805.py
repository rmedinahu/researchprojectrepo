# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repo_app', '0002_auto_20170927_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prj_membership', to='repo_app.Project'),
        ),
    ]