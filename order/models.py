from django.db import models

from authent.models import CustomUser, Address
from authent.validators import check_min
from product.models import Product

## order data models ##
PAYMENT_MODE = [("phonepe", "Phone Pe"), ("googlepay", "Google Pay")]


class Order(models.Model):
    quantity = models.IntegerField(validators=[check_min])
    cost = models.FloatField(validators=[check_min])
    timestamp = models.DateTimeField(_("Time Stamp"), default=timezone.now)
    ip = model.???  # (add IP field here)
    browser = models.ForeignKey("Browser")
    system = models.ForeignKey("System")
    payment_mode = models.ForeignKey("PaymentMode")
    payment_status = models.BooleanField(default=False)
    user = models.ForeignKey("CustomUser")


class Browser(models.Model):
    name = models.CharField(max_length=220)


class System(models.Model):
    name = models.CharField(max_length=120)


class PaymentMode(models.Model):
    mode = models.CharField(choices=PAYMENT_MODE)
    transaction_id = models.TextField()


class OrderProduct(models.Model):
    order = models.ForeignKey("Order")
    product = models.ForeignKey("Product")
    quantity = models.IntegerField()


## Shipping data models ##
class Shipping(models.Model):
    order = models.ForeignKey("Order")
    address = models.ForeignKey("Address")
    cost = models.FloatField(default=0)


class Track(models.Model):
    shipping = models.ForeignKey("Shipping")
    is_delivered = models.BooleanField(default=False)
