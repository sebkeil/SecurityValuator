from django.db import models
import datetime

class Article(models.Model):
    name = models.CharField(max_length=200)
    main_body = models.CharField(max_length=2000)
    date_added = models.DateTimeField(default=datetime.datetime.now())

