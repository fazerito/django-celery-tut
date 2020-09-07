from django.db import models

class City(models.Model):
    name = models.CharField(max_length=80, unique=False)
    description = models.CharField(max_length=250, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    temperature_feel = models.FloatField(null=True, blank=True)
    pressure = models.IntegerField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)
    updated = models.DateTimeField()

    def __str__(self):
        return self.name
