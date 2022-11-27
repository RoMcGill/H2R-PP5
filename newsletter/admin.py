"""
imports:
"""
from django.contrib import admin
from . models import Subscribers, SendNews


admin.site.register(Subscribers)
admin.site.register(SendNews)
