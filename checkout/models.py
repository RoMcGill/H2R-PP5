"""
imports
"""
import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from brands.models import Brand_products
from profiles.models import UserProfile


class Order(models.Model):
    """
    models for Orders
    """
    order_number = models.CharField(
        max_length=32,
        null=False,
        editable=False
        )
    user_profile = models.ForeignKey(

        UserProfile,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orders'
        )
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
        )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
        )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False
        )
    country = CountryField(
        blank_label='country *',
        null=False, blank=False
        )
    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
        )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
        )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
        )
    street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    county = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    date = models.DateTimeField(
        auto_now_add=True
        )
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
        )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    original_cart = models.TextField(
        null=False,
        blank=False,
        default=''
        )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
        )

    def _generate_order_number(self):
        """
        generate a random, unique order number using uuid
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        update grand total when line item added
        """
        self.order_total = self.lineitems.aggregate(
                            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost =\
                 self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        override save to set order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    class to create line items
    """
    order = models.ForeignKey(
        Order, null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
        )
    product = models.ForeignKey(
        Brand_products,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    quantity = models.IntegerField(
        null=True,
        blank=True,
        default=0
        )
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
        )

    def save(self, *args, **kwargs):
        """
        override save to set order total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
