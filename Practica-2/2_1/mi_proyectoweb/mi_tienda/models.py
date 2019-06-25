from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ClaseA (models.Model):
    image = models.ImageField(upload_to='static', default=0)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    power = models.FloatField()

    def __str__(self):
        return self.name
class Berlinas (models.Model):
    image = models.ImageField(upload_to='static', default=0)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    power = models.FloatField()

    def __str__(self):
        return self.name
