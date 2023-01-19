from django.db import models

# Create your models here.


class Currency(models.Model):
    full_name = models.CharField(max_length=50)
    short_form = models.CharField(max_length=10)