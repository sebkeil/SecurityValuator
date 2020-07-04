from django.db import models

# Create your models here.

class Enterprise(models.Model):
    enterprise_name = models.CharField(max_length=200)
    # enter all the accounting info?

    def __str__(self):
        return self.enterprise_name

