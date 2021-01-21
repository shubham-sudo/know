"""
Validators
"""
from django.core.exceptions import ValidationError


def check_min(value):
    if isinstance(value, (int, float)) and value < 0:
        raise ValidationError("value should be greater than zero")
    return value


def is_ip_address(value):
    """
    Soft validation for Ip address
    """
    not_valid = "IP address not valid"
    ip = value.split('.')
    if len(ip) != 4:
        raise ValidationError(not_valid)
    for i in ip:
        if not i.isdecimal():
            raise ValidationError(not_valid)
    
    return value
