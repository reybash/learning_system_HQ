from django.contrib import admin
from .models import Product, ProductAccess

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductAccess)
