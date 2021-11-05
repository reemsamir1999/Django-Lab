from django.db import models

# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.type

class Cast(models.Model):
    names = models.TextField(null=True)

    def __str__(self):
        return self.names

class Movie(models.Model):

    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    rate = models.PositiveIntegerField(null=True)
    production_date = models.DateField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    cast = models.ForeignKey(Cast, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name