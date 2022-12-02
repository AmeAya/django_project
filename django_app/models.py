from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    manufacturing_date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return str(self.name)
