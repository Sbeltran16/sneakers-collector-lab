from django.db import models
from django.urls import reverse

# Create your models here.
class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()


    def get_absolute_url(self):
        return reverse('detail', kwargs={'sneaker_id': self.id})