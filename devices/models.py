from django.db import models

# Create your models here.
class Device(models.Model):

    name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.name