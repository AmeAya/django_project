from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    manufacturing_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    image = models.ImageField(default='default.png', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
