from django.db import models

class Sensor(models.Model):
    oid = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    community = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    def __str__(self):
        return self.oid

class Server(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    sensors = models.ManyToManyField(Sensor, blank=True)
    def __str__(self):
        return self.name