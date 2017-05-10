# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20150730_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart_Item',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
