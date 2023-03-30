from django.db import models

from customer.models import customer
import uuid

# Create your models here.
class Order(models.Model):
    order_no = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_code = models.ForeignKey(customer, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    total_without_discount = models.FloatField(null=True, blank=True)
    gross = models.FloatField()

class OrderLines(models.Model):
    order_no = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    tax = models.FloatField()