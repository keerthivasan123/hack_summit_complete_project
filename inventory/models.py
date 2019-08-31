from django.contrib import admin
# Register your models here.
from django.db import models
from datetime import date

# Create your models here.

class Device(models.Model):

    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()
    quantity = models.IntegerField()
    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

class Desktops(Device):
    pass

class Laptops(Device):
    pass

class Mobiles(Device):
    pass

class predict(models.Model):

    type = models.CharField(max_length=200, blank=False)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} for date: {1}'.format(self.type, self.date)