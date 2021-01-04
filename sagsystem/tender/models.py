from django.db import models
from mainapp.models import Measure
from django.contrib.auth.models import User
from django_pandas.managers import DataFrameManager


class Organization(models.Model):
    name = models.CharField(max_length=200)


class Tender(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    cpo_confirm = models.BooleanField(null=True, blank=True)
    cpo_confirm_date = models.DateTimeField(null=True, blank=True)
    cpo_comment = models.TextField(null=True, blank=True)
    cfo_confirm = models.BooleanField(null=True, blank=True)
    cfo_confirm_date = models.DateTimeField(null=True, blank=True)
    cfo_comment = models.TextField(null=True, blank=True)


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
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.SET_NULL, null=True, blank=True)


class Price(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    objects = DataFrameManager()


class SelectedPrice(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    sum = models.DecimalField(max_digits=12, decimal_places=2)


class Comment(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
