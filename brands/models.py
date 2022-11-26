"""
imports
"""
from django.db import models


class Brands(models.Model):
    """
    brands model
    """
    brand_email = models.EmailField(
        max_length=254, null=False,
        blank=False, default="Email")
    brand_name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        """
        fix admin calling brands brandss
        """
        verbose_name_plural = "Brands"

    def __str__(self):
        """
        return brand name to admin
        """
        return self.brand_name


class Brand_products(models.Model):
    """
    brand products model
    (products that belong to a brand)
    """
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True)
    brand_name = models.CharField(max_length=254, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    max_quant = models.IntegerField(null=True,
                                    blank=True,
                                    default=0)

    class Meta:
        """
        fix admin calling brand productss
        """
        verbose_name_plural = "Brand_products"

    def __str__(self):
        """
        return brand name to admin
        """
        return self.brand_name
