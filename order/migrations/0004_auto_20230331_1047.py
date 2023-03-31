# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20230331_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_no',
            field=models.CharField(default=order.models.get_next_ord_number, max_length=100, serialize=False, primary_key=True),
        ),
    ]
