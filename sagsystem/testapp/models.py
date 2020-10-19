from django.db import models
from tender.models import Provider, Product


class TenderElement(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField()
