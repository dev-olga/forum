# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20150417_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subject',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, max_length=1024, null=True, upload_to=b'posts/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='user_email',
            field=models.EmailField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='user_name',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=models.ImageField(default=None, max_length=1024, null=True, upload_to=b'threads/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='subject',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='user_email',
            field=models.EmailField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='user_name',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
