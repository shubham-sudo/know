from django.db import models

from authent.validators import check_min

## product data models ##
class Product(models.Model):
    name = models.CharField(max_length=220)
    description = models.TextField()
    feature = models.TextField("Features")
    quantity = models.IntegerField(validators=[check_min])
    price = models.FloatField(validators=[check_min])
    in_stock = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Photos(models.Model):
    photo = models.ImageField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
