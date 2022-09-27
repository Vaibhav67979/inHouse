from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to="prop/images", default="")
    popu = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name
