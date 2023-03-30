from django.db import models

# Create your models here.
class product(models.Model):
    product_code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    tax = models.IntegerField()


