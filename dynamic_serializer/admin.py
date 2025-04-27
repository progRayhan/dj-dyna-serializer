# admin.py
from django.contrib import admin
from dynamic_serializer.models import SerializerConfig


@admin.register(SerializerConfig)
class SerializerConfigAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'step', 'field_name', 'field_type', 'required', 'max_length', 'write_only', 'default_value', 'help_text', 'model_name')
    search_fields = ('product_name', 'field_name', 'model_name')
    list_filter = ('step', 'field_type', 'required', 'write_only', 'model_name')
    ordering = ('product_name', 'step', 'field_name')
    list_per_page = 30
