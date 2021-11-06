from django.db import models

# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=255, null=True)
    class Meta:
        verbose_name_plural = "categories"


    def __str__(self):
        return self.type

class Actor(models.Model):
    name = models.TextField(null=True)

    def __str__(self):
        return self.name


class Code(models.Model):
    num = models.IntegerField(null=True)

    def __str__(self):
        return str(self.num)

class Review(models.Model):
    comment = models.TextField(null=True, blank=True)
    movie = models.ForeignKey("Movie",on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.comment


class Movie(models.Model):

    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    rate = models.PositiveIntegerField(blank=True,null=True)
    likes = models.IntegerField(default=0, null=True)
    production_date = models.DateField(blank=True)
    poster = models.ImageField(upload_to='movie/images')
    actors = models.ManyToManyField(Actor)
    categories = models.ManyToManyField(Category)
    code = models.OneToOneField(Code,  on_delete = models.CASCADE)

    def __str__(self):
        return self.name