from django.db import models

# Create your models here.


class FeelLikeIt(models.Model):
    date = models.DateTimeField()
    reason = models.TextField()
    snap = models.ImageField()
    no = models.TextField()