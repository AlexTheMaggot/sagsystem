from django.db import models
from mainapp.models import Measure


class Tender(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    measure = models.ForeignKey(Measure, on_delete=models.SET_NULL, null=True, blank=True)


class Provider(models.Model):
    name = models.CharField(max_length=200)


class Goods(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.PROTECT)
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=0)
