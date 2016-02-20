# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AuthorID', models.AutoField(serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=50, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('Age', models.IntegerField(null=True, verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84', blank=True)),
                ('Country', models.CharField(max_length=50, verbose_name=b'\xe5\x9b\xbd\xe5\x88\xab')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.AutoField(serialize=False, primary_key=True)),
                ('AuthorID', models.IntegerField(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85ID')),
                ('Title', models.CharField(max_length=50, verbose_name=b'\xe4\xb9\xa6\xe5\x90\x8d')),
                ('Publisher', models.CharField(max_length=50, verbose_name=b'\xe5\x87\xba\xe7\x89\x88\xe5\x95\x86')),
                ('PublishDate', models.DateField(null=True, verbose_name=b'\xe5\x87\xba\xe7\x89\x88\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('Price', models.FloatField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
            ],
        ),
    ]
