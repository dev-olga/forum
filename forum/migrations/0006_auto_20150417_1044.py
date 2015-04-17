# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20150413_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to=b'posts/', storage=django.core.files.storage.FileSystemStorage(location=b'forum/static/media/'), max_length=1024, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='user_email',
            field=models.EmailField(default=None, max_length=1024, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=models.ImageField(default=None, upload_to=b'threads/', storage=django.core.files.storage.FileSystemStorage(location=b'forum/static/media/'), max_length=1024, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='user_email',
            field=models.EmailField(default=None, max_length=1024, null=True),
            preserve_default=True,
        ),
    ]
