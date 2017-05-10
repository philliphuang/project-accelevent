# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Generic',
        ),
    ]
