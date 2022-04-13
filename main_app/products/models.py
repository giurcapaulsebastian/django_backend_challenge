from unicodedata import decimal
from django.db import models

# Create your models here.

class Nutrition(models.Model):
    unit_choices = [
        ('g', 'gram'),
        ('Kcal', 'kcal'),
    ]
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=5, choices=unit_choices)
    value = models.DecimalField(default=0.00,max_digits=7,decimal_places=2)

    def __str__(self):
        return self.name

class Product(models.Model):
    status_choices = [
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=status_choices, default='ACTIVE')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'nutrition'], name='unique_nutrition_product')
        ]

    def __str__(self):
        return self.name