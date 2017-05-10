# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='place_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='price_level',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='rating',
            field=models.DecimalField(null=True, max_digits=2, decimal_places=1),
        ),
    ]
