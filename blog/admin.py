"""
imports:
"""
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    enable list display of fields
    search for fields
    prepopulate fields
    """
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
