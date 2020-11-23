from django.db import models


class Brands(models.Model):
    brands = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='brand')
    cls = models.CharField(max_length=100, default='n')
    value = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.brands

    class Meta:
        verbose_name_plural = 'Brands'


class PriceRange(models.Model):
    label = models.CharField(max_length=100)
    price_range = models.BigIntegerField()
    name = models.CharField(max_length=100, default='price_range')
    cls = models.CharField(max_length=100, default='n')
    min_value = models.BigIntegerField()
    max_value = models.BigIntegerField()

    def __str__(self):
        return str(self.price_range)

    class Meta:
        verbose_name_plural = 'Price Range'


class RAM(models.Model):
    RAM = models.IntegerField()
    name = models.CharField(max_length=100, default='RAM')
    cls = models.CharField(max_length=100, default='n')
    value = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.RAM)

    class Meta:
        verbose_name_plural = 'RAM'
