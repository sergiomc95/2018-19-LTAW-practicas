# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-25 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berlinas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=0, upload_to='static')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('power', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ClaseA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=0, upload_to='static')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('power', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
