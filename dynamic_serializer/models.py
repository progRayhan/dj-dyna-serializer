from django.db import models


class SerializerConfig(models.Model):
    product_name = models.CharField(max_length=255)
    step = models.PositiveIntegerField()
    field_name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=50)
    required = models.BooleanField(default=True)
    max_length = models.PositiveIntegerField(null=True, blank=True)
    write_only = models.BooleanField(default=False)
    default_value = models.CharField(max_length=255, null=True, blank=True)
    help_text = models.CharField(max_length=255, null=True, blank=True)
    regex_pattern = models.CharField(max_length=255, null=True, blank=True)
    model_name = models.CharField(max_length=100)

    def __str__(self):
        return f"product: {self.product_name} - step: {self.step} - field: {self.field_name}"
    
    class Meta:
        verbose_name = "Serializer Config"
        verbose_name_plural = "Serializer Configs"
        db_table = "serializer_config"
