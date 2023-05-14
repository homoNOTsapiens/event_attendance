# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 20:54
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('event_date', models.DateField(blank=True, default=datetime.date.today)),
                ('event_admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255)),
                ('login', models.CharField(blank=True, max_length=255)),
                ('group', models.CharField(blank=True, max_length=255)),
                ('gps', models.CharField(blank=True, max_length=255)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='signin_sheets.Event')),
            ],
        ),
    ]
