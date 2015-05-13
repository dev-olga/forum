# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20150513_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to=b'posts/', storage=django.core.files.storage.FileSystemStorage(location=b'static/forum/media/'), max_length=1024, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=models.ImageField(default=None, upload_to=b'threads/', storage=django.core.files.storage.FileSystemStorage(location=b'static/forum/media/'), max_length=1024, blank=True, null=True),
        ),
    ]
