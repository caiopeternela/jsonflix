from django.db import models


class Netflix(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    type = models.CharField(max_length=36)
    title = models.CharField(max_length=512)
    director = models.CharField(max_length=512, null=True, blank=True)
    cast = models.TextField()
    country = models.CharField(max_length=512)
    date_added = models.DateTimeField(max_length=36, null=True, blank=True)
    release_year = models.CharField(max_length=36)
    rating = models.CharField(max_length=36)
    duration = models.CharField(max_length=64)
    genres = models.CharField(max_length=512)
    description = models.TextField()
