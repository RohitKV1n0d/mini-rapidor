from django.db import models

from customer.models import customer

def get_next_ord_number():
    try:
        latest_ord_number = Order.objects.all().order_by('-order_no').first().order_no
        if latest_ord_number:
            prefix = latest_ord_number[:3]
            number = int(latest_ord_number[3:]) + 1
            return '{}{:04}'.format(prefix, number)
        else:
            return "ORD0001"
    except:
        return "ORD0001"

# Create your models here.
class Order(models.Model):
    order_no =  models.CharField(primary_key=True, default=get_next_ord_number, max_length=100)
    customer_code = models.ForeignKey(customer, on_delete=models.CASCADE, null=True, blank=True)
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



