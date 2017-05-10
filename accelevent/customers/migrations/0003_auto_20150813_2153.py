# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150813_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cart',
            field=models.ManyToManyField(to='vendors.Vendor', blank=True),
        ),
    ]
