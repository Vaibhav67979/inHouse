from django.db import models


# Create your models here.


class Props(models.Model):
    prop_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=500)
    build_date = models.DateField()
    image = models.ImageField(upload_to="prop/images")

    def __str__(self):
        return self.prop_name

