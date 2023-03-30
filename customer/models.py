from django.db import models

# Create your models here.
class customer(models.Model):
    customer_code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
