
from email.policy import default
from tabnanny import verbose
from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=2000, unique=True, blank=True, null=True, verbose_name='url')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=2000, unique=True, blank=True, null=True, verbose_name='url')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='скидка в процентах')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'