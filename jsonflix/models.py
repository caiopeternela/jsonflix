from django.db import models


class Netflix(models.Model):
    show_id = models.CharField(max_length=36, unique=True, primary_key=True)
    type = models.CharField(max_length=36)
    title = models.CharField(max_length=512)
    director = models.CharField(max_length=512, null=True, blank=True)
    cast = models.TextField()
    country = models.CharField(max_length=512)
    date_added = models.CharField(max_length=36)
    release_year = models.CharField(max_length=36)
    rating = models.CharField(max_length=36)
    duration = models.CharField(max_length=64)
    genres = models.CharField(max_length=512)
    description = models.TextField()
