from django.db import models


def image_product_path(instance, filename):
    return f"products/{instance.category.name}/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=255)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()

    available = models.BooleanField(default=False)
    image = models.ImageField(upload_to=image_product_path, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.price} р."

    class Meta:
        ordering = ["name"]
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
