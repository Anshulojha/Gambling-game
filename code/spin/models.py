from django.db import models

# Create your models here.


class Spins(models.Model):
    # fields to be shown in db
    created = models.DateTimeField(auto_now_add=True)
    strip1 = models.CharField(max_length=100)
    strip2 = models.CharField(max_length=100)
    strip3 = models.CharField(max_length=100)
    strip4 = models.CharField(max_length=100)
    strip5 = models.CharField(max_length=100)
    strip6 = models.CharField(max_length=100)
    win = models.IntegerField()
