from django.db import models


# Create your models here.


class Colaborators(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)

    def __str__(self):
        return self.name
