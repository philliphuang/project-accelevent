# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_delete_generic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cart',
            field=models.ManyToManyField(to='search.Cart_Item', blank=True),
        ),
    ]
