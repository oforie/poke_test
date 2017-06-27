# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('log_regis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='first_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='last_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='users',
            name='dob',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
