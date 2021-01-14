from django.db import models

from authent.models import CustomUser, Address
from product.models import Product

# Create your models here.
## order data models ##
PAYMENT_MODE = [
    ('phonepe', 'Phone Pe'),
    ('googlepay', 'Google Pay')
]


class Order(models.Model):
    quantity = models.IntegerField()  # add validator for min check
    cost = models.FloatField()  # add validator for checking lowest price
    timestamp = models.DateTimeField('Time Stamp', default=timezone.now)
    ip = model.???  # (add IP field here)
    browser = models.ForeignKey('Browser')
    system = models.ForeignKey('System')
    payment_mode = models.ForeignKey('PaymentMode')
    payment_status = models.BooleanField(default=False)
    user = models.ForeignKey('CustomUser')


class Browser(models.Model):
    name = models.CharField(max_length=220)


class System(models.Model):
    name = models.CharField(max_length=120)


class PaymentMode(models.Model):
    mode = models.CharField('Mode', choices=PAYMENT_MODE)
    transaction_id = models.TextField()


class OrderProduct(models.Model):
    order = models.ForeignKey('Order')
    product = models.ForeignKey('Product')
    quantity = models.IntegerField()

## Shipping data models ##
class Shipping(models.Model):
    order = models.ForeignKey('Order')
    address = models.ForeignKey('Address')
    cost = models.FloatField()  # add validator for checking lowest price


class Track(models.Model):
    shipping = models.ForeignKey('Shipping')
    is_delivered = models.BooleanField(default=False)
