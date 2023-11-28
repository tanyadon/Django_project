from django.db import models

# Create your models here.
class Sale(models.Model):
    Sale_NamePr = models.CharField(max_length=200)
    Sale_QuantityPr = models.BigIntegerField(max_length=9223372036854775807)
    Sale_PricePr = models.CharField(max_length=200)
    Sale_Date = models.DateField(auto_now=True)
    Sale_NameSalesman = models.CharField(max_length=200)
