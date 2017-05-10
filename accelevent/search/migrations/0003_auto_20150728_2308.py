# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.AlterField(
            model_name='generic',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
