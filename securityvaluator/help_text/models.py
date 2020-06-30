from django.db import models

# Create your models here.

class HelpTutorial(models.Model):
    title = models.CharField(max_length=200)
    main_text = models.CharField(max_length=2000)
    publishing_date = models.DateField()


