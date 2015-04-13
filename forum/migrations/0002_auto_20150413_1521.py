# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to=b'posts'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thread',
            name='image',
            field=models.ImageField(default=None, upload_to=b'threads'),
            preserve_default=True,
        ),
    ]
