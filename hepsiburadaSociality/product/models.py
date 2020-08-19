from django.db import models


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False, default='', unique=True)
    image = models.CharField(max_length=255, blank=False, default='')
    price = models.CharField(max_length=25, blank=False, default='')

    class Meta:
        ordering = ['created']
