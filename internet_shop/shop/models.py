from django.core.cache import cache
from django.db import models


def image_product_path(instance, filename):
    return f"products/{instance.subcategory.name}/{filename}"


class Category(models.Model):
    name = models.CharField(verbose_name="Имя категории", max_length=255)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    name = models.CharField(
        verbose_name="Имя суб-категории",
        max_length=255,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория суб-категории",
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Суб-категория"
        verbose_name_plural = "Суб-категории"


class Product(models.Model):
    name = models.CharField(verbose_name="Название продукта", max_length=255)
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    stock = models.IntegerField(verbose_name="Наличие на складе")

    available = models.BooleanField(verbose_name="Доступность", default=False)
    image = models.ImageField(verbose_name="Изображение", upload_to=image_product_path, blank=True)

    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        verbose_name="Суб-категория",
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.price} р."

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'product-{self.pk}')

    class Meta:
        ordering = ["name"]
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
