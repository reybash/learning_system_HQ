from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=32)
    datetime_start = models.DateTimeField()
    models.ForeignKey(User, on_delete=models.CASCADE)
    max_size_group = models.PositiveIntegerField(default=20)
    min_size_group = models.PositiveIntegerField(default=10)
    user = models.ForeignKey(User, models.PROTECT)


class ProductAccess(models.Model):
    user = models.ForeignKey(User, models.PROTECT)
    product = models.ForeignKey(Product, models.PROTECT, "accesses")
    is_valid = models.BooleanField(default=True)
