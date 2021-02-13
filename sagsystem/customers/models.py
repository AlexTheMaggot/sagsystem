# DjangoImports
from django.db import models
# End DjangoImports


class Customer(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=1, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
