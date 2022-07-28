from django.shortcuts import render
from .models import Netflix
from django.http import HttpResponse
from .scripts.date_formatter import date_formatter
import json
import this

a = this


def home(request):
    return render(request, 'jsonflix/home.html')


def api(request):

    type = request.GET.get("type")
    title = request.GET.get("title")
    date_added = request.GET.get("date_added")

    qs = Netflix.objects.all()
    if type:
        for show in qs:
            show.type = show.type.lower()
        qs = qs.filter(type__contains=type)

    if title:
        qs = qs.filter(title__contains=title)

    if date_added:
        date = date_formatter(date_added)
        qs = qs.filter(date_added__contains=date)

    dict = [
        {
         "show_id": content.show_id,
         "type": content.type,
         "title": content.title,
         "director": content.director,
         "cast": content.cast,
         "country": content.country,
         "date_added": content.date_added,
         "release_year": content.release_year,
         "rating": content.rating,
         "duration": content.duration,
         "genres": content.genres,
         "description": content.description,
        }
        for content in qs
    ]
    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=2), content_type="application/json")
