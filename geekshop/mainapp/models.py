from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, blank=True, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name='имя', max_length=128, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    short_description = models.CharField(verbose_name='короткое описание', max_length=64, blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    price_with_discount = models.DecimalField(verbose_name='цена со скидкой', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    image = models.ImageField(upload_to='products_images', blank=True)
