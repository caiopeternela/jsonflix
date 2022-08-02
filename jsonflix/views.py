import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Netflix


def home(request):
    return render(request, 'jsonflix/home.html')


def api(request):

    type = request.GET.get("type")
    title = request.GET.get("title")
    cast = request.GET.get("cast")
    country = request.GET.get("country")
    genres = request.GET.get("genres")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    release_year = request.GET.get("release_year")
    limit = request.GET.get("limit")
    qs = Netflix.objects.all()

    if type:
        for show in qs:
            show.type = show.type.lower()
        qs = qs.filter(type__contains=type).order_by('id')

    if title:
        qs = qs.filter(title__contains=title).order_by('id')

    if country:
        qs = qs.filter(country__contains=country).order_by('id')

    if start_date and not end_date:
        qs = qs.filter(date_added=start_date).order_by('id')

    elif start_date and end_date:
        qs = qs.filter(date_added__range=(start_date, end_date)).order_by('date_added')

    if release_year:
        qs = qs.filter(release_year__gt=release_year).order_by('id')

    if cast:
        cast = cast.split(' ')
        for actor in cast:
            actor = actor.replace('_', ' ')
            qs = qs.filter(cast__contains=actor).order_by('id')

    if genres:
        genres = genres.split(' ')
        for genre in genres:
            genre = genre.replace('_', ' ')
            qs = qs.filter(genres__contains=genre).order_by('id')

    if limit:
        limit = int(request.GET.get("limit"))
    qs = qs[:limit]

    dict = [
        {
            "id": content.id,
            "type": content.type,
            "title": content.title,
            "director": content.director,
            "cast": content.cast,
            "country": content.country,
            "date_added": str(content.date_added),
            "release_year": content.release_year,
            "rating": content.rating,
            "duration": content.duration,
            "genres": content.genres,
            "description": content.description,
        }
        for content in qs
    ]
    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=2), content_type="application/json")
