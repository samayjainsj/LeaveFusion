# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eis', '0009_auto_20171008_0335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp_mtechphd_thesis',
            name='user',
        ),
        migrations.AlterField(
            model_name='emp_mtechphd_thesis',
            name='cosupervisors',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='emp_mtechphd_thesis',
            name='degree_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='emp_mtechphd_thesis',
            name='rollno',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='emp_mtechphd_thesis',
            name='s_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='emp_mtechphd_thesis',
            name='supervisors',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='emp_mtechphd_thesis',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]