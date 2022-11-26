"""
imports:
"""
from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    class to add search field in admin panel for contact
    """
    search_fields = ('name', 'subject')
