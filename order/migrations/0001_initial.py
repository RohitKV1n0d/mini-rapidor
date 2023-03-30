# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_no', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('order_date', models.DateField(null=True, blank=True)),
                ('discount', models.FloatField(null=True, blank=True)),
                ('total_without_discount', models.FloatField(null=True, blank=True)),
                ('gross', models.FloatField()),
                ('customer_code', models.ForeignKey(to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_code', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('tax', models.FloatField()),
                ('order_no', models.ForeignKey(to='order.Order')),
            ],
        ),
    ]
