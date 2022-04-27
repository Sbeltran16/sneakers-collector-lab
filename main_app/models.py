from django.db import models
from django.urls import reverse

# Create your models here.
class Sneaker(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  price = models.IntegerField('Retail Price')


  def get_absolute_url(self):
      return reverse('detail', kwargs={'sneaker_id': self.id})

SIZES = (
  ('11', 'Size 11'),
  ('10', 'Size 10'),
  ('9', 'Size 9'),
  ('8','Size 8'),
  ('7','Size 7')
)

class Buyer(models.Model):
  name = models.CharField('Buyer Name', max_length=100)
  value = models.IntegerField('Resell Price')
  bought = models.DateField('Date Bought')
  size = models.CharField(
    'Size Bought',
    max_length=2,
    choices=SIZES,
    default=SIZES[0][0]
  )

  sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_size_display()} on {self.bought}"

  class Meta:
    ordering = ['-bought']