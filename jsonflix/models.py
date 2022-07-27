from django.db import models
from typing import Any


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


    @property
    def search_type(self):
        return self.type.lower()


    @property
    def search_title(self):
        return self.title.lower()

    
    @property
    def search_director(self):
        return self.director.lower()


    @property
    def search_cast(self):
        return self.cast.lower()

    
    @property
    def search_country(self):
        return self.country.lower()

    
    @property
    def search_date_added(self):
        return self.date_added.lower()

    
    @property
    def search_duration(self):
        return self.duration.lower()

    
    @property
    def search_genres(self):
        return self.genres.lower()

    
    @property
    def search_description(self):
        return self.description.lower()
    