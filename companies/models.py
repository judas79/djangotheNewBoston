from django.db import models

# Create your models here.
# L37 inherit from import models
class Stock(models.Model):

    # L38 field attribute for company names, max. amount of characters
    ticker = models.CharField(unique=True, max_length=10)
    open = models.FloatField(max_length=20)
    # more accurate when rounding numbers than Float, must have decimal_places field to use with decimal points
    close = models.DecimalField(max_digits=5, decimal_places=3)
    volume = models.IntegerField()

    # L38 string representation of the ticker field, above
    def __str__(self):
        return self.ticker
