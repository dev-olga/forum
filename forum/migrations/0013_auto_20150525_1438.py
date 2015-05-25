# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_remove_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
        migrations.AlterField(
            model_name='thread',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]
