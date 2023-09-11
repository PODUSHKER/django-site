from django.db import models
from users.models import *
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    image = models.FileField(verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    quantity = models.PositiveIntegerField(verbose_name='Колличество товаров', default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

class BasketQuerySet(models.QuerySet):

    def total_price(self):
        return sum(i.basket_price() for i in self)

    def total_quantity(self):
        return sum(i.quantity for i in self)

class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина, {self.user} - {self.product}'

    def basket_price(self):
        return self.quantity * self.product.price
