from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'ip_address']
    search_fields = ['name', 'ip_address']
    list_per_page = 25  # Pagination
    ordering = ['name']  # Default sort order