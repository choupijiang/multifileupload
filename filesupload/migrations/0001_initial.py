# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe8\xa1\xa8\xe5\x90\x8d')),
            ],
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'images', verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\x90\x8d')),
                ('datatable', models.ForeignKey(related_name='files', to='filesupload.DataTable')),
            ],
        ),
    ]
