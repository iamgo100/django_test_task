from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']

# Register your models here.
admin.site.register(MenuItem, MenuItemAdmin)