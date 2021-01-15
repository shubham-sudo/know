"""
Validators
"""
from django.core.exceptions import ValidationError


def check_min(value):
    if isinstance(value, (int, float)) and value < 0:
        raise ValidationError("value should be greater than zero")
    return value
