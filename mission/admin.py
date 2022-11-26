from django.contrib import admin
from .models import Mission
admin.site.disable_action('delete_selected')


# This ModelAdmin will not have delete_selected available
class MissionAdmin(admin.ModelAdmin):
    actions = ['edit_selected']


admin.site.register(Mission)
