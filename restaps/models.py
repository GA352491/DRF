from django.db import models


# Create your models here.


class Movies(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    language = models.CharField(max_length=120, null=True, blank=True)
    genre = models.CharField(max_length=120, null=True, blank=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.title
