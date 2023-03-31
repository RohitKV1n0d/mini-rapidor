# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20230331_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_code',
            field=models.ForeignKey(blank=True, to='customer.customer', null=True),
        ),
    ]
