from django.db import models

# Create your models here.



class Brands(models.Model):

    brand_name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.brand_name


class Brand_products(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True)
    brand_name = models.CharField(max_length=254, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    Product_name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Brand_products"

    def __str__(self):
        return self.brand_name


