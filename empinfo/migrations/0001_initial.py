# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-07 11:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.CharField(max_length=400)),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=400)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Emp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
