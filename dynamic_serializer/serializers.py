from rest_framework import serializers
from dynamic_serializer.models import SerializerConfig
from django.core.validators import RegexValidator

FIELD_TYPE_MAP = {
    'char': serializers.CharField,
    'integer': serializers.IntegerField,
    'email': serializers.EmailField,
    'boolean': serializers.BooleanField,
    'date': serializers.DateField,
    'datetime': serializers.DateTimeField,
    'float': serializers.FloatField,
    'image': serializers.ImageField,
    'file': serializers.FileField,
}


class DynamicSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        step = kwargs.pop('step', None)
        super().__init__(*args, **kwargs)

        if step is not None:
            step_fields = SerializerConfig.objects.filter(step=step)
        else:
            step_fields = SerializerConfig.objects.filter(step__isnull=True)

        if not step_fields.exists():
            raise ValueError(f"No fields configured for step {step}")
        
        for field_def in step_fields:
            field_class = FIELD_TYPE_MAP.get(field_def.field_type)
            if not field_class:
                raise ValueError(f"Unknown field type: {field_def.field_type}")
            
            field_kwargs = {
                'required': field_def.required,
                'write_only': field_def.write_only,
            }

            if field_def.max_length:
                field_kwargs['max_length'] = field_def.max_length
            if field_def.default_value:
                field_kwargs['default'] = field_def.default_value
            if field_def.help_text:
                field_kwargs['help_text'] = field_def.help_text

            validators = []
            if field_def.regex_pattern:
                validators.append(RegexValidator(regex=field_def.regex_pattern))

            if validators:
                field_kwargs['validators'] = validators

            self.fields[field_def.field_name] = field_class(**field_kwargs)
