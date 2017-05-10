# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_vendor_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='additional_info',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
