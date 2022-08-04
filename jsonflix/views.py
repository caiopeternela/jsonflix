import json
import re

from django.http import HttpResponse
from django.shortcuts import render
from jsonflix.scripts.scripts import country_code_converter
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
    description = request.GET.get("description")
    limit = request.GET.get("limit")
    qs = Netflix.objects.all()

    if type:
        for show in qs:
            show.type = show.type.lower()
        qs = qs.filter(type__icontains=type).order_by('id')

    if title:
        qs = qs.filter(title__icontains=title).order_by('id')

    if country:
        if len(country) <= 3:
            country = country_code_converter(country)
        qs = qs.filter(country__icontains=country).order_by('id')

    if start_date and not end_date:
        qs = qs.filter(date_added=start_date).order_by('id')

    elif start_date and end_date:
        qs = qs.filter(date_added__range=(start_date, end_date)).order_by('date_added')

    if release_year:
        qs = qs.filter(release_year__gt=release_year).order_by('id')

    if cast:
        cast = cast.split('+')
        for actor in cast:
            actor = actor.replace('_', ' ')
            qs = qs.filter(cast__icontains=actor).order_by('id')

    if genres:
        genres = genres.split(',')
        for genre in genres:
            genre = genre.replace('_', ' ')
            qs = qs.filter(genres__icontains=genre).order_by('id')

    if description:
        description = set(description.split(','))

        desc = []
        for show in qs:
            ds = show.description
            ds = set(re.findall(r"[\w']+", ds))
            if description.issubset(ds):
                desc.append(show.id)
        qs = qs.filter(id__in=desc)

    if limit:
        limit = int(request.GET.get("limit"))
    qs = qs[:limit]

    dict = [Netflix.json_dict(content) for content in qs]

    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=2), content_type="application/json")
