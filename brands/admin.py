"""
imports:
"""
from django.contrib import admin
from .models import Brands, Brand_products

"""
register models
"""
admin.site.register(Brands)
admin.site.register(Brand_products)
