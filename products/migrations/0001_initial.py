# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('tax', models.IntegerField()),
            ],
        ),
    ]
