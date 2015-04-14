# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20150413_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, max_length=1024, storage=django.core.files.storage.FileSystemStorage(location=b'/forum/media/'), null=True, upload_to=b'posts'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=models.ImageField(default=None, max_length=1024, storage=django.core.files.storage.FileSystemStorage(location=b'/forum/media/'), null=True, upload_to=b'threads'),
            preserve_default=True,
        ),
    ]
