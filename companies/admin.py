from django.contrib import admin
# L38 import the class Stock from the model.py file we created
from .models import Stock

# Register your models here.

# add ability to add or delete Stocks, from within sites admin panel
admin.site.register(Stock)

