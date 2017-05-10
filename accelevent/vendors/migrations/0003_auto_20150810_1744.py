# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_auto_20150810_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='place_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='price_level',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='rating',
            field=models.DecimalField(null=True, max_digits=2, decimal_places=1, blank=True),
        ),
    ]
