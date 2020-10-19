from django.db import models
from mainapp.models import Measure
from django.contrib.auth.models import User
from django_pandas.managers import DataFrameManager


class Tender(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    measure = models.ForeignKey(Measure, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)


class Provider(models.Model):
    name = models.CharField(verbose_name='Товар', max_length=200)
    contact = models.CharField(max_length=200, null=True, blank=True)
    phone_1 = models.CharField(max_length=200, null=True, blank=True)
    phone_2 = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    inn = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Participant(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE, null=True, blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True, blank=True)


class Goods(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='goods')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.SET_NULL, null=True, blank=True, related_name='goods')
    price = models.IntegerField()
    objects = DataFrameManager()
