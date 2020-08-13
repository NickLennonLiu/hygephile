from django.db import models


# Create your models here.
class Category(models.Model):
    catName = models.CharField(max_length=1000)

    def __str__(self):
        return self.catName


class Dos(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    dos = models.CharField(max_length=1000)

    def __str__(self):
        return self.dos
