from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

from django.contrib.auth.models import User

from django.core.cache import cache

# Create your models here.
# Товар для нашей витрины 
class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, # названия товаров не должны повторяться
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products', # все продукты в категории будут доступны через поле products
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'product-{self.pk}')
    
    def delete(self, using, keep_parents):
        pk = self.pk
        result = super().delete(using, keep_parents)
        cache.delete(f'product-{pk}')
        return result

# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name.title()

class Material(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    material = models.ForeignKey(Material, on_delete = models.CASCADE)

class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )