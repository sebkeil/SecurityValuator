from django.db import models
import datetime
# Create your models here.

class Enterprise(models.Model):
    enterprise_name = models.CharField(max_length=200)
    sector = models.CharField(max_length=200, default="all")
    description = models.CharField(max_length=400)
    date_added = models.DateTimeField(default=datetime.datetime.now())
    fair_value = models.FloatField()

    def __str__(self):
        return self.enterprise_name

