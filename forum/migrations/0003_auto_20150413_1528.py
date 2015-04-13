# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20150413_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'posts'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='parent_post',
            field=models.ForeignKey(default=None, to='forum.Post', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='user_email',
            field=models.CharField(default=None, max_length=1024, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='user_name',
            field=models.CharField(default=None, max_length=1024, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'threads'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='user_email',
            field=models.CharField(default=None, max_length=1024, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thread',
            name='user_name',
            field=models.CharField(default=None, max_length=1024, null=True),
            preserve_default=True,
        ),
    ]
