# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20150417_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent_post',
            field=models.ForeignKey(default=None, blank=True, to='forum.Post', null=True),
            preserve_default=True,
        ),
    ]
